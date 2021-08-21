from PyQt4 import QtCore, QtGui
import sqlite3
from main import Ui_MainWindow1 as Ui_HomePage
from PyQt4.QtGui import *
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

class Ui_Dialog(object):
    
    def UserHomeCheck(self):
        self.userHomeWindow=QtGui.QMainWindow()
        self.ui=Ui_HomePage()
        self.ui.setupUii(self.userHomeWindow)
        self.userHomeWindow.show()

           
    def loginCheck(self):
        username1=self.uname_lineEdit.text()
        username =str(username1)
        password1=self.pass_lineEdit.text()
        password = str(password1)
        print("password is:"+password)
        connection=sqlite3.connect("multiD.db")
        s="select *from userdetails where username='"+username+"' and password='"+password+"'"
        print("query is:"+s)
        result=connection.execute(s)
        if(len(result.fetchall())>0):
         print("user found!")
         self.UserHomeCheck()

        else:
         print("user not fount!")
         self.showmsg()
    
    def signupCheck(self):
        self.signUpShow()
        print("Signup button clicked !")

    def showmsg(self):
        self.showdialog1()

    def showdialog1(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Login failed")
        msg.setInformativeText("Please enter correct details ")
        msg.setWindowTitle("Status")
        # msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        retval = msg.exec_()
        print
        "value of pressed message box button:", retval

    def setinUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1200, 800)
        Dialog.setStyleSheet(_fromUtf8("background-image: url(bg1.jpg); border: 2px solid blue"))
        self.u_user_label = QtGui.QLabel(Dialog)
        self.u_user_label.setGeometry(QtCore.QRect(400, 150, 91, 31))
        self.u_user_label.setObjectName(_fromUtf8("u_user_label"))
        self.pass_label = QtGui.QLabel(Dialog)
        self.pass_label.setGeometry(QtCore.QRect(400, 190, 81, 31))
        self.pass_label.setObjectName(_fromUtf8("pass_label"))
       
        
        self.uname_lineEdit = QtGui.QLineEdit(Dialog)
        self.uname_lineEdit.setGeometry(QtCore.QRect(510, 149, 201, 31))
        self.uname_lineEdit.setText(_fromUtf8(""))
        self.uname_lineEdit.setObjectName(_fromUtf8("uname_lineEdit"))
       
        
        self.pass_lineEdit = QtGui.QLineEdit(Dialog)
        self.pass_lineEdit.setGeometry(QtCore.QRect(510, 190, 201, 31))
        self.pass_lineEdit.setObjectName(_fromUtf8("pass_lineEdit"))
        self.pass_lineEdit.setEchoMode(QtGui.QLineEdit.Password)
        
        
        self.login_btn = QtGui.QPushButton(Dialog)
        self.login_btn.setGeometry(QtCore.QRect(510, 250, 201, 31))
        self.login_btn.setObjectName(_fromUtf8("login_btn"))
       #####################Button Event####################################
        self.login_btn.clicked.connect(self.loginCheck)
        ####################################################################

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "LOGIN FORM", None))
        self.u_user_label.setText(_translate("Dialog", "NAME", None))
        self.pass_label.setText(_translate("Dialog", "PASSWORD", None))
        self.login_btn.setText(_translate("Dialog", "LOGIN TO SYSTEM", None))

        
    def quit(self):
        print ('Process end')
        print ('******End******')
        quit()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setinUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

