#!/usr/bin/python2.7
from masterMind import *

def main():
    app = QtGui.QApplication(sys.argv)
    ex = gui()
    ex.show()
    sys.exit(app.exec_())

main()
