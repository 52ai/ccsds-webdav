# coding:utf-8
import easywebdav
import os
# Start off by creating a client object. Username and
# password may be omitted if no authentication is needed.
# webdav = easywebdav.connect('192.168.102.205, username='nssc', password='123456',protocol='https', port=443, verify_ssl=False)
webdav = easywebdav.connect('localhost', username='nssc', password='123456',protocol='http', port=80, verify_ssl=False)
# Do some stuff:
#webdav.mkdir('some_dir')
#webdav.rmdir('another_dir')
#webdav.download('remote/path/to/file', 'local/target/file')
#webdav.upload('local/path/to/file', 'remote/target/file')
print webdav.ls("/webdav/")
#webdav.mkdir("/webdav/test_mkdir", safe=True)
webdav.rmdir("/webdav/test_mkdir", safe=True)
print webdav.exists("/webdav")
webdav.upload(os.getcwd()+"/testFile","/webdav/testFile" )
webdav.download("/webdav/passwd.dav", os.getcwd()+"/passwd.dav")
print os.getcwd()
