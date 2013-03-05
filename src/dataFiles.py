'''
The application of hierarchical cluster analysis to the selection of isomorphous crystals
R. Giordano, R. M. F. Leal, G. P. Bourenkov, S. McSweeney and A. N. Popov
Acta Cryst. (2012). D68, 649-658

@author: ricardo.leal@esrf.fr

'''

import subprocess as sub
import sys
import os
import re
import csv
import time
import threading
import getpass
import os.path

import oar
from PyQt4 import QtGui, QtCore
import clusterAnalysis

__author__ = "Ricardo M. Ferraz Leal"
__copyright__ = "Copyright 2012, European Synchrotron Radiation Facility"
__credits__ = ["Ricardo M. Ferraz Leal", "Alexander N. Popov", "Gleb P. Bourenkov",
                    "Sean McSweeney", "Rita Giordano"]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Ricardo M. Ferraz Leal"
__email__ = "ricardo.leal@esrf.fr"
__status__ = "Beta"

class WaitForOarToFinishThread(QtCore.QThread):
    '''
    Thread to check OAR status and print it to the text window
    '''
    def __init__(self, parent = None):
        QtCore.QThread.__init__(self, parent)
    
    def run(self):
        command = '/usr/bin/oarstat  -u ' + getpass.getuser() + " | grep " + DataFiles.oarJobName
        output = DataFiles.run(command)
        while output is not None and len(output)>0 :
            self.sendTextMessage(output.strip())
            output="Sleeping for 10 seconds: Waiting for the jobs to stop..."
            #self.emit(QtCore.SIGNAL("output(QString)"),QtCore.QString(output))
            self.sendTextMessage(output.strip())
            time.sleep(10)
            output = DataFiles.run(command)
        #self.emit(QtCore.SIGNAL("output(QString)"),QtCore.QString("OAR Job(s) finished"))
        self.sendTextMessage("<b>OAR Job(s) finished</b>")
    
    def sendTextMessage(self,text):
        self.emit(QtCore.SIGNAL("output(QString)"),QtCore.QString(text))

            
