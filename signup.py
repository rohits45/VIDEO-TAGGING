from PyQt4 import QtCore, QtGui
import sqlite3
from login import Ui_Dialog
from PyQt4.QtCore import QRegExp
from PyQt4.QtGui import QRegExpValidator
from tkinter.constants import ALL
from PyQt4.QtCore import QRegExp
from PyQt4.QtGui import QRegExpValidator
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import re
import sys

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


class Ui_signUp(object):

    def insertData(self):
        error = None
        username1 = self.uname_lineEdit.text()
        username = str(username1)
        email1 = self.email_lineEdit.text()
        if email1.find('@') == -1:
            error = True
            alrt = "please enter valid email"
            self.showdialog(alrt)
        else:
            email = str(email1)

        mob1 = self.mob_lineEdit.text()
        if len(mob1) != 10 or len(re.findall('\D', str(mob1), re.I)) > 0:
            error = True
            alrt = 'please enter valid number'
            self.showdialog(alrt)
        else:
            mob = str(mob1)
        password1 = self.password_lineEdit.text()
        password = str(password1)

        if not error:
            connection = sqlite3.connect("multiD.db")
            s = "insert into userdetails (username,email,mob,password) values('" + username + "','" + email + "','" + mob + "','" + password + "')"
            print("query is:-" + s)
            result = connection.execute(s)
            if result:
                s1 = "select * from userdetails"
                result = connection.execute(s1)
                print("Success  :: " + s1)
            connection.commit()
            connection.close()
            self.showmsg()

    def showmsg(self):
        self.showdialog1()

    def showdialog(self, alrt):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Registration Status")
        msg.setInformativeText(alrt)
        msg.setWindowTitle("Status")
        # msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        retval = msg.exec_()
        print
        "value of pressed message box button:", retval

    def showdialog1(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Registration Status")
        msg.setInformativeText("Registration successful")
        msg.setWindowTitle("Status")
        # msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        retval = msg.exec_()
        print
        "value of pressed message box button:", retval

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))

    def signInCheck(self):
        print("hello signin button")
        self.signInWindow = QtGui.QDialog()
        self.ui = Ui_Dialog()
        print("i'm in self signin")
        self.ui.setinUi(self.signInWindow)
        print("i'm in self setupUi method")
        self.signInWindow.show()
        print("i'm in self signin windows")

    def signInButton(self):
        self.signInCheck()

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1200, 800)
        Dialog.setStyleSheet(_fromUtf8("background-image: url(bg1.jpg); border: 2px solid orange"))
        # Dialog.setStyleSheet(_fromUtf8("border: 2px solid black"))

        #############################################################################

        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(500, 100, 110, 30))
        self.label.setObjectName(_fromUtf8("label"))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(500, 150, 110, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)

        self.label_M = QtGui.QLabel(Dialog)
        self.label_M.setGeometry(QtCore.QRect(500, 200, 110, 20))
        self.label_M.setObjectName(_fromUtf8("label_M"))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_M.setFont(font)

        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(500, 250, 110, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)

        #############################################################

        self.uname_lineEdit = QtGui.QLineEdit(Dialog)
        self.uname_lineEdit.setGeometry(QtCore.QRect(615, 100, 211, 27))
        self.uname_lineEdit.setObjectName(_fromUtf8("uname_lineEdit"))

        '''
        reg_ex = QRegExp("[0-9]*@.?[a-z]*/.?[a-z]")
        input_validator = QRegExpValidator(reg_ex, self.uname_lineEdit)
        self.uname_lineEdit.setValidator(input_validator)
        '''

        self.email_lineEdit = QtGui.QLineEdit(Dialog)
        self.email_lineEdit.setGeometry(QtCore.QRect(615, 150, 211, 27))
        self.email_lineEdit.setObjectName(_fromUtf8("email_lineEdit"))

        self.mob_lineEdit = QtGui.QLineEdit(Dialog)
        self.mob_lineEdit.setGeometry(QtCore.QRect(615, 200, 211, 27))
        self.mob_lineEdit.setObjectName(_fromUtf8("mob_lineEdit"))

        self.password_lineEdit = QtGui.QLineEdit(Dialog)
        self.password_lineEdit.setGeometry(QtCore.QRect(615, 250, 211, 27))
        self.password_lineEdit.setObjectName(_fromUtf8("password_lineEdit"))
        self.password_lineEdit.setEchoMode(QtGui.QLineEdit.Password)

        self.email_lineEdit.setStyleSheet("color: black")
        self.mob_lineEdit.setStyleSheet("color: black")

        self.signup_btn = QtGui.QPushButton(Dialog)
        self.signup_btn.setGeometry(QtCore.QRect(615, 300, 211, 27))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.signup_btn.setFont(font)
        self.signup_btn.setObjectName(_fromUtf8("signup_btn"))
        self.signup_btn.setStyleSheet("background-color: black")
        #########################EVENT##############
        self.signup_btn.clicked.connect(self.insertData)
        ############################################

        self.exit = QtGui.QPushButton(Dialog)
        self.exit.setGeometry(QtCore.QRect(615, 350, 211, 27))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.exit.setFont(font)
        self.exit.setObjectName(_fromUtf8("exit"))
        self.exit.setStyleSheet("background-color: black")
        #########################EVENT##############
        self.exit.clicked.connect(self.closeall)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def closeall(self):
        quit()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Registration Form", None))
        self.label.setText(_translate("Dialog", "NAME", None))
        self.label_2.setText(_translate("Dialog", "EMAIL", None))
        self.label_M.setText(_translate("Dialog", "MOBILE", None))
        self.label_3.setText(_translate("Dialog", "PASSWORD", None))
        self.signup_btn.setText(_translate("Dialog", "Click To Register", None))
        self.exit.setText(_translate("Dialog", "Click To Exit", None))


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_signUp()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())

