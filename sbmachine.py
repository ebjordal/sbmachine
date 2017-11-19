import sys
'''Qt bindings for core Qt functionalities (non-GUI)'''

from PyQt5 import QtWidgets

'''Subscripts'''
from mainwindow import *


if __name__="__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

