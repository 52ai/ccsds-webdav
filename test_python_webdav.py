#coding:utf-8
import python_webdav 
client_object = python_webdav.Client('localhost/webdav/')
client_object.set_connection(username='nssc', password='123456')
help(python_webdav)

print python_webdav.get_version()


