# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_hw_pin_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HardwareWalletPinDlg(object):
    def setupUi(self, HardwareWalletPinDlg):
        HardwareWalletPinDlg.setObjectName("HardwareWalletPinDlg")
        HardwareWalletPinDlg.resize(172, 275)
        HardwareWalletPinDlg.setMinimumSize(QtCore.QSize(0, 0))
        HardwareWalletPinDlg.setMaximumSize(QtCore.QSize(100000, 10000))
        HardwareWalletPinDlg.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(HardwareWalletPinDlg)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lblMessage = QtWidgets.QLabel(HardwareWalletPinDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblMessage.sizePolicy().hasHeightForWidth())
        self.lblMessage.setSizePolicy(sizePolicy)
        self.lblMessage.setObjectName("lblMessage")
        self.horizontalLayout_4.addWidget(self.lblMessage)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.wdgPinButtons = QtWidgets.QWidget(HardwareWalletPinDlg)
        self.wdgPinButtons.setObjectName("wdgPinButtons")
        self.layPinButtons = QtWidgets.QHBoxLayout(self.wdgPinButtons)
        self.layPinButtons.setContentsMargins(1, 0, 0, 0)
        self.layPinButtons.setSpacing(0)
        self.layPinButtons.setObjectName("layPinButtons")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.btnPin1 = QtWidgets.QPushButton(self.wdgPinButtons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPin1.sizePolicy().hasHeightForWidth())
        self.btnPin1.setSizePolicy(sizePolicy)
        self.btnPin1.setMinimumSize(QtCore.QSize(60, 60))
        self.btnPin1.setMaximumSize(QtCore.QSize(60, 60))
        self.btnPin1.setAutoDefault(False)
        self.btnPin1.setObjectName("btnPin1")
        self.gridLayout.addWidget(self.btnPin1, 2, 0, 1, 1)
        self.btnPin5 = QtWidgets.QPushButton(self.wdgPinButtons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPin5.sizePolicy().hasHeightForWidth())
        self.btnPin5.setSizePolicy(sizePolicy)
        self.btnPin5.setMinimumSize(QtCore.QSize(60, 60))
        self.btnPin5.setMaximumSize(QtCore.QSize(60, 60))
        self.btnPin5.setAutoDefault(False)
        self.btnPin5.setObjectName("btnPin5")
        self.gridLayout.addWidget(self.btnPin5, 1, 1, 1, 1)
        self.btnPin3 = QtWidgets.QPushButton(self.wdgPinButtons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPin3.sizePolicy().hasHeightForWidth())
        self.btnPin3.setSizePolicy(sizePolicy)
        self.btnPin3.setMinimumSize(QtCore.QSize(60, 60))
        self.btnPin3.setMaximumSize(QtCore.QSize(60, 60))
        self.btnPin3.setAutoDefault(False)
        self.btnPin3.setObjectName("btnPin3")
        self.gridLayout.addWidget(self.btnPin3, 2, 2, 1, 1)
        self.btnPin4 = QtWidgets.QPushButton(self.wdgPinButtons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPin4.sizePolicy().hasHeightForWidth())
        self.btnPin4.setSizePolicy(sizePolicy)
        self.btnPin4.setMinimumSize(QtCore.QSize(60, 60))
        self.btnPin4.setMaximumSize(QtCore.QSize(60, 60))
        self.btnPin4.setAutoDefault(False)
        self.btnPin4.setObjectName("btnPin4")
        self.gridLayout.addWidget(self.btnPin4, 1, 0, 1, 1)
        self.btnPin9 = QtWidgets.QPushButton(self.wdgPinButtons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPin9.sizePolicy().hasHeightForWidth())
        self.btnPin9.setSizePolicy(sizePolicy)
        self.btnPin9.setMinimumSize(QtCore.QSize(60, 60))
        self.btnPin9.setMaximumSize(QtCore.QSize(60, 60))
        self.btnPin9.setAutoDefault(False)
        self.btnPin9.setObjectName("btnPin9")
        self.gridLayout.addWidget(self.btnPin9, 0, 2, 1, 1)
        self.btnPin8 = QtWidgets.QPushButton(self.wdgPinButtons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPin8.sizePolicy().hasHeightForWidth())
        self.btnPin8.setSizePolicy(sizePolicy)
        self.btnPin8.setMinimumSize(QtCore.QSize(60, 60))
        self.btnPin8.setMaximumSize(QtCore.QSize(60, 60))
        self.btnPin8.setAutoDefault(False)
        self.btnPin8.setFlat(False)
        self.btnPin8.setObjectName("btnPin8")
        self.gridLayout.addWidget(self.btnPin8, 0, 1, 1, 1)
        self.btnPin7 = QtWidgets.QPushButton(self.wdgPinButtons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPin7.sizePolicy().hasHeightForWidth())
        self.btnPin7.setSizePolicy(sizePolicy)
        self.btnPin7.setMinimumSize(QtCore.QSize(60, 60))
        self.btnPin7.setMaximumSize(QtCore.QSize(60, 60))
        self.btnPin7.setAutoDefault(False)
        self.btnPin7.setFlat(False)
        self.btnPin7.setObjectName("btnPin7")
        self.gridLayout.addWidget(self.btnPin7, 0, 0, 1, 1)
        self.btnPin6 = QtWidgets.QPushButton(self.wdgPinButtons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPin6.sizePolicy().hasHeightForWidth())
        self.btnPin6.setSizePolicy(sizePolicy)
        self.btnPin6.setMinimumSize(QtCore.QSize(60, 60))
        self.btnPin6.setMaximumSize(QtCore.QSize(60, 60))
        self.btnPin6.setAutoDefault(False)
        self.btnPin6.setObjectName("btnPin6")
        self.gridLayout.addWidget(self.btnPin6, 1, 2, 1, 1)
        self.btnPin2 = QtWidgets.QPushButton(self.wdgPinButtons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPin2.sizePolicy().hasHeightForWidth())
        self.btnPin2.setSizePolicy(sizePolicy)
        self.btnPin2.setMinimumSize(QtCore.QSize(60, 60))
        self.btnPin2.setMaximumSize(QtCore.QSize(60, 60))
        self.btnPin2.setAutoDefault(False)
        self.btnPin2.setObjectName("btnPin2")
        self.gridLayout.addWidget(self.btnPin2, 2, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 4, 0, -1)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.edtPin = QtWidgets.QLineEdit(self.wdgPinButtons)
        self.edtPin.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtPin.sizePolicy().hasHeightForWidth())
        self.edtPin.setSizePolicy(sizePolicy)
        self.edtPin.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.edtPin.setFont(font)
        self.edtPin.setFrame(True)
        self.edtPin.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edtPin.setObjectName("edtPin")
        self.horizontalLayout.addWidget(self.edtPin)
        self.btnDelete = QtWidgets.QPushButton(self.wdgPinButtons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDelete.sizePolicy().hasHeightForWidth())
        self.btnDelete.setSizePolicy(sizePolicy)
        self.btnDelete.setMinimumSize(QtCore.QSize(32, 26))
        self.btnDelete.setText("")
        self.btnDelete.setAutoDefault(False)
        self.btnDelete.setObjectName("btnDelete")
        self.horizontalLayout.addWidget(self.btnDelete)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.layPinButtons.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layPinButtons.addItem(spacerItem)
        self.verticalLayout.addWidget(self.wdgPinButtons)
        spacerItem1 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 4, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.btnEnterPin = QtWidgets.QPushButton(HardwareWalletPinDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnEnterPin.sizePolicy().hasHeightForWidth())
        self.btnEnterPin.setSizePolicy(sizePolicy)
        self.btnEnterPin.setMinimumSize(QtCore.QSize(120, 0))
        self.btnEnterPin.setMaximumSize(QtCore.QSize(100000, 16777215))
        self.btnEnterPin.setObjectName("btnEnterPin")
        self.horizontalLayout_3.addWidget(self.btnEnterPin)
        spacerItem3 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(HardwareWalletPinDlg)
        QtCore.QMetaObject.connectSlotsByName(HardwareWalletPinDlg)

    def retranslateUi(self, HardwareWalletPinDlg):
        _translate = QtCore.QCoreApplication.translate
        HardwareWalletPinDlg.setWindowTitle(_translate("HardwareWalletPinDlg", "Dialog"))
        self.lblMessage.setText(_translate("HardwareWalletPinDlg", "Enter PIN"))
        self.btnPin1.setText(_translate("HardwareWalletPinDlg", "*"))
        self.btnPin5.setText(_translate("HardwareWalletPinDlg", "*"))
        self.btnPin3.setText(_translate("HardwareWalletPinDlg", "*"))
        self.btnPin4.setText(_translate("HardwareWalletPinDlg", "*"))
        self.btnPin9.setText(_translate("HardwareWalletPinDlg", "*"))
        self.btnPin8.setText(_translate("HardwareWalletPinDlg", "*"))
        self.btnPin7.setText(_translate("HardwareWalletPinDlg", "*"))
        self.btnPin6.setText(_translate("HardwareWalletPinDlg", "*"))
        self.btnPin2.setText(_translate("HardwareWalletPinDlg", "*"))
        self.btnDelete.setToolTip(_translate("HardwareWalletPinDlg", "Delete last character"))
        self.btnEnterPin.setText(_translate("HardwareWalletPinDlg", "Enter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HardwareWalletPinDlg = QtWidgets.QDialog()
    ui = Ui_HardwareWalletPinDlg()
    ui.setupUi(HardwareWalletPinDlg)
    HardwareWalletPinDlg.show()
    sys.exit(app.exec_())

