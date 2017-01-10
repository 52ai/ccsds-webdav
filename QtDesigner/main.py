# coding:utf-8
import re
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_webdav2ccsds
import time

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
        host = self.host_edit.text()
        port = self.port_edit.text()
        # username = self.user_edit.text()
        # pwd = self.pwd_edit.text()
        print "Host:", host
        # self.add_item_to_log(u"您输入的主机地址是:"+host)
        print "Port:", port
        # self.add_item_to_log(u"您输入的端口号是:"+port)
        # print "username:", username
        # print "password:", pwd
        self.connect_to_host()

    def updateUi(self):
        print u"更新UI啦！"
        # Create an empty model for the log list's data
        self.log_listView_model = QStandardItemModel(self.log_listView)

    def add_item_to_log(self, item):
        """往底部的log_listView中添加信息"""
        print item
        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 获取当前时间用于生成日志
        item = QStandardItem(now+u"   "+item)
        self.log_listView_model.appendRow(item)
        self.log_listView.setModel(self.log_listView_model)
        self.log_listView.show()
    def connect_to_host(self):
        """根据输入的信息，连接webdav主机"""
        self.add_item_to_log(u"正在为您链接主机...")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MainDlg()
    form.show()
    app.exec_()