class DataFiles:
    
    oarJobName = 'clusterAn'
    
    def __init__(self,currentFolder=None):
        ###################### Program parameters
        self.xdsHklFileName = 'XDS_ASCII.HKL'
        self.xdsIniFileName = 'XDS.INP'
        self.xscaleIniFileName = 'XDS.INP'
        self.xdsCommand = '/opt/pxsoft/bin/xds_par'
        self.xscaleCommand = '/opt/pxsoft/bin/xscale_par'
        self.xscaleFolderName = 'XSCALE'
        self.ccMatrixFileName = 'cc.mat'
        ###################### User parameters
        #self.baseFolderPath = '/data/id23eh1/inhouse/opid231/20110605/PROCESSED_DATA/GALYNA/LOOP2'
        self.spaceGroupNumber = None
        self.unitcell = None
        self.friedelsLaw = True # default
        self.currentWorkingFolderPath = None
        
        
    @staticmethod
    def run(command) :
        p = sub.Popen(command, stdout=sub.PIPE, stderr=sub.PIPE, shell=True)
        output, errors = p.communicate()
        if errors is not None and len(errors) > 0 :
            print errors
        return output
    
    @staticmethod
    def getInHMS(seconds):
        hours = seconds / 3600
        seconds -= 3600*hours
        minutes = seconds / 60
        seconds -= 60*minutes
        if hours == 0:
            return "%02d:%02d" % (minutes, seconds)
        return "%02d:%02d:%02d" % (hours, minutes, seconds)
    
    def retrieveFolderList(self,pattern):
        """
        """
        #path  = os.path.join(self.currentWorkingFolderPath,pattern)
        path = pattern
        lsResult = DataFiles.run("ls -d " + path)
        return lsResult.rstrip('\n').split('\n')
    
    def getSymmetryFromXdsXklFile(self,filename):
        """
        Will parse XDS file and get unit cell and space group number
        """
        print filename
        print self.xdsIniFileName
        print "***"
        
        #xdsFilePath = os.path.join(folderName,self.xdsIniFileName)
        xdsFilePath = os.path.abspath(filename)
        print 'Parsing xds file: %s' % xdsFilePath
        
        # put file contents in list of lines
        inp = open(xdsFilePath,"r")
        lines = inp.readlines()
        inp.close()
        
        # patterns for regular expressions
        # For XDS_ASCII.XHKL
        #spaceGroupNumberPattern   = re.compile('\s*!SPACE_GROUP_NUMBER=\s*(\d+).*$')
        #unitCellConstantsPattern = re.compile('\s*!UNIT_CELL_CONSTANTS=\s*(\d+\.?\d*)\s+(\d+\.?\d*)\s+(\d+\.?\d*)\s+(\d+\.?\d*)\s+(\d+\.?\d*)\s+(\d+\.?\d*).*$')
        # FOR XDS.INP        
        spaceGroupNumberPattern   = re.compile('SPACE_GROUP_NUMBER=\s*(\d+).*$')
        unitCellConstantsPattern = re.compile('UNIT_CELL_CONSTANTS=\s*(\d+\.?\d*)\s+(\d+\.?\d*)\s+(\d+\.?\d*)\s+(\d+\.?\d*)\s+(\d+\.?\d*)\s+(\d+\.?\d*).*$')
        friedelsLawPattern = re.compile("FRIEDEL'S_LAW=\s*(\w+).*$")
        # parse file content
        for line in lines:
            line = line.strip()
            if not line.startswith('!') :    
                spaceGroupNumber = spaceGroupNumberPattern.search(line)
                unitCellConstants = unitCellConstantsPattern.search(line)
                friedelsLaw = friedelsLawPattern.search(line)
                
                if spaceGroupNumber is not None :
                    print 'Space Group = %d' % int(spaceGroupNumber.group(1))
                    self.spaceGroupNumber = int(spaceGroupNumber.group(1))
                    
                elif unitCellConstants is not None:
                    self.unitcell = []
                    for i in range(1,7) :
                        self.unitcell.append(float(unitCellConstants.group(i)))
                    print 'Unit cell = ', self.unitcell
                elif friedelsLaw is not None:
                    res = friedelsLaw.group(1).upper()
                    print 'Friedel\'s law is', res
                    if res == 'TRUE' :
                        self.friedelsLaw = True
                    elif res == 'FALSE' :
                        self.friedelsLaw = False
                    else :
                        print 'ERROR: Friedel\'s law is neither TRUE or FALSE'


    
    def modifyCellAndSgInXdsIniFile(self,folderName):
        """
        Modify unit cell and space group
        """
        
        if self.unitcell is None:
            print 'ERROR: Unit Cell is None!'
            return
        if self.spaceGroupNumber is None:
            print 'ERROR: Space Group number is None!'
            return
        
        xdsFilePath = os.path.join(folderName,self.xdsIniFileName)
        print 'Modifying SG and cell in xds file: %s' % xdsFilePath
        
        # put file contents in list of lines
        inp = open(xdsFilePath,"r")
        lines = inp.readlines()
        inp.close()
        
        # create XDS.INP backup        
        DataFiles.run("cp %s %s_%s" %(xdsFilePath,xdsFilePath,str(time.time())))
        
        outlines = []
        # patterns for regular expressions
        spaceGroupNumberPattern   = re.compile('SPACE_GROUP_NUMBER=.*$')
        unitCellConstantsPattern = re.compile('UNIT_CELL_CONSTANTS=.*$')
        friedelsLawPattern = re.compile("FRIEDEL'S_LAW=\s*(\w+).*$")
       
        # parse file content
        friedelsLawPresentInTheFile = False
        for line in lines:
            line = line.strip()
            if line.startswith('!') :
                outlines.append(line)
            else :                 
                spaceGroupNumber = spaceGroupNumberPattern.search(line)
                unitCellConstants = unitCellConstantsPattern.search(line)
                friedelsLaw = friedelsLawPattern.search(line)
                
                if spaceGroupNumber is not None :
                    #print line
                    newLine = 'SPACE_GROUP_NUMBER= %d\n' % self.spaceGroupNumber 
                    print 'New space group ->',  self.spaceGroupNumber
                    outlines.append(newLine)
                    
                elif unitCellConstants is not None:
                    #print line
                    newLine = 'UNIT_CELL_CONSTANTS= '
                    #print self.unitcell 
                    for i in self.unitcell :
                        newLine += '%.2f '%i
                    newLine += '\n'
                    print 'New unit cell->', newLine,
                    outlines.append(newLine)
                elif friedelsLaw is not None:
                    newLine = "FRIEDEL'S_LAW= "
                    if self.friedelsLaw :
                        newLine += 'TRUE'
                    else :
                        newLine += 'FALSE'
                    print 'FRIEDEL\'S_LAW->', newLine,
                    outlines.append(newLine)
                    friedelsLawPresentInTheFile = True

                else :
                    outlines.append(line)
        
        if friedelsLawPresentInTheFile is False:
            # Add Friedels law flag
            newLine = "FRIEDEL'S_LAW= "
            if self.friedelsLaw :
                newLine += 'TRUE'
            else :
                newLine += 'FALSE'
            print 'FRIEDEL\'S_LAW->', newLine,
            outlines.append(newLine)
            friedelsLawPresentInTheFile = True
            
        outp = open(xdsFilePath,'w')
        #outp.writelines(outlines)
        for l in outlines:
            print l
            outp.write(l + '\n')
        outp.close()
        
    
    def processXdsJob(self, folderName):
        """
        Go throught a list of data sets to process and process them if
        XDS_ASCII.HKL does not exist
        """
        
        print 'Processing dataset: %s ' % folderName
        oarHandler = oar.Oar(folderName)
        jobFilePath = oarHandler.createJob(self.xdsCommand)
        oarHandler.launchJob(jobFilePath,self.oarJobName)
    
    def getOarStatus(self):
                
        command = '/usr/bin/oarstat  -u ' + getpass.getuser() + " | grep " + self.oarJobName
        output = DataFiles.run(command)
        return output
    
    def waitForOarToFinish(self):
        
        output = self.getOarStatus()
        
        while output is not None and len(output)>0 :
            print output
            print("Sleeping for 10 seconds: Waiting for the jobs to stop...")
            time.sleep(10)
            output = self.getOarStatus()
        print("Jobs finished")
    
    def addReferenceDsInXdsIniFile(self,folderName,referenceFolderName):
        """
        Add reference data set
        """
        xdsFilePath = os.path.join(folderName,self.xdsIniFileName)
        print 'Add reference data set to xds file: %s' % xdsFilePath
        
        
        # put file contents in list of lines
        inp = open(xdsFilePath,"r")
        lines = inp.readlines()
        inp.close()
        
        # create XDS.INP backup        
        DataFiles.run("cp %s %s_%s" %(xdsFilePath,xdsFilePath,str(time.time())))
        
        outlines = []
        
        # parse file content
        
        for line in lines:
            if line.find('REFERENCE_DATA_SET') < 0 :
                outlines.append(line)
        outlines.append('REFERENCE_DATA_SET= %s\n\n' %os.path.join('../'+ referenceFolderName, self.xdsHklFileName))
        
        outp = open(xdsFilePath,'w')
        outp.writelines(outlines)
        outp.close()
        
    def includeListOfDataSetsInXscale(self,referenceDataSet,listOfDataSetsToIncludeInXscale,resolution,editWithNedit,waitingThread):
        
        while waitingThread.isRunning() :
            print 'XSCALE will run as soon as XDS finishes...'
            #waitingThread.emit(QtCore.SIGNAL("output(QString)"),QtCore.QString("XSCALE will run as soon as XDS finishes..."))
            waitingThread.sendTextMessage("XSCALE will run as soon as XDS finishes...")
            time.sleep(5)
        
        
        xscaleFolderName = os.path.join(self.currentWorkingFolderPath,self.xscaleFolderName)
                
        try :
            os.mkdir(self.xscaleFolderName)
        except :
            pass
        
        os.chdir(self.xscaleFolderName)
        
        
        outlines = """!============ XSCALE.INP 
!
!      To activate an input parameter remove all "!" left of it.

!MAXIMUM_NUMBER_OF_PROCESSORS=16
!RESOLUTION_SHELLS= 10 6 4 3 2.5 2.0 1.8 1.7 1.6
!SPACE_GROUP_NUMBER=19
!UNIT_CELL_CONSTANTS=65.46 108.41 113.15   90.000  90.000  90.000
!REIDX=-1 0 0 0    0 -1 0 0    0 0 -1 0
!REFERENCE_DATA_SET= ../%s/%s 

!MINIMUM_I/SIGMA=3.0
!REFLECTIONS/CORRECTION_FACTOR=50   !minimum #reflections/correction_factor
!0-DOSE_SIGNIFICANCE_LEVEL=0.10

OUTPUT_FILE=alldatasets.ahkl 
""" % (referenceDataSet,self.xdsHklFileName)

        if self.friedelsLaw :
            outlines += "FRIEDEL'S_LAW= TRUE\n"
        else :
            outlines += "FRIEDEL'S_LAW= FALSE\n"
        
        outlines += """!  MERGE=FALSE !TRUE
!  STRICT_ABSORPTION_CORRECTION=TRUE  !FALSE is default
"""     
        for f in listOfDataSetsToIncludeInXscale :
            # default Path format:
            xdsAsciiFilePath = "../" + f + "/XDS_ASCII.HKL"
            if not os.path.exists(xdsAsciiFilePath) and f[-3:].upper() == 'HKL' :
                xdsAsciiFilePath = "../" + f
                
            if os.path.exists(xdsAsciiFilePath) : 
            
                outlines += "  INPUT_FILE= " + xdsAsciiFilePath + "\n"
                outlines += """    INCLUDE_RESOLUTION_RANGE=100 %s
    !    CORRECTIONS= DECAY MODULATION ABSORPTION
    !    CRYSTAL_NAME=Seleno1 !Remove first "!" to switch on 0-dose extrapolation
    !    STARTING_DOSE=0.0  DOSE_RATE=1.0  !Use defaults for 0-dose extrapolation            
"""%resolution
            else :
                waitingThread.sendTextMessage("Attention: File does not exist: " + xdsAsciiFilePath)
        
        try :
            outp = open('XSCALE.INP','w')
            outp.writelines(outlines)
            outp.close()
        except Exception, e:
            waitingThread.sendTextMessage( "XSCALE.INP: <p>Error: %s</p> : Running XSCALE anyway!" % str(e) )
            

        if editWithNedit :
            os.system('nedit XSCALE.INP')
        
        waitingThread.sendTextMessage("Running XSCALE")
        print 'Running XSCALE'    
        out = DataFiles.run('/opt/pxsoft/bin/xscale_par')
        if out.find('!!! ERROR !!! CANNOT OPEN OR READ') > 0:
            waitingThread.sendTextMessage(out)
        print 'Running XSCALE: DONE!'
        
        waitingThread.sendTextMessage("Running XSCALE: DONE!")
        # TODO PLOT DENDOGRAM
        os.chdir(xscaleFolderName)
        
        if os.path.exists('XSCALE.LP'):
            listOfCc = self.parseXscaleLpFile('XSCALE.LP')
            if len(listOfCc) > 0 :
                print 'Creating CC matrix: ', self.ccMatrixFileName
                self.createCcMatrix(listOfCc)
                print 'Building the Dendrogram...'
                waitingThread.sendTextMessage('Building the Dendrogram...')
                dendro = clusterAnalysis.ClusterAnalysis(self.ccMatrixFileName)
                dendro.plotDendogram()
                
                #self.showDendogram()
                #command = 'python2.6 ~/Python/Rita/src/clusterAnalysis.py'
                #print command
                #os.system(command)
        else :
            waitingThread.sendTextMessage('Could not build the dendrogram! Check if XSCALE.LP file was generated!')
        
        os.chdir('..')
        waitingThread.sendTextMessage('All Done!')


    
    def parseXscaleLpFile(self,xscaleLpFilePath):
        """
        Will 
        """
        
        print 'Parsing xscale log file: %s' % xscaleLpFilePath
        
        # put file contents in list of lines
        inp = open(xscaleLpFilePath,"r")
        lines = inp.readlines()
        inp.close()
        
        
        datasetNumbersHeader = 'DATA    MEAN       REFLECTIONS        INPUT FILE NAME'
        ccHeader = 'OVERALL SCALING AND CRYSTAL DISORDER CORRECTION'
        #    1    2        7414           0.998            1.0028        -0.0150
        ccPattern   = re.compile('[^!]\s*(\d+)\s*(\d+)\s+\d+\s+(\d+\.\d+)\s+.*$')
        
        # parse file content
        inDataSetNumber = False
        inCC = False
        ccList = []
        for line in lines:
            
