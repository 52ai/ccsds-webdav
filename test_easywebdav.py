# coding:utf-8
import webdav_client
import os

# Start off by creating a client object. Username and
# password may be omitted if no authentication is needed.
# webdav = easywebdav.connect('192.168.102.205, username='nssc', password='123456',protocol='https', port=443, verify_ssl=False)
webdav =webdav_client.Client('localhost', username='nssc', password='123456',protocol='http', port=80, verify_ssl=False)
"""
webdav.mkdir('some_dir')
webdav.rmdir('another_dir')
webdav.download('remote/path/to/file', 'local/target/file')
webdav.upload('local/path/to/file', 'remote/target/file')
"""

# webdav.cd("/webdav/") # 在webdav客户端类中初始化了当前目录为/webdav/所以不需要cd进去

print webdav.ls()
for i in webdav.ls():
    print i.name
# webdav.cd("/webdav/testFolder/")
# print webdav.ls()
# webdav.mkdir("/webdav/test_mkdir", safe=True) # 新建一个目录
# webdav.rmdir("/webdav/test_mkdir", safe=True) # 删除一个目录
# print webdav.exists("/webdav")
# webdav.upload(os.getcwd()+"/auto_git.sh","/webdav/auto_git.sh" ) # 上传文件
# webdav.download("/webdav/passwd.dav", os.getcwd()+"/passwd.dav") # 下载文件
# print os.getcwd()
# webdav.delete("webdav/auto_git.sh")
