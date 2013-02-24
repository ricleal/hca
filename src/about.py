# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created: Fri Jun  1 11:19:42 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogAbout(object):
    def setupUi(self, DialogAbout):
        DialogAbout.setObjectName(_fromUtf8("DialogAbout"))
        DialogAbout.resize(391, 304)
        self.pushButtonAboutOK = QtGui.QPushButton(DialogAbout)
        self.pushButtonAboutOK.setGeometry(QtCore.QRect(150, 260, 101, 27))
        self.pushButtonAboutOK.setObjectName(_fromUtf8("pushButtonAboutOK"))
        self.textBrowser = QtGui.QTextBrowser(DialogAbout)
        self.textBrowser.setGeometry(QtCore.QRect(30, 10, 331, 231))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

        self.retranslateUi(DialogAbout)
        QtCore.QMetaObject.connectSlotsByName(DialogAbout)

    def retranslateUi(self, DialogAbout):
        DialogAbout.setWindowTitle(QtGui.QApplication.translate("DialogAbout", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAboutOK.setText(QtGui.QApplication.translate("DialogAbout", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setHtml(QtGui.QApplication.translate("DialogAbout", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">Hierarchical Cluster Analysis</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Please cite:</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">R. Giordano, R. M. F. Leal, G. Bourenkov, S. McSweeney, A. Popov.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic; text-decoration: underline;\">The application of hierarchical cluster analysis to the selection of isomorphic crystals</span><span style=\" font-size:12pt; font-style:italic;\">.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-style:italic; color:#000000;\">Acta Cryst.</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\"> (2012). D</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">68</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">, 649-658</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

