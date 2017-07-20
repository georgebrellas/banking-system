# -*- coding: utf-8 -*-
# Created by: PyQt5 UI code generator 5.9
# Banking System UI
# By George Brellas

from PyQt5 import QtCore, QtGui, QtWidgets
from Bank import *


    
class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(391, 316)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main.sizePolicy().hasHeightForWidth())
        main.setSizePolicy(sizePolicy)
        main.setMinimumSize(QtCore.QSize(391, 316))
        main.setMaximumSize(QtCore.QSize(391, 316))
        main.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        main.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(main)
        self.centralwidget.setObjectName("centralwidget")
        self.bLogin = QtWidgets.QPushButton(self.centralwidget)
        self.bLogin.setGeometry(QtCore.QRect(130, 230, 121, 51))
        self.bLogin.setObjectName("bLogin")
        self.accLabel = QtWidgets.QLabel(self.centralwidget)
        self.accLabel.setGeometry(QtCore.QRect(90, 10, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.accLabel.setFont(font)
        self.accLabel.setObjectName("accLabel")
        self.numEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.numEntry.setGeometry(QtCore.QRect(100, 60, 191, 31))
        self.numEntry.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.numEntry.setMouseTracking(True)
        self.numEntry.setText("")
        self.numEntry.setReadOnly(False)
        self.numEntry.setObjectName("numEntry")
        self.pinEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.pinEntry.setGeometry(QtCore.QRect(150, 170, 81, 31))
        self.pinEntry.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pinEntry.setMouseTracking(True)
        self.pinEntry.setText("")
        self.pinEntry.setMaxLength(4)
        self.pinEntry.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pinEntry.setReadOnly(False)
        self.pinEntry.setObjectName("pinEntry")
        self.pinLabel = QtWidgets.QLabel(self.centralwidget)
        self.pinLabel.setGeometry(QtCore.QRect(170, 120, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pinLabel.setFont(font)
        self.pinLabel.setObjectName("pinLabel")
        main.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(main)
        self.statusbar.setObjectName("statusbar")
        main.setStatusBar(self.statusbar)

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "Banking System v2.3"))
        self.bLogin.setText(_translate("main", "Login"))
        self.accLabel.setText(_translate("main", "Account Number"))
        self.pinLabel.setText(_translate("main", "PIN"))
        self.bLogin.clicked.connect(self.uiLogin)
        
    def uiLogin():
        Num = self.numEntry.text()
        Pin = self.pinEntry.text()
        print(Num,Pin)
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QMainWindow()
    ui = Ui_main()
    ui.setupUi(main)
    main.show()
    sys.exit(app.exec_())



