# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'webdav2ccsds.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ccsds_dialog(object):
    def setupUi(self, ccsds_dialog):
        ccsds_dialog.setObjectName(_fromUtf8("ccsds_dialog"))
        ccsds_dialog.resize(979, 606)
        ccsds_dialog.setMinimumSize(QtCore.QSize(979, 606))
        ccsds_dialog.setMaximumSize(QtCore.QSize(979, 614))
        ccsds_dialog.setSizeGripEnabled(False)
        self.head_frame = QtGui.QFrame(ccsds_dialog)
        self.head_frame.setGeometry(QtCore.QRect(-10, 0, 1001, 51))
        self.head_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.head_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.head_frame.setObjectName(_fromUtf8("head_frame"))
        self.qc_comb = QtGui.QComboBox(self.head_frame)
        self.qc_comb.setGeometry(QtCore.QRect(470, 10, 21, 31))
        self.qc_comb.setObjectName(_fromUtf8("qc_comb"))
        self.qc_comb.addItem(_fromUtf8(""))
        self.qc_comb.addItem(_fromUtf8(""))
        self.port_label = QtGui.QLabel(self.head_frame)
        self.port_label.setGeometry(QtCore.QRect(220, 10, 31, 31))
        self.port_label.setObjectName(_fromUtf8("port_label"))
        self.user_label = QtGui.QLabel(self.head_frame)
        self.user_label.setGeometry(QtCore.QRect(590, 10, 41, 31))
        self.user_label.setObjectName(_fromUtf8("user_label"))
        self.port_edit = QtGui.QLineEdit(self.head_frame)
        self.port_edit.setGeometry(QtCore.QRect(260, 10, 51, 31))
        self.port_edit.setObjectName(_fromUtf8("port_edit"))
        self.user_edit = QtGui.QLineEdit(self.head_frame)
        self.user_edit.setGeometry(QtCore.QRect(630, 10, 131, 31))
        self.user_edit.setObjectName(_fromUtf8("user_edit"))
        self.pwd_edit = QtGui.QLineEdit(self.head_frame)
        self.pwd_edit.setGeometry(QtCore.QRect(840, 10, 131, 31))
        self.pwd_edit.setObjectName(_fromUtf8("pwd_edit"))
        self.host_label = QtGui.QLabel(self.head_frame)
        self.host_label.setGeometry(QtCore.QRect(40, 10, 71, 31))
        self.host_label.setObjectName(_fromUtf8("host_label"))
        self.pwd_label = QtGui.QLabel(self.head_frame)
        self.pwd_label.setGeometry(QtCore.QRect(770, 10, 81, 31))
        self.pwd_label.setObjectName(_fromUtf8("pwd_label"))
        self.host_edit = QtGui.QLineEdit(self.head_frame)
        self.host_edit.setGeometry(QtCore.QRect(80, 10, 131, 31))
        self.host_edit.setMaxLength(342764)
        self.host_edit.setObjectName(_fromUtf8("host_edit"))
        self.qc_btn = QtGui.QPushButton(self.head_frame)
        self.qc_btn.setGeometry(QtCore.QRect(330, 10, 141, 31))
        self.qc_btn.setObjectName(_fromUtf8("qc_btn"))
        self.bl_frame = QtGui.QFrame(ccsds_dialog)
        self.bl_frame.setGeometry(QtCore.QRect(20, 80, 461, 291))
        self.bl_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.bl_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.bl_frame.setObjectName(_fromUtf8("bl_frame"))
        self.bl_h_frame = QtGui.QFrame(self.bl_frame)
        self.bl_h_frame.setGeometry(QtCore.QRect(0, 0, 461, 51))
        self.bl_h_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.bl_h_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.bl_h_frame.setObjectName(_fromUtf8("bl_h_frame"))
        self.local_label = QtGui.QLabel(self.bl_h_frame)
        self.local_label.setGeometry(QtCore.QRect(10, 10, 71, 31))
        self.local_label.setObjectName(_fromUtf8("local_label"))
        self.local_comb = QtGui.QComboBox(self.bl_h_frame)
        self.local_comb.setGeometry(QtCore.QRect(60, 10, 391, 31))
        self.local_comb.setObjectName(_fromUtf8("local_comb"))
        self.local_treeView = QtGui.QTreeView(self.bl_frame)
        self.local_treeView.setGeometry(QtCore.QRect(0, 50, 461, 241))
        self.local_treeView.setObjectName(_fromUtf8("local_treeView"))
        self.br_frame = QtGui.QFrame(ccsds_dialog)
        self.br_frame.setGeometry(QtCore.QRect(500, 80, 461, 291))
        self.br_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.br_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.br_frame.setObjectName(_fromUtf8("br_frame"))
        self.br_h_frame = QtGui.QFrame(self.br_frame)
        self.br_h_frame.setGeometry(QtCore.QRect(0, 0, 461, 51))
        self.br_h_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.br_h_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.br_h_frame.setObjectName(_fromUtf8("br_h_frame"))
        self.remote_label = QtGui.QLabel(self.br_h_frame)
        self.remote_label.setGeometry(QtCore.QRect(10, 10, 71, 31))
        self.remote_label.setObjectName(_fromUtf8("remote_label"))
        self.remote_comb = QtGui.QComboBox(self.br_h_frame)
        self.remote_comb.setGeometry(QtCore.QRect(80, 10, 371, 31))
        self.remote_comb.setObjectName(_fromUtf8("remote_comb"))
        self.treeView_2 = QtGui.QTreeView(self.br_frame)
        self.treeView_2.setGeometry(QtCore.QRect(0, 50, 461, 241))
        self.treeView_2.setObjectName(_fromUtf8("treeView_2"))
        self.foot_frame = QtGui.QFrame(ccsds_dialog)
        self.foot_frame.setGeometry(QtCore.QRect(20, 390, 941, 201))
        self.foot_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.foot_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.foot_frame.setObjectName(_fromUtf8("foot_frame"))
        self.foot_h_frame = QtGui.QFrame(self.foot_frame)
        self.foot_h_frame.setGeometry(QtCore.QRect(0, 0, 941, 41))
        self.foot_h_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.foot_h_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.foot_h_frame.setObjectName(_fromUtf8("foot_h_frame"))
        self.log_label = QtGui.QLabel(self.foot_h_frame)
        self.log_label.setGeometry(QtCore.QRect(430, 0, 101, 41))
        self.log_label.setObjectName(_fromUtf8("log_label"))
        self.log_listView = QtGui.QListView(self.foot_frame)
        self.log_listView.setGeometry(QtCore.QRect(0, 40, 941, 192))
        self.log_listView.setObjectName(_fromUtf8("log_listView"))

        self.retranslateUi(ccsds_dialog)
        QtCore.QMetaObject.connectSlotsByName(ccsds_dialog)
        ccsds_dialog.setTabOrder(self.host_edit, self.port_edit)
        ccsds_dialog.setTabOrder(self.port_edit, self.user_edit)
        ccsds_dialog.setTabOrder(self.user_edit, self.pwd_edit)
        ccsds_dialog.setTabOrder(self.pwd_edit, self.qc_comb)
        ccsds_dialog.setTabOrder(self.qc_comb, self.qc_btn)
        ccsds_dialog.setTabOrder(self.qc_btn, self.local_treeView)
        ccsds_dialog.setTabOrder(self.local_treeView, self.treeView_2)
        ccsds_dialog.setTabOrder(self.treeView_2, self.log_listView)
        ccsds_dialog.setTabOrder(self.log_listView, self.local_comb)
        ccsds_dialog.setTabOrder(self.local_comb, self.remote_comb)

    def retranslateUi(self, ccsds_dialog):
        ccsds_dialog.setWindowTitle(_translate("ccsds_dialog", "WebDAV Client for CCSDS", None))
        self.qc_comb.setItemText(0, _translate("ccsds_dialog", "127.0.0.1", None))
        self.qc_comb.setItemText(1, _translate("ccsds_dialog", "192.168.1.1", None))
        self.port_label.setText(_translate("ccsds_dialog", "Port:", None))
        self.user_label.setText(_translate("ccsds_dialog", "User:", None))
        self.host_label.setText(_translate("ccsds_dialog", "Host:", None))
        self.pwd_label.setText(_translate("ccsds_dialog", "Password:", None))
        self.qc_btn.setText(_translate("ccsds_dialog", "Quick Connected", None))
        self.local_label.setText(_translate("ccsds_dialog", "Local:", None))
        self.remote_label.setText(_translate("ccsds_dialog", "Remote:", None))
        self.log_label.setText(_translate("ccsds_dialog", "  Event Log", None))

