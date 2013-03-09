#!/usr/bin/python


'''
The application of hierarchical cluster analysis to the selection of isomorphous crystals
R. Giordano, R. M. F. Leal, G. P. Bourenkov, S. McSweeney and A. N. Popov
Acta Cryst. (2012). D68, 649-658

@author: ricardo.leal@esrf.fr

Executable that launches the Qt interface

'''

import sys
from PyQt4 import QtGui, QtCore
from form import Ui_MainWindow
import dataFiles
import threading
import time
import spaceGroups as sg
import os
import about

__author__ = "Ricardo M. Ferraz Leal"
__copyright__ = "Copyright 2012, European Synchrotron Radiation Facility"
__credits__ = ["Ricardo M. Ferraz Leal", "Alexander N. Popov", "Gleb P. Bourenkov",
                    "Sean McSweeney", "Rita Giordano"]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Ricardo M. Ferraz Leal"
__email__ = "ricardo.leal@esrf.fr"
__status__ = "Beta"

class myDialog(QtGui.QDialog, about.Ui_DialogAbout):
    """
    about dialog class
    """
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        
        self.connect(self.pushButtonAboutOK, QtCore.SIGNAL("clicked()"),self.close)
        
    def on_acceptButton_clicked(self):
        self.close()
        
    def on_rejectButton_clicked(self):
        self.close()

