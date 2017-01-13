# coding:utf-8
import re
import sys
import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_webdav2ccsds
import time
import webdav_client
from requests.exceptions import ConnectionError
reload(sys)
sys.setdefaultencoding('utf-8')


class MainDlg(QDialog, ui_webdav2ccsds.Ui_ccsds_dialog):
    def __init__(self, parent=None):
        super(MainDlg, self).__init__(parent)
        self.setupUi(self)
        self.updateUi()

    @pyqtSignature("")
    def on_qc_btn_clicked(self):
        # print("我是快速链接按钮，点我了啦！")
        self.add_item_to_log(u'系统提示：您点击了快速链接！')
        self.host = self.host_edit.text()
        self.port = self.port_edit.text()
        # username = self.user_edit.text()
        # pwd = self.pwd_edit.text()
        print "Host:", self.host
        # self.add_item_to_log(u"您输入的主机地址是:"+host)
        print "Port:", self.port
        # self.add_item_to_log(u"您输入的端口号是:"+port)
        # print "username:", username
        # print "password:", pwd
        self.connect_to_host()

    def updateUi(self):
        print u"更新UI啦！"
        # Create an empty model for the log list's data
        self.log_listView_model = QStandardItemModel(self.log_listView)
        self.remote_listView_model = QStandardItemModel(self.remote_listView)
        self.local_listView_model = QStandardItemModel(self.local_listView)
        for f in os.listdir("."):
            # print f
            self.add_item_to_local(f)


    def add_item_to_log(self, item):
        """往底部的log_listView中添加信息"""
        print item
        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 获取当前时间用于生成日志
        item = QStandardItem(now+u"   "+item)
        self.log_listView_model.appendRow(item)
        self.log_listView.setModel(self.log_listView_model)
        self.log_listView.show()

    def add_item_to_remote(self, item):
        """往远程文件显示list_view中添加信息"""
        item = QStandardItem(unicode(item.name))
        self.remote_listView_model.appendRow(item)
        self.remote_listView.setModel(self.remote_listView_model)
        self.show()

    def add_item_to_local(self, item):
        """往本地文件显示list_view中添加信息"""
        item = QStandardItem(unicode(item))
        self.local_listView_model.appendRow(item)
        self.local_listView.setModel(self.local_listView_model)
        self.show()



    def connect_to_host(self):
        """根据输入的信息，连接webdav主机"""
        self.add_item_to_log(u"正在为您链接主机...")

        try:
            webdav = webdav_client.Client(self.host,
                                          username='nssc',
                                          password='123456',
                                          protocol='http',
                                          port=int(self.port),
                                          verify_ssl=False)
            print webdav.ls()
            for item in webdav.ls():
                self.add_item_to_remote(item)
            # print "链接主机成功"
            self.add_item_to_log(u"链接主机成功")
        except ConnectionError as e:
            # print "链接失败，请重试！"
            self.add_item_to_log(u"链接主机失败，请重试!")






if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MainDlg()
    form.show()
    app.exec_()