#            if line.find(datasetNumbersHeader):
#                inDataSetNumber = True
#            if inDataSetNumber is True:
#                if len(line.rstrip('\n').strip()) <= 0:
#                    print inDataSetNumber, len(line.rstrip('\n').strip())
#                    inDataSetNumber = False
#                else :
#                    #print line,
#                    pass
                    
            
            if line.find(ccHeader) > 0:
                inCC = True
            if inCC is True:
                cc = ccPattern.search(line)
                if cc is not None :
                    ccList.append([int(cc.group(1)),int(cc.group(2)),float(cc.group(3))])
                    #print "****", lineNumber
                elif len(ccList) > 0 :
                    inCC = False
                    #print "**** inCC = ", inCC
        import pprint
        pprint.pprint(ccList)
        return ccList


    def createCcMatrix(self,listOfCc):
        
        Matrix = {}
        
        
        for i in listOfCc:
            #print line
            Matrix[(i[0],i[1])] = i[2]
        
        
        
        f = open(self.ccMatrixFileName,'w')
        
        keys_x = [line[0] for line in Matrix.keys()]
        keys_y = [line[1] for line in Matrix.keys()]
        
        #print Matrix 
        #ks=Matrix.keys()
        
        for index_row,row in enumerate(range(int(min(keys_x)),  int(max(keys_x)+1))):    
            #print "Row: " + str(row) +" ",
            for index_col,col in enumerate(range(int(min(keys_y)),  int(max(keys_y)+1))):
            
                # First columns of the matrix must be 1 followed by 0s
                if index_row == 0 and index_col == 0 :
                    print >>f,"%2.3f  " % 1 ,
                elif index_row > 0 and index_col == 0 :
                    print >>f, "%2.3f  " % 0 ,        
                
                # Print file contents
                if row == col :
                    print >>f, "%2.3f" % 1 ,
                elif Matrix.has_key((row,col)):     # check for key before fetch
                    print >>f, "%2.3f" % Matrix[(row,col)] ,
                else:
                    print >>f, "%2.3f" % 0 ,
                print >>f, " ",
            print >>f
        
        
        # Add a new line at the end of the matrix with 0s and 1 at the end of the line
        for col in range(int(min(keys_y)),  int(max(keys_y)+1)):
            if col < int(max(keys_y)+1) :
                print >>f, "%2.3f  " % 0 ,
        print >>f, "%2.3f  " % 1 ,
        print >>f
        print >>f
        
        f.close()

