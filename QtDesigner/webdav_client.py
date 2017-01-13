# coding:utf-8
# Requests是唯一一个非转基因的Python HTTP库，人类可以安全享用
# 更多详情可以访问　http://docs.python-requests.org/zh_CN/latest/
import requests
import platform
from numbers import Number
import xml.etree.cElementTree as et
from collections import namedtuple
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

py_majversion, py_minversion, py_revversion = platform.python_version_tuple()
# 下面是为了解决python版本问题
# The httplib module has been renamed to http.client in Python 3.
if py_majversion == '2':
    from httplib import responses as HTTP_CODES
    from urlparse import urlparse
    from urllib import unquote
else:
    from http.client import responses as HTTP_CODES
    from urllib.parse import urlparse
    from urllib import unquote

DOWNLOAD_CHUNK_SIZE_BYTES = 1 * 1024 * 1024


class WebdavException(Exception):
    pass


class ConnectionFailed(WebdavException):
    pass


def codestr(code):
    return HTTP_CODES.get(code, 'UNKNOWN')
    # 获得responses中的HTTP_OODES类型，要是没有找到则返回'UNKNOWN',对照表见python说明文档　
    # https://hg.python.org/cpython/file/2.7/Lib/httplib.py

File = namedtuple('File', ['name', 'size', 'mtime', 'ctime', 'contenttype'])  # 文件信息的元组格式


def prop(elem, name, default=None):
    child = elem.find('.//{DAV:}' + name)
    return default if child is None else unquote(child.text)


def elem2file(elem):
    return File(
        prop(elem, 'href'),
        int(prop(elem, 'getcontentlength', 0)),
        prop(elem, 'getlastmodified', ''),
        prop(elem, 'creationdate', ''),
        prop(elem, 'getcontenttype', ''),
    )


class OperationFailed(WebdavException):
    _OPERATIONS = dict(
        HEAD="get header",
        GET="download",
        PUT="upload",
        DELETE="delete",
        MKCOL="create directory",
        PROPFIND="list directory",
        )

    def __init__(self, method, path, expected_code, actual_code):
        self.method = method
        self.path = path
        self.expected_code = expected_code
        self.actual_code = actual_code
        operation_name = self._OPERATIONS[method]
        self.reason = 'Failed to {operation_name} "{path}"'.format(**locals())
        expected_codes = (expected_code,) if isinstance(expected_code, Number) else expected_code
        expected_codes_str = ", ".join('{0} {1}'.format(code, codestr(code)) for code in expected_codes)
        actual_code_str = codestr(actual_code)
        msg = '''\
{self.reason}.
  Operation     :  {method} {path}
  Expected code :  {expected_codes_str}
  Actual code   :  {actual_code} {actual_code_str}'''.format(**locals())
        super(OperationFailed, self).__init__(msg)


