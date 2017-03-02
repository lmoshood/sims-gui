# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cart.ui'
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

class Ui_cartWindow(object):
    def setupUi(self, cartWindow):
        cartWindow.setObjectName(_fromUtf8("cartWindow"))
        cartWindow.resize(1094, 795)
        cartWindow.setStyleSheet(_fromUtf8("QPushButton {padding: 10px}\n"
"QWidget {background-color: white}\n"
"\\"))
        self.gridLayout_3 = QtGui.QGridLayout(cartWindow)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 4)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 3, 0, 1, 4)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.partName = QtGui.QLabel(cartWindow)
        self.partName.setStyleSheet(_fromUtf8("font: 20pt \"Noto Sans\";"))
        self.partName.setObjectName(_fromUtf8("partName"))
        self.gridLayout.addWidget(self.partName, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.label_12 = QtGui.QLabel(cartWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 6, 0, 1, 1)
        self.removeFromCartButton = QtGui.QPushButton(cartWindow)
        self.removeFromCartButton.setObjectName(_fromUtf8("removeFromCartButton"))
        self.gridLayout.addWidget(self.removeFromCartButton, 8, 0, 1, 2)
        self.label_3 = QtGui.QLabel(cartWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.partID = QtGui.QLabel(cartWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.partID.setFont(font)
        self.partID.setObjectName(_fromUtf8("partID"))
        self.gridLayout.addWidget(self.partID, 3, 1, 1, 1)
        self.label_5 = QtGui.QLabel(cartWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.partShelf = QtGui.QLabel(cartWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.partShelf.setFont(font)
        self.partShelf.setObjectName(_fromUtf8("partShelf"))
        self.gridLayout.addWidget(self.partShelf, 4, 1, 1, 1)
        self.partQty = QtGui.QLabel(cartWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.partQty.setFont(font)
        self.partQty.setObjectName(_fromUtf8("partQty"))
        self.gridLayout.addWidget(self.partQty, 6, 1, 1, 1)
        self.label_4 = QtGui.QLabel(cartWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.partBox = QtGui.QLabel(cartWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.partBox.setFont(font)
        self.partBox.setObjectName(_fromUtf8("partBox"))
        self.gridLayout.addWidget(self.partBox, 5, 1, 1, 1)
        self.partCategory = QtGui.QLabel(cartWindow)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.partCategory.setFont(font)
        self.partCategory.setStyleSheet(_fromUtf8("font: italic 16pt \"Noto Sans\";"))
        self.partCategory.setObjectName(_fromUtf8("partCategory"))
        self.gridLayout.addWidget(self.partCategory, 1, 0, 1, 2, QtCore.Qt.AlignHCenter)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 7, 0, 1, 2)
        self.label = QtGui.QLabel(cartWindow)
        self.label.setMaximumSize(QtCore.QSize(130, 130))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("images/atmega328.jpg")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.openInventory = QtGui.QPushButton(cartWindow)
        self.openInventory.setObjectName(_fromUtf8("openInventory"))
        self.gridLayout.addWidget(self.openInventory, 9, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 3, 1, 1)
        self.label_2 = QtGui.QLabel(cartWindow)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans"))
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("font: 24pt \"Noto Sans\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 4, QtCore.Qt.AlignHCenter)
        self.buttonBox = QtGui.QDialogButtonBox(cartWindow)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_2.addWidget(self.buttonBox, 4, 0, 1, 4, QtCore.Qt.AlignHCenter)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 5, 0, 1, 4)
        self.listView = QtGui.QListView(cartWindow)
        self.listView.setMinimumSize(QtCore.QSize(500, 0))
        self.listView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.gridLayout_2.addWidget(self.listView, 2, 1, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 2, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 0, 2, 1, 1)

        self.retranslateUi(cartWindow)
        QtCore.QMetaObject.connectSlotsByName(cartWindow)

    def retranslateUi(self, cartWindow):
        cartWindow.setWindowTitle(_translate("cartWindow", "Form", None))
        self.partName.setText(_translate("cartWindow", "ATMega32U4", None))
        self.label_12.setText(_translate("cartWindow", "Quantity", None))
        self.removeFromCartButton.setText(_translate("cartWindow", "Remove From Cart", None))
        self.label_3.setText(_translate("cartWindow", "ID", None))
        self.partID.setText(_translate("cartWindow", "035", None))
        self.label_5.setText(_translate("cartWindow", "Box", None))
        self.partShelf.setText(_translate("cartWindow", "3", None))
        self.partQty.setText(_translate("cartWindow", "2", None))
        self.label_4.setText(_translate("cartWindow", "Shelf", None))
        self.partBox.setText(_translate("cartWindow", "5", None))
        self.partCategory.setText(_translate("cartWindow", "<html><head/><body><p align=\"center\"><span style=\" font-style:italic;\">Microcontroller</span></p></body></html>", None))
        self.openInventory.setText(_translate("cartWindow", "Inventory", None))
        self.label_2.setText(_translate("cartWindow", "Cart", None))