class MyApp(QtGui.QMainWindow, Ui_MainWindow): 
    """
    Main window
    """
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        # initialise auxiliary class
        self.data = dataFiles.DataFiles()
        
        # About
        self.popDialog=myDialog()
        
    def openAbout(self):
        print "openAbout"
        self.popDialog.show()

    def log(self,text):
        """ LOGGER """
        self.textBrowser.insertHtml(text + '<br>')
        
    def logW(self,text):
        """ LOGGER warning """
        self.textBrowser.insertHtml('<b>' + text + '</b><br>')

    def logE(self,text):
        """ LOGGER """
        self.textBrowser.insertHtml('<font color="red"><b>' + text + '</b></font><br>')            
                
    
    def searchRefDSs(self):
        """
        button pressed!
        """
        pattern = str(self.lineEditRefDsPattern.text())
        # TODO
        self.log('Searching Reference Datasets')
        lsResult = self.data.retrieveFolderList(pattern) 
        if  self.comboBoxRefDS.count() > 0 :
            self.comboBoxRefDS.clear()
        #self.comboBoxRefDS.addItems(lsResult)
        commonprefix = os.path.commonprefix(lsResult)
        if not os.path.isdir(commonprefix):
            commonprefix = '.'

        for f in lsResult:
            #self.comboBoxRefDS.addItem(os.path.basename(f),QtCore.QVariant(f))
            self.comboBoxRefDS.addItem(os.path.relpath(f,commonprefix),QtCore.QVariant(f))
        
    
    def getRefDSSymmetry(self):
        """
        """
        #currentDS = str(self.comboBoxRefDS.currentText())
        currentIndex = self.comboBoxRefDS.currentIndex()
        currentDS = str(self.comboBoxRefDS.itemData(currentIndex).toString())
        
        if len(currentDS) == 0 :
            self.logE('Reference Data set empty... Have you clicked "Get Ref Data set"?')
            return
        self.log('Getting symmetry from Reference Dataset: <b>%s</b>'%currentDS)
        self.data.getSymmetryFromXdsXklFile(currentDS)
        # populate
        unitCellTxt = ""
        for i in self.data.unitcell:
            unitCellTxt += "%.1f " % i
        self.lineEditUnitCell.setText(unitCellTxt)
        self.lineEditSpaceGroup.setText(str(self.data.spaceGroupNumber))
        if self.data.friedelsLaw is False:
            self.radioButtonFriedelFalse.setChecked(True)
        else :
            self.radioButtonFriedelTrue.setChecked(True)

    def processRefDS(self):
        """
        """
        
        refDS = str(self.comboBoxRefDS.currentText())
        
        if len(refDS) == 0 :
            self.logE('Reference DS empty... have you clicked Ref DSs?')
            return
        
        self.log('<p>Processing Reference Datasets: %s</p>'%refDS)
        
        if self.lineEditUnitCell.text() is not None and len(str(self.lineEditUnitCell.text()).strip()) > 0 :
            self.data.unitcell = [float(i) for i in str(self.lineEditUnitCell.text()).strip().split()]
        
        if self.lineEditSpaceGroup.text() is not None and len(str(self.lineEditSpaceGroup.text()).strip()) > 0 :
            try :
                self.data.spaceGroupNumber = int(str(self.lineEditSpaceGroup.text()).strip())
            except:
                sgStr = str(self.lineEditSpaceGroup.text()).strip()
                sgInt = sg.SpaceGroups.getSpaceGroupNumber(sgStr)
                self.data.spaceGroupNumber = sgInt
                print "Converted to spacegroup:", sgStr, ' --> ', sgInt
        
        if self.radioButtonFriedelFalse.isChecked() : 
            self.data.friedelsLaw = False
        elif self.radioButtonFriedelTrue.isChecked() :
            self.data.friedelsLaw = True
        else :
            print 'ERRROR radioButtonFriedelTrue...'
        
        if self.data.unitcell is not None and self.data.spaceGroupNumber is not None:
            self.log('Modifying XDS file %s. New Symmetry: <b>%s</b> : <b>%s</b>'%(refDS,self.lineEditUnitCell.text(),
                                                                                            self.data.spaceGroupNumber))
            self.data.modifyCellAndSgInXdsIniFile(refDS)
        else :
            self.logW('%s data set submit to XDS as it is....'%refDS)
        self.data.processXdsJob(refDS)
        
        # thread to plot OAR Status 
        self.thread.start()
        
        
    def searchRemainingDSs(self):
        """
        
        """
        
        pattern = str(self.lineEditRemainingDSsPattern.text())
        # TODO
        self.log('Searching Remaining Datasets<br><b>HINT: </b> Click on the column header to select the whole column.')
        lsResult = self.data.retrieveFolderList(pattern)
        
        self.table.setRowCount(len(lsResult));
        
        for i,item in enumerate(lsResult):
            #model.insertRows(i, 1)
            #model.insertRow(i)
            
            # Col 0 Folder name
            temp = QtGui.QTableWidgetItem()
            #temp.setText( item );
            #temp.setData(QtCore.Qt.DisplayRole, item);
            
            # TO DO: This has to work with full path:
            #temp.setText( os.path.basename(item) );
            temp.setText( item );
            
            self.table.setItem( i, 0, temp );
            # Col 1
            checkBox = QtGui.QCheckBox()            
            self.table.setCellWidget(i,1,checkBox)
            # col 2
            checkBox = QtGui.QCheckBox()
            checkBox.setCheckState(QtCore.Qt.Checked)  
            self.table.setCellWidget(i,2,checkBox)
            
            #self.log(item + '<br>')
        
        #item = QtGui.QTableWidgetItem(self.tableWidget)
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()
    
    def processAllDSs(self):
        """
        Process in XDS
        Once XDS done, submit jobs to XSCALE
        """
        
        print 'processAllDSs'
        
        model =  self.table.model()
        dataSetsToIncludeInXscale = []
        dataSetsToProcessInXds = []
        
        refDS = str(self.comboBoxRefDS.currentText())
        
        for row in range(model.rowCount()):
            
            col0 = model.index( row, 0, QtCore.QModelIndex()).data( QtCore.Qt.DisplayRole ).toString()            
            col1 = self.table.cellWidget(row, 1)            
            col2 = self.table.cellWidget(row, 2)
            
            ds = str(col0) 
            if col1.checkState() > 0 :
                #self.textBrowser.insertHtml('Processing dataset <b>' + ds+ '</b><br>')
                dataSetsToProcessInXds.append(ds)
                # modify XDS files
                self.data.modifyCellAndSgInXdsIniFile(ds)
                self.data.addReferenceDsInXdsIniFile(ds,refDS)               
                # submit to condor
                self.data.processXdsJob(ds)
                
            if col2.checkState() > 0 :
                #self.textBrowser.insertHtml('Including in XSCALE <b>' + ds + '</b><br>')
                
                dataSetsToIncludeInXscale.append(ds)
            
