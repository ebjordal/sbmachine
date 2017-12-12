import sys
'''Qt bindings for core Qt functionalities (non-GUI)'''
from PyQt5 import QtCore
import PyQt5
from PyQt5.QtWidgets import QMainWindow,QApplication,QDialog, QFileDialog,QVBoxLayout
'''Subscripts'''

from mainwindow import Ui_MainWindow 		#import the MainWindow widget from the converted files from .ui to .py
from pincode import Ui_pincode
from userlogin_manual import Ui_userlogin_manual
import ButtonPopup


'''Setup of the GUI with associated functions for buttons'''
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent) 	#initialization of the superclass
        self.setupUi(self) 	#setup the GUI --> function generated by pyuic4/pyuic5 depending on QT version
        self.loginout_b.clicked.connect(self.login)

    def login(self):
        dmw.hide()
        dmf.show()
        dmf.user_email.clear()


class UserLoginM(QDialog, Ui_userlogin_manual):
    def __init__(self, parent = None):
        super(UserLoginM, self).__init__(parent)
        self.setupUi(self)
        self.user_email.clear()
        self.pushButton_Ok.clicked.connect(self.submit)
        self.pushButton_cancel.clicked.connect(self.cancel)
        self.pushButton_del.clicked.connect(self.LoginPushDel)
        self.pushButton_a.clicked.connect(self.LoginPushA)
        self.pushButton_b.clicked.connect(self.LoginPushB)
        self.pushButton_c.clicked.connect(self.LoginPushC)
        self.pushButton_d.clicked.connect(self.LoginPushD)
        self.pushButton_e.clicked.connect(self.LoginPushE)
        self.pushButton_f.clicked.connect(self.LoginPushF)
        self.pushButton_g.clicked.connect(self.LoginPushG)
        self.pushButton_h.clicked.connect(self.LoginPushH)
        self.pushButton_i.clicked.connect(self.LoginPushI)
        self.pushButton_j.clicked.connect(self.LoginPushJ)
        self.pushButton_k.clicked.connect(self.LoginPushK)
        self.pushButton_l.clicked.connect(self.LoginPushL)
        self.pushButton_m.clicked.connect(self.LoginPushM)
        self.pushButton_n.clicked.connect(self.LoginPushN)
        self.pushButton_o.clicked.connect(self.LoginPushO)
        self.pushButton_p.clicked.connect(self.LoginPushP)
        self.pushButton_q.clicked.connect(self.LoginPushQ)
        self.pushButton_r.clicked.connect(self.LoginPushR)
        self.pushButton_s.clicked.connect(self.LoginPushS)
        self.pushButton_t.clicked.connect(self.LoginPushT)
        self.pushButton_u.clicked.connect(self.LoginPushU)
        self.pushButton_v.clicked.connect(self.LoginPushV)
        self.pushButton_w.clicked.connect(self.LoginPushW)
        self.pushButton_x.clicked.connect(self.LoginPushX)
        self.pushButton_y.clicked.connect(self.LoginPushY)
        self.pushButton_z.clicked.connect(self.LoginPushZ)
        self.pushButton_dot.clicked.connect(self.LoginPushDot)
        self.pushButton_dash.clicked.connect(self.LoginPushDash)
        self.pushButton_alfa.clicked.connect(self.LoginPushAlpha)
        self.pushButton_one.clicked.connect(self.LoginPushOne)
        self.pushButton_two.clicked.connect(self.LoginPushTwo)
        self.pushButton_three.clicked.connect(self.LoginPushThree)
        self.pushButton_four.clicked.connect(self.LoginPushFour)
        self.pushButton_five.clicked.connect(self.LoginPushFive)
        self.pushButton_six.clicked.connect(self.LoginPushSix)
        self.pushButton_seven.clicked.connect(self.LoginPushSeven)
        self.pushButton_eight.clicked.connect(self.LoginPushEight)
        self.pushButton_nine.clicked.connect(self.LoginPushNine)
        self.pushButton_zero.clicked.connect(self.LoginPushZero)

    def submit(self):
        dmp.pincode_entry.clear()
        dmf.hide()
        dmp.show()

    def cancel(self):
        dmf.user_email.clear()
        dmf.hide()
        dmw.show()


    def LoginPushA(self):
        self.user_email.insert("a")
    def LoginPushB(self):
        self.user_email.insert("b")
    def LoginPushC(self):
        self.user_email.insert("c")
    def LoginPushD(self):
        self.user_email.insert("d")
    def LoginPushE(self):
        self.user_email.insert("e")
    def LoginPushF(self):
        self.user_email.insert("f")
    def LoginPushG(self):
        self.user_email.insert("g")
    def LoginPushH(self):
        self.user_email.insert("h")
    def LoginPushI(self):
        self.user_email.insert("i")
    def LoginPushJ(self):
        self.user_email.insert("j")
    def LoginPushK(self):
        self.user_email.insert("k")
    def LoginPushL(self):
        self.user_email.insert("l")
    def LoginPushM(self):
        self.user_email.insert("m")
    def LoginPushN(self):
        self.user_email.insert("n")
    def LoginPushO(self):
        self.user_email.insert("o")
    def LoginPushP(self):
        self.user_email.insert("p")
    def LoginPushQ(self):
        self.user_email.insert("q")
    def LoginPushR(self):
        self.user_email.insert("r")
    def LoginPushS(self):
        self.user_email.insert("s")
    def LoginPushT(self):
        self.user_email.insert("t")
    def LoginPushU(self):
        self.user_email.insert("u")
    def LoginPushV(self):
        self.user_email.insert("v")
    def LoginPushW(self):
        self.user_email.insert("w")
    def LoginPushX(self):
        self.user_email.insert("x")
    def LoginPushY(self):
        self.user_email.insert("y")
    def LoginPushZ(self):
        self.user_email.insert("z")
    def LoginPushDot(self):
        self.user_email.insert(".")
    def LoginPushDash(self):
        self.user_email.insert("-")
    def LoginPushAlpha(self):
        self.user_email.insert("@")
    def LoginPushOne(self):
        self.user_email.insert("1")
    def LoginPushTwo(self):
        self.user_email.insert("2")
    def LoginPushThree(self):
        self.user_email.insert("3")
    def LoginPushFour(self):
        self.user_email.insert("4")
    def LoginPushFive(self):
        self.user_email.insert("5")
    def LoginPushSix(self):
        self.user_email.insert("6")
    def LoginPushSeven(self):
        self.user_email.insert("7")
    def LoginPushEight(self):
        self.user_email.insert("8")
    def LoginPushNine(self):
        self.user_email.insert("9")
    def LoginPushZero(self):
        self.user_email.insert("0")
    def LoginPushDel(self):
        self.user_email.backspace()


