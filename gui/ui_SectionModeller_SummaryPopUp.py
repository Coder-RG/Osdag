# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'summary_popup.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import QMainWindow, QDialog, QFontDialog, QApplication, QFileDialog, QColorDialog,QDialogButtonBox
from PyQt5.QtWidgets import QMessageBox, qApp
from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_Dialog1(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(539, 595)
        Dialog.setInputMethodHints(QtCore.Qt.ImhNone)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_companyName = QtWidgets.QLabel(Dialog)
        self.lbl_companyName.setObjectName("lbl_companyName")
        self.gridLayout.addWidget(self.lbl_companyName, 0, 0, 1, 1)
        self.lineEdit_companyName = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_companyName.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_companyName.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_companyName.setObjectName("lineEdit_companyName")
        self.gridLayout.addWidget(self.lineEdit_companyName, 0, 1, 1, 1)
        self.lbl_comapnyLogo = QtWidgets.QLabel(Dialog)
        self.lbl_comapnyLogo.setObjectName("lbl_comapnyLogo")
        self.gridLayout.addWidget(self.lbl_comapnyLogo, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_browse = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_browse.sizePolicy().hasHeightForWidth())
        self.btn_browse.setSizePolicy(sizePolicy)
        self.btn_browse.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btn_browse.setObjectName("btn_browse")
        self.horizontalLayout.addWidget(self.btn_browse)
        self.lbl_browse = QtWidgets.QLabel(Dialog)
        self.lbl_browse.setMouseTracking(True)
        self.lbl_browse.setAcceptDrops(True)
        self.lbl_browse.setText("")
        self.lbl_browse.setObjectName("lbl_browse")
        self.horizontalLayout.addWidget(self.lbl_browse)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.lbl_groupName = QtWidgets.QLabel(Dialog)
        self.lbl_groupName.setObjectName("lbl_groupName")
        self.gridLayout.addWidget(self.lbl_groupName, 2, 0, 1, 1)
        self.lineEdit_groupName = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_groupName.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_groupName.setCursorPosition(0)
        self.lineEdit_groupName.setObjectName("lineEdit_groupName")
        self.gridLayout.addWidget(self.lineEdit_groupName, 2, 1, 1, 1)
        self.lbl_designer = QtWidgets.QLabel(Dialog)
        self.lbl_designer.setObjectName("lbl_designer")
        self.gridLayout.addWidget(self.lbl_designer, 3, 0, 1, 1)
        self.lineEdit_designer = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_designer.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_designer.setObjectName("lineEdit_designer")
        self.gridLayout.addWidget(self.lineEdit_designer, 3, 1, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.formLayout.setObjectName("formLayout")
        self.btn_useProfile = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_useProfile.sizePolicy().hasHeightForWidth())
        self.btn_useProfile.setSizePolicy(sizePolicy)
        self.btn_useProfile.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btn_useProfile.setObjectName("btn_useProfile")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.btn_useProfile)
        self.btn_saveProfile = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_saveProfile.sizePolicy().hasHeightForWidth())
        self.btn_saveProfile.setSizePolicy(sizePolicy)
        self.btn_saveProfile.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btn_saveProfile.setObjectName("btn_saveProfile")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.btn_saveProfile)
        self.gridLayout.addLayout(self.formLayout, 4, 1, 1, 1)
        self.lbl_projectTitle = QtWidgets.QLabel(Dialog)
        self.lbl_projectTitle.setObjectName("lbl_projectTitle")
        self.gridLayout.addWidget(self.lbl_projectTitle, 5, 0, 1, 1)
        self.lineEdit_projectTitle = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_projectTitle.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_projectTitle.setObjectName("lineEdit_projectTitle")
        self.gridLayout.addWidget(self.lineEdit_projectTitle, 5, 1, 1, 1)
        self.lbl_subtitle = QtWidgets.QLabel(Dialog)
        self.lbl_subtitle.setObjectName("lbl_subtitle")
        self.gridLayout.addWidget(self.lbl_subtitle, 6, 0, 1, 1)
        self.lineEdit_subtitle = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_subtitle.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_subtitle.setText("")
        self.lineEdit_subtitle.setObjectName("lineEdit_subtitle")
        self.gridLayout.addWidget(self.lineEdit_subtitle, 6, 1, 1, 1)
        self.lbl_jobNumber = QtWidgets.QLabel(Dialog)
        self.lbl_jobNumber.setObjectName("lbl_jobNumber")
        self.gridLayout.addWidget(self.lbl_jobNumber, 7, 0, 1, 1)
        self.lineEdit_jobNumber = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_jobNumber.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_jobNumber.setObjectName("lineEdit_jobNumber")
        self.gridLayout.addWidget(self.lineEdit_jobNumber, 7, 1, 1, 1)
        self.lbl_client = QtWidgets.QLabel(Dialog)
        self.lbl_client.setObjectName("lbl_client")
        self.gridLayout.addWidget(self.lbl_client, 8, 0, 1, 1)
        self.lineEdit_client = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_client.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_client.setObjectName("lineEdit_client")
        self.gridLayout.addWidget(self.lineEdit_client, 8, 1, 1, 1)
        self.lbl_addComment = QtWidgets.QLabel(Dialog)
        self.lbl_addComment.setObjectName("lbl_addComment")
        self.gridLayout.addWidget(self.lbl_addComment, 9, 0, 1, 1)
        self.txt_additionalComments = QtWidgets.QTextEdit(Dialog)
        self.txt_additionalComments.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.txt_additionalComments.setStyleSheet("  QTextCursor textCursor;\n"
"  textCursor.setPosistion(0, QTextCursor::MoveAnchor); \n"
"  textedit->setTextCursor( textCursor );")
        self.txt_additionalComments.setInputMethodHints(QtCore.Qt.ImhNone)
        self.txt_additionalComments.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.txt_additionalComments.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.txt_additionalComments.setTabChangesFocus(False)
        self.txt_additionalComments.setReadOnly(False)
        self.txt_additionalComments.setObjectName("txt_additionalComments")
        self.gridLayout.addWidget(self.txt_additionalComments, 9, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 10, 1, 1, 1)

        self.retranslateUi(Dialog)

        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.accepted.connect(lambda:self.save_inputSummary(Dialog))
        self.buttonBox.rejected.connect(Dialog.reject)
        self.btn_browse.clicked.connect(self.lbl_browse.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit_companyName, self.btn_browse)
        Dialog.setTabOrder(self.btn_browse, self.lineEdit_groupName)
        Dialog.setTabOrder(self.lineEdit_groupName, self.lineEdit_designer)
        Dialog.setTabOrder(self.lineEdit_designer, self.btn_useProfile)
        Dialog.setTabOrder(self.btn_useProfile, self.btn_saveProfile)
        Dialog.setTabOrder(self.btn_saveProfile, self.lineEdit_projectTitle)
        Dialog.setTabOrder(self.lineEdit_projectTitle, self.lineEdit_subtitle)
        Dialog.setTabOrder(self.lineEdit_subtitle, self.lineEdit_jobNumber)
        Dialog.setTabOrder(self.lineEdit_jobNumber, self.lineEdit_client)
        Dialog.setTabOrder(self.lineEdit_client, self.txt_additionalComments)
        Dialog.setTabOrder(self.txt_additionalComments, self.buttonBox)
        self.input_summary={}

    def save_inputSummary(self,Dialog):
        self.input_summary = self.getPopUpInputs()  # getting all inputs entered by user in PopUp dialog box.
        file_type = "PDF (*.pdf)"
        filename = QFileDialog.getSaveFileName(QFileDialog(), "Save File As", os.path.join(str(' '), "untitled.pdf"), file_type)
        fname_no_ext = filename[0].split(".")[0]
        self.input_summary['filename'] = fname_no_ext
        Dialog.close()



    def getPopUpInputs(self):
        input_summary = {}
        input_summary["ProfileSummary"] = {}
        input_summary["ProfileSummary"]["CompanyName"] = str(self.lineEdit_companyName.text())
        input_summary["ProfileSummary"]["CompanyLogo"] = str(self.lbl_browse.text())
        input_summary["ProfileSummary"]["Group/TeamName"] = str(self.lineEdit_groupName.text())
        input_summary["ProfileSummary"]["Designer"] = str(self.lineEdit_designer.text())

        input_summary["ProjectTitle"] = str(self.lineEdit_projectTitle.text())
        input_summary["Subtitle"] = str(self.lineEdit_subtitle.text())
        input_summary["JobNumber"] = str(self.lineEdit_jobNumber.text())
        input_summary["AdditionalComments"] = str(self.txt_additionalComments.toPlainText())
        input_summary["Client"] = str(self.lineEdit_client.text())

        return input_summary

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lbl_companyName.setText(_translate("Dialog", "Company Name :"))
        self.lbl_comapnyLogo.setText(_translate("Dialog", "Company Logo :"))
        self.btn_browse.setText(_translate("Dialog", "Browse..."))
        self.lbl_groupName.setText(_translate("Dialog", "Group/Team Name :"))
        self.lbl_designer.setText(_translate("Dialog", "Designer :"))
        self.btn_useProfile.setText(_translate("Dialog", "Use Profile"))
        self.btn_saveProfile.setText(_translate("Dialog", "Save Profile"))
        self.lbl_projectTitle.setText(_translate("Dialog", "Project Title :"))
        self.lbl_subtitle.setText(_translate("Dialog", "Subtitle :"))
        self.lineEdit_subtitle.setPlaceholderText(_translate("Dialog", "(Optional)"))
        self.lbl_jobNumber.setText(_translate("Dialog", "Job Number :"))
        self.lbl_client.setText(_translate("Dialog", "Client :"))
        self.lbl_addComment.setText(_translate("Dialog", "Additional Comments :"))
        self.txt_additionalComments.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.5pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt;\"><br /></p></body></html>"))

