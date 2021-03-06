# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created: Sat Sep 15 19:03:24 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

__author__ = "Ricardo M. Ferraz Leal"
__copyright__ = "Copyright 2012, European Synchrotron Radiation Facility"
__credits__ = ["Ricardo M. Ferraz Leal", "Alexander N. Popov", "Gleb P. Bourenkov",
                    "Sean McSweeney", "Rita Giordano"]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Ricardo M. Ferraz Leal"
__email__ = "ricardo.leal@esrf.fr"
__status__ = "Beta"

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(801, 711)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButtonRefDSPattern = QtGui.QPushButton(self.centralwidget)
        self.pushButtonRefDSPattern.setGeometry(QtCore.QRect(190, 60, 121, 27))
        self.pushButtonRefDSPattern.setObjectName(_fromUtf8("pushButtonRefDSPattern"))
        self.lineEditRefDsPattern = QtGui.QLineEdit(self.centralwidget)
        self.lineEditRefDsPattern.setGeometry(QtCore.QRect(10, 60, 171, 25))
        self.lineEditRefDsPattern.setObjectName(_fromUtf8("lineEditRefDsPattern"))
        self.comboBoxRefDS = QtGui.QComboBox(self.centralwidget)
        self.comboBoxRefDS.setGeometry(QtCore.QRect(320, 60, 351, 25))
        self.comboBoxRefDS.setObjectName(_fromUtf8("comboBoxRefDS"))
        self.lineEditRemainingDSsPattern = QtGui.QLineEdit(self.centralwidget)
        self.lineEditRemainingDSsPattern.setGeometry(QtCore.QRect(600, 180, 191, 25))
        self.lineEditRemainingDSsPattern.setObjectName(_fromUtf8("lineEditRemainingDSsPattern"))
        self.pushButtonRemainingDSsPattern = QtGui.QPushButton(self.centralwidget)
        self.pushButtonRemainingDSsPattern.setGeometry(QtCore.QRect(600, 210, 191, 27))
        self.pushButtonRemainingDSsPattern.setObjectName(_fromUtf8("pushButtonRemainingDSsPattern"))
        self.table = QtGui.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(10, 160, 581, 231))
        self.table.setObjectName(_fromUtf8("table"))
        self.table.setColumnCount(3)
        self.table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.table.setHorizontalHeaderItem(2, item)
        self.pushButtonCellDetails = QtGui.QPushButton(self.centralwidget)
        self.pushButtonCellDetails.setGeometry(QtCore.QRect(680, 60, 111, 27))
        self.pushButtonCellDetails.setObjectName(_fromUtf8("pushButtonCellDetails"))
        self.lineEditUnitCell = QtGui.QLineEdit(self.centralwidget)
        self.lineEditUnitCell.setGeometry(QtCore.QRect(110, 120, 311, 25))
        self.lineEditUnitCell.setObjectName(_fromUtf8("lineEditUnitCell"))
        self.lineEditSpaceGroup = QtGui.QLineEdit(self.centralwidget)
        self.lineEditSpaceGroup.setGeometry(QtCore.QRect(10, 120, 81, 25))
        self.lineEditSpaceGroup.setObjectName(_fromUtf8("lineEditSpaceGroup"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 100, 81, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 100, 161, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButtonProcessRefDS = QtGui.QPushButton(self.centralwidget)
        self.pushButtonProcessRefDS.setGeometry(QtCore.QRect(650, 110, 141, 27))
        self.pushButtonProcessRefDS.setObjectName(_fromUtf8("pushButtonProcessRefDS"))
        self.pushButtonProcessAllDS = QtGui.QPushButton(self.centralwidget)
        self.pushButtonProcessAllDS.setGeometry(QtCore.QRect(600, 360, 191, 27))
        self.pushButtonProcessAllDS.setObjectName(_fromUtf8("pushButtonProcessAllDS"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 400, 781, 251))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.lineEditResolution = QtGui.QLineEdit(self.centralwidget)
        self.lineEditResolution.setGeometry(QtCore.QRect(710, 330, 81, 25))
        self.lineEditResolution.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditResolution.setObjectName(_fromUtf8("lineEditResolution"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(600, 340, 111, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(460, 100, 131, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.radioButtonFriedelTrue = QtGui.QRadioButton(self.centralwidget)
        self.radioButtonFriedelTrue.setGeometry(QtCore.QRect(460, 120, 102, 20))
        self.radioButtonFriedelTrue.setChecked(True)
        self.radioButtonFriedelTrue.setObjectName(_fromUtf8("radioButtonFriedelTrue"))
        self.radioButtonFriedelFalse = QtGui.QRadioButton(self.centralwidget)
        self.radioButtonFriedelFalse.setGeometry(QtCore.QRect(520, 120, 102, 20))
        self.radioButtonFriedelFalse.setObjectName(_fromUtf8("radioButtonFriedelFalse"))
        self.lineEditWorkingFolder = QtGui.QLineEdit(self.centralwidget)
        self.lineEditWorkingFolder.setGeometry(QtCore.QRect(10, 30, 781, 27))
        self.lineEditWorkingFolder.setObjectName(_fromUtf8("lineEditWorkingFolder"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 171, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.checkBoxNedit = QtGui.QCheckBox(self.centralwidget)
        self.checkBoxNedit.setGeometry(QtCore.QRect(600, 300, 191, 22))
        self.checkBoxNedit.setObjectName(_fromUtf8("checkBoxNedit"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 25))
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.comboBoxRefDS, QtCore.SIGNAL(_fromUtf8("activated(QString)")), self.statusbar.showMessage)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonRefDSPattern.setText(QtGui.QApplication.translate("MainWindow", "Get Ref Data set", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditRefDsPattern.setText(QtGui.QApplication.translate("MainWindow", "xds_*", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditRemainingDSsPattern.setText(QtGui.QApplication.translate("MainWindow", "xds_*", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonRemainingDSsPattern.setText(QtGui.QApplication.translate("MainWindow", "Get  Remaining Data sets", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("MainWindow", "Folder name", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("MainWindow", "Process in XDS", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table.horizontalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("MainWindow", "Include in XSCALE", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCellDetails.setText(QtGui.QApplication.translate("MainWindow", "Get Cell details", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Space Group", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Unit Cell Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonProcessRefDS.setText(QtGui.QApplication.translate("MainWindow", "Process Ref Dataset", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonProcessAllDS.setText(QtGui.QApplication.translate("MainWindow", "Process all Datasets", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditResolution.setText(QtGui.QApplication.translate("MainWindow", "2.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Resolution up to:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Friedel\'s law", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonFriedelTrue.setText(QtGui.QApplication.translate("MainWindow", "True", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonFriedelFalse.setText(QtGui.QApplication.translate("MainWindow", "False", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Working folder:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxNedit.setText(QtGui.QApplication.translate("MainWindow", "Edit with Nedit?", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