class PinCode(QDialog,Ui_pincode):
    def __init__(self, parent = None):
        super(PinCode, self).__init__(parent)
        self.setupUi(self)
        self.pushbutton_ok.clicked.connect(self.submit)
        self.pushButton_cancel.clicked.connect(self.cancel)
        self.pushButton_one.clicked.connect(self.PinButtonOne)
        self.pushButton_two.clicked.connect(self.PinButtonTwo)
        self.pushButton_three.clicked.connect(self.PinButtonThree)
        self.pushButton_four.clicked.connect(self.PinButtonFour)
        self.pushButton_five.clicked.connect(self.PinButtonFive)
        self.pushButton_six.clicked.connect(self.PinButtonSix)
        self.pushButton_seven.clicked.connect(self.PinButtonSeven)
        self.pushButton_eight.clicked.connect(self.PinButtonEight)
        self.pushButton_nine.clicked.connect(self.PinButtonNine)
        self.pushButton_zero.clicked.connect(self.PinButtonZero)

    def PinButtonOne(self):
        self.pincode_entry.insert("1")
    def PinButtonTwo(self):
        self.pincode_entry.insert("2")
    def PinButtonThree(self):
        self.pincode_entry.insert("3")
    def PinButtonFour(self):
        self.pincode_entry.insert("4")
    def PinButtonFive(self):
        self.pincode_entry.insert("5")
    def PinButtonSix(self):
        self.pincode_entry.insert("6")
    def PinButtonSeven(self):
        self.pincode_entry.insert("7")
    def PinButtonEight(self):
        self.pincode_entry.insert("8")
    def PinButtonNine(self):
        self.pincode_entry.insert("9")
    def PinButtonZero(self):
        self.pincode_entry.insert("0")



    def submit(self):
        print(self.pincode_entry.text())
        print("Hello")
        dmp.hide()
        dmw.show()

    def cancel(self):
        dmp.hide()
        dmw.show()



app = QApplication(sys.argv) # create the GUI application
dmw = MainWindow() # instantiate the main window
dmf = UserLoginM()
dmp = PinCode()
dmw.show() # show it
sys.exit(app.exec_())