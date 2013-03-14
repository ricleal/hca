'''
The application of hierarchical cluster analysis to the selection of isomorphous crystals
R. Giordano, R. M. F. Leal, G. P. Bourenkov, S. McSweeney and A. N. Popov
Acta Cryst. (2012). D68, 649-658

@author: ricardo.leal@esrf.fr

This files handles XDS.INI and XDS_ASCII.HKL

Ordered dictionaries are built to keep the contents of these files

It parses the XSCALE.LP and builds a CC matrix which can be used to plot the dendrogram

'''
import sys
import os
import errno
import time
import re
import collections
import pprint
import shutil
import datetime

# local imports
import airspeed 
import config
import log
logger = log.setupLogger("xds")


class XdsHandler :
    """
    Prepares the XdsHandler.INI file 
    """
    
    def __init__(self,path) :
        """
        @param path : folder where the XDS files are
        """
        
        logger.debug("Initialising XDS Handler with : " + path)
        
        # make sure that path is a folder
        if not os.path.isdir(path):
            path =  os.path.dirname(path)
        

        self.xdsInpFilePath = os.path.join(path,
                                           config.Config().getPar("XDS","inp_file_name"))
        self.xdsHklFilePath = os.path.join(path,
                                           config.Config().getPar("XDS","hkl_file_name"))
        #xscale paths
        self.xscaleFolderPath = os.path.join(path,
                                        config.Config().getPar("XDS","xscale_folder_name"))
        self.xscaleInpFilePath = os.path.join(self.xscaleFolderPath,
                                           config.Config().getPar("XDS","xscale_inp_file_name"))
        self.xscaleLpFilePath = os.path.join(self.xscaleFolderPath,
                                           config.Config().getPar("XDS","xscale_lp_file_name"))
        self.ccMatFilePath = os.path.join(self.xscaleFolderPath,
                                           config.Config().getPar("R","cc_matrix_file_name"))
        
        

        # dicts
        self.xdsInpDic = collections.OrderedDict()
        self.xdsHklDic = collections.OrderedDict()
    
    def parseXdsInpFile(self):
        """
        Put the XDS.INI file in a ordered dic : self.xdsInpDic
        """
        if os.path.isfile(self.xdsInpFilePath) is False :
            logger.error("File does not exist: " + self.xdsInpFilePath)
            return
        
        fp = open(self.xdsInpFilePath)
        for line in fp:
            commentCharacterPos = line.find('!')
            if commentCharacterPos >= 0 :
                # if the line has a comment
                line = line[:commentCharacterPos]
            line = line.strip()
            splittedLine = re.split("([a-zA-Z0-9_\-'\(\)]+)=",line)
            splittedLine = [i.strip() for i in splittedLine]
            self.xdsInpDic.update(zip(splittedLine[1:][::2], splittedLine[1:][1::2]))
        #pprint.pprint(self.xdsInpDic.items())
        
    def parseXdsHklFile(self):
        """
        Put the XDS.INI file in a ordered dic : self.xdsInpDic
        """
        if os.path.isfile(self.xdsHklFilePath) is False :
            logger.error("File does not exist: " + self.xdsInpFilePath)
            return
        
        fp = open(self.xdsHklFilePath)
        for line in fp:
            commentCharacterPos = line.find('!')
            if commentCharacterPos >= 0 :
                # if the line has a comment
                line = line[commentCharacterPos:]
            else :
                # ed of the header
                break
            line = line.strip()
            splittedLine = re.split("([a-zA-Z0-9_\-'\(\)]+)=",line)
            splittedLine = [i.strip() for i in splittedLine]
            self.xdsHklDic.update(zip(splittedLine[1:][::2], splittedLine[1:][1::2]))
            
    
    def __createBackup(self,filePath):
        """ general bakup function """
        outFilePath = "%s.%d"%(filePath,int(time.time()*1e6))
        logger.info("Backing up file %s to %s."%(filePath,outFilePath))
        shutil.copy(filePath, outFilePath)
    
    def __backupXdsInp(self):
        self.__createBackup(self.xdsInpFilePath)
    
    def dumpXdsInpToFile(self,out=None):
        """ Dumps the content of the XdsInpdic to a new File """
        if out is None:
            out = self.xdsInpFilePath
        self.__backupXdsInp()
        logger.debug("Dumping XDS INP dict to the file: %s"%out)
        fp = open(out,'w')
        fp.write("! XDS.INI file written by XdsHandler on the %s\n\n" % datetime.datetime.now())
        for key, val in self.xdsInpDic.items():
            fp.write("%s= %s\n" %(key,val))
        fp.close()
    
    def __makeDir(self,path):
        """
        Similar to mkdir -p in linux :
               -p, --parents
              no error if existing, make parent directories as needed
        """
        try:
            os.makedirs(path)
        except OSError as exc: # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                logger.error("Problem creating the folder: " + path)
                raise

        
        
    def buildXscaleInp(self,listOfDataSetsToInclude,friedelsLawFlag,resolution):
        """
        Reads the template and saves the XSCALE.INP file
        """
        self.__makeDir(self.xscaleFolderPath) 
        
        loader = airspeed.CachingFileLoader(".") 
        template = loader.load_template(config.Config().getPar("XDS","xscale_template_file_name"))
        
        # inputs for the template
        dict = {}
        dict['date'] = str(datetime.datetime.now())
        dict['output_file'] = config.Config().getPar("XDS","xscale_out_file_name")
        dict['friedels_law_value'] = str(friedelsLawFlag).upper()
        dict['input_files'] = listOfDataSetsToInclude
        dict['resolution_limit'] = resolution
        
        outFileContents = template.merge(dict, loader=loader)
        logger.info("Writting XSCALE.INP to %s."%self.xscaleInpFilePath)
        fp = open(self.xscaleInpFilePath,'w')
        fp.writelines(outFileContents)
        fp.close()
    
    def parseXscaleLpFile(self):
        """
        Parses the XSCALE.LP file, finds the correlation coefficients (CC)
        between the datasets and put everything in a list of lists of the
        form [CCi,CCj,Value] 
        """
        logger.info("Parsing XSCALE log file: " +  self.xscaleLpFilePath)
        
        # put file contents in list of lines
        inp = open(self.xscaleLpFilePath,"r")
        lines = inp.readlines()
        inp.close()

        ccHeader = 'OVERALL SCALING AND CRYSTAL DISORDER CORRECTION'
        #    1    2        7414           0.998            1.0028        -0.0150
        ccPattern   = re.compile('[^!]\s*(\d+)\s*(\d+)\s+\d+\s+(\d+\.\d+)\s+.*$')
        
        # parse file content
        inCC = False
        self.ccList = []
        for line in lines:
            if line.find(ccHeader) > 0:
                inCC = True
            if inCC is True:
                cc = ccPattern.search(line)
                if cc is not None :
                    self.ccList.append([int(cc.group(1)),int(cc.group(2)),float(cc.group(3))])
                elif len(self.ccList) > 0 :
                    inCC = False
        #pprint.pprint(self.ccList)
    
    def createCcMatrix(self):
        """
        creates a CC matrix file in the R form
        from the list of CCs - self.ccList 
        """

        matrix = {}
        for i in self.ccList:
            #print line
            matrix[(i[0],i[1])] = i[2]

        logger.info("Creating CC matrix file: " +  self.ccMatFilePath) 
        f = open(self.ccMatFilePath,'w')
        
        keys_x = [line[0] for line in matrix.keys()]
        keys_y = [line[1] for line in matrix.keys()]
        
        
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
                elif matrix.has_key((row,col)):     # check for key before fetch
                    print >>f, "%2.3f" % matrix[(row,col)] ,
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
        
               
    
if __name__ == "__main__":
    
    # Copy files to test if this is working!     
    shutil.copy("../data/xds_x2_run1_1/XDS.INP", "/tmp/")
    shutil.copy("../data/xds_x2_run1_1/XDS_ASCII.HKL", "/tmp/")
    #shutil.copy("../data/XSCALE/XSCALE.LP", "/tmp/XSCALE/")
    
    # Fun starts here
    xds = XdsHandler('/tmp')
    logger.debug("XDS.INI full path: " + xds.xdsInpFilePath)
    logger.debug("XDS_ASCII.HKL full path: " + xds.xdsHklFilePath)
    
    xds.parseXdsInpFile()
    xds.parseXdsHklFile()
    xds.dumpXdsInpToFile()
    # to show the backuped files
    import glob
    print glob.glob('/tmp/XDS.INP*')
    logger.debug("End...")
    
    xds.buildXscaleInp(['../xds1/XDS.INP','../xds2/XDS.INP','../xds3/XDS.INP','../xds4/XDS.INP'], True,1.2)
    xds.parseXscaleLpFile()
    xds.createCcMatrix()