#            if col1.checkState() == QtCore.Qt.Checked : # 2
#                print 'checked',            
#            elif col1.checkState() == QtCore.Qt.Unchecked: # 0
#                print 'unchecked',
#            else:
#                print ':(',
        
        if len(dataSetsToProcessInXds)>0:
            #check OAR state
            self.thread.start()
        
#       
        if len(dataSetsToIncludeInXscale) > 0:

            if self.lineEditResolution.text() is not None and len(str(self.lineEditResolution.text()).strip()) > 0 :
                resolution = str(self.lineEditResolution.text())
            else:
                resolution = '2.0'
                        
            self.log('Running XSCALE up to <b>' + resolution + '</b> A resolution')
            
            
            if self.checkBoxNedit.checkState() > 0 :
                editWithNedit = True
            else:
                editWithNedit = False
            
            processThread = threading.Thread(target=self.data.includeListOfDataSetsInXscale, args=(refDS,dataSetsToIncludeInXscale,resolution,editWithNedit,self.thread,))
            processThread.start()
    
            #self.data.includeListOfDataSetsInXscale(dataSetsToIncludeInXscale,resolution)
        else:
            self.logE('No selected DSs to be included in XSCALE!')
            
    
        
    def addLineToTextBrowser(self,text):
        self.log('<pre>%s<pre>'%text)
        c =  self.textBrowser.textCursor();
        c.movePosition(QtGui.QTextCursor.End);
        self.textBrowser.setTextCursor(c);
    
    def selectEntireCollumn(self,index):
        '''
        Called when a table header is clicked. Checks all dropbox in the whole column
        '''
        if (index > 0):
            #print "header index clicked: ", index
            model =  self.table.model()
            if model.rowCount() > 1 :  # more than one column
                cell0 = self.table.cellWidget(0, index)
                check = True
                if cell0.checkState() > 0 : # row 0 is checked
                    #print 'Cell 0 is checked!'
                    check = False
                for row in range(model.rowCount()):
                    cell = self.table.cellWidget(row, index)
                    if check is True:
                        cell.setCheckState(QtCore.Qt.Checked)   
                    else:
                        cell.setCheckState(QtCore.Qt.Unchecked)  
                
                
            
            
        
    def initilise(self):
        self.connect(self.pushButtonRefDSPattern, QtCore.SIGNAL("clicked()"),self.searchRefDSs)
        self.connect(self.pushButtonCellDetails, QtCore.SIGNAL("clicked()"),self.getRefDSSymmetry) 
        self.connect(self.pushButtonProcessRefDS, QtCore.SIGNAL("clicked()"),self.processRefDS)
        
        self.connect(self.pushButtonRemainingDSsPattern, QtCore.SIGNAL("clicked()"),self.searchRemainingDSs)
        self.connect(self.pushButtonProcessAllDS, QtCore.SIGNAL("clicked()"),self.processAllDSs)
        
        #About 
        self.connect(self.actionAbout, QtCore.SIGNAL("triggered()"), self.openAbout)
    
        # Thread
        self.thread = dataFiles.WaitForOarToFinishThread()
        self.connect(self.thread, QtCore.SIGNAL("output(QString)"), self.addLineToTextBrowser)
        
        # table
        self.table.resizeColumnsToContents()
        # header clickable
        #self.connect(self.table.horizontalHeader(),QtCore.SIGNAL('sectionDoubleClicked(int)'),self.on_header_doubleClicked)
        self.connect(self.table.horizontalHeader(),QtCore.SIGNAL('sectionClicked(int)'), self.selectEntireCollumn)
        
        # window 
        self.setWindowTitle('Cluster Analysis')
    


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    window.initilise()
    sys.exit(app.exec_())
    
    