class Client(object):
    def __init__(self, host, port=0, auth=None, username=None, password=None,
                 protocol='http', verify_ssl=True, path=None, cert=None):
        # 如果没有指定端口号，则根据链接的协议来给定，若为https协议则port为443，若为http协议则端口号为80
        if not port:
            port = 443 if protocol == 'https' else 80
        # 根绝输入生成要访问的webdav URL
        self.baseurl = '{0}://{1}:{2}'.format(protocol, host, port)
        if path:
            self.baseurl = '{0}/{1}'.format(self.baseurl, path)
        # 设定当前目录，默认为根目录
        self.cwd = '/webdav/'
        # print"当前目录为："+self.cwd
        # 利用Requests（Python HTTP库）的seession来使用会话对象
        self.session = requests.session()
        self.session.verify = verify_ssl  # 为HTTPS请求验证SSL证书
        self.session.stream = True  # 响应体内容工作流设置参数

        if cert:
            self.session.cert = cert # verify仅应用于主机证书，但可以使用cert参数指定一个本地证书用作客户端证书,可以是单个文件（包含秘钥和证书），或者一个包含两个文件路劲的元祖
        if auth:
            self.session.auth = auth  # 自定义身份验证
        elif username and password:
            self.session.auth = (username, password)  # 采用用户名和密码进行验证
        # 到此，与webdav服务器的初始化链接结束

    def _send(self, method, path, expected_code, **kwargs):
        url = self._get_url(path)
        response = self.session.request(method, url, allow_redirects=False, **kwargs)   # 关键性语句！！！
        # help(self.session)
        # help(response)
        print "status_code:", response.status_code
        print "headers:", response.headers
        # print "content:", response.content
        print "request:", response.request
        if isinstance(expected_code, Number) and response.status_code != expected_code \
            or not isinstance(expected_code, Number) and response.status_code not in expected_code:
            raise OperationFailed(method, path, expected_code, response.status_code)  # status_code 为状态响应码
        return response

    def _get_url(self, path):
        path = str(path).strip()
        if path.startswith('/'):
            return self.baseurl + path
        # print self.baseurl
        # print self.cwd
        # print path
        return "".join((self.baseurl, self.cwd, path))

    def ls(self, remote_path='.'):
        """实现webdav PROPFIND方法,也就是list命令功能，也就是MULTI_STATUS,状态码207"""
        headers = {'Depth': '1'}
        response = self._send('PROPFIND', remote_path, (207, 301), headers=headers)  # 返回一个xml格式的数据

        # Redirect
        if response.status_code == 301:
            url = urlparse(response.headers['location'])
            return self.ls(url.path)
        # print response.content
        tree = et.fromstring(response.content)
        # The fromstring() function is the easiest way to parse a string(xml)
        # fromstring() parses XML from a string directly into an Element, which is the root element of the parsed tree
        # print tree
        # print tree.findall('{DAV:}response')
        return [elem2file(elem) for elem in tree.findall('{DAV:}response')]  # 将找到的数据项转为文件

    def cd(self, path):
        path = path.strip()
        if not path:
            return
        stripped_path = '/'.join(part for part in path.split('/') if part) + '/'
        if stripped_path == '/':
            self.cwd = stripped_path
        elif path.startswith('/'):
            self.cwd = '/' + stripped_path
        else:
            self.cwd += stripped_path

    def mkdir(self, path, safe=False):
        """实现webdav　mkdir命令，亦即创建文件夹的功能"""
        expected_codes = 201 if not safe else (201, 301, 405)
        # 当safe为True时，如果新创建的目录已存在则不予创建
        self._send('MKCOL', path, expected_codes)

    def mkdirs(self, path):
        """批量创建文件夹"""
        dirs = [d for d in path.split('/') if d]
        if not dirs:
            return
        if path.startswith('/'):
            dirs[0] = '/' + dirs[0]
        old_cwd = self.cwd
        try:
            for dir in dirs:
                try:
                    self.mkdir(dir, safe=True)
                except Exception as e:
                    if e.actual_code == 409:
                        raise
                finally:
                    self.cd(dir)
        finally:
            self.cd(old_cwd)

    def rmdir(self, path, safe=False):
        """删除目录"""
        path = str(path).rstrip('/') + '/'
        expected_codes = 204 if not safe else (204, 404)
        self._send('DELETE', path, expected_codes)

    def delete(self, path):
        """删除文件"""
        self._send('DELETE', path, 204)  # 204表示NO_CONTENT,删除之后期待返回的HTTP_CODES为204

    def upload(self, local_path_or_fileobj, remote_path):
        """上传文件"""
        if isinstance(local_path_or_fileobj, basestring):
            with open(local_path_or_fileobj, 'rb') as f:
                self._upload(f, remote_path)
        else:
            self._upload(local_path_or_fileobj, remote_path)

    def _upload(self, fileobj, remote_path):
        self._send('PUT', remote_path, (200, 201, 204), data=fileobj)

    def download(self, remote_path, local_path_or_fileobj):
        """下载文件"""
        response = self._send('GET', remote_path, 200, stream=True)
        if isinstance(local_path_or_fileobj, basestring):
            with open(local_path_or_fileobj, 'wb') as f:
                self._download(f, response)
        else:
            self._download(local_path_or_fileobj, response)

    def _download(self, fileobj, response):
        for chunk in response.iter_content(DOWNLOAD_CHUNK_SIZE_BYTES):
            fileobj.write(chunk)

    def exists(self, remote_path):
        """判断文件是否存在"""
        response = self._send('HEAD', remote_path, (200, 301, 404))
        return True if response.status_code != 404 else False