#    def showDendogram(self):
#        import rpy2
#        import rpy2.robjects as robjects
#        import numpy as np
#        import rpy2.robjects.numpy2ri as np2r
#        from rpy2.robjects.packages import importr
#        
#        
#        # Define robjects
#        r = robjects.r
#        stats = importr('stats')
#        
#        # Open the data
#        data=robjects.r('read.table("' + self.ccMatrixFileName +  '")')
#        # transpose the data's matrix
#        cc=r.t(data)
#        
#        cm=robjects.r['as.matrix'](cc)
#        
#        ## Convert thr robjects in numpy objects
#        cm_np=np.array(cm)
#        
#        # define distance function
#        d = np.sqrt(1-cm_np**2)
#        
#        ## convert from numpy to rpy2
#        dist = np2r.numpy2ri(d)
#        
#        dm=robjects.r['as.matrix'](dist)
#        
#        ## Define that dit is a distance matrix
#        dist_m=stats.as_dist(dm)
#        # Perform the cluster analysis and plot the dendrogram
#        
#        r.plot(stats.hclust(dist_m),sub="", xlab="")
#        
#        # Save plot:
#        r('dev.copy(jpeg, file="cluster.jpg",height=600, width=800,bg="white")')
#        
#        ## Cut the dendrogram at one desiderable value h 
#        stats.rect_hclust(stats.hclust(dist_m), h=0.1)
#        
#        r('dev.off()')
#        print "Dendrogram saved..."
    
    
    
