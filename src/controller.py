# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 16:01:16 2013

@author: leal
"""
import glob
import os
import sys

import xdsHandler
import config
import log
logger = log.setupLogger("controller")


class Controller:
    '''
    Class that will bridge the gui with the remaining classes
    '''
    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def getDetailsFromInpFile(self,xdsFolder,fields = ['SPACE_GROUP_NUMBER',
                  'UNIT_CELL_CONSTANTS',
                  "FRIEDEL'S_LAW"]):
        '''
        gets contents from XDS_ASCII.HKL File
        @returns : a list of the parameters below (same order)
        '''
        
        
        xds = xdsHandler.XdsHandler(xdsFolder)
        xds.parseXdsInpFile()
            
        returnList = []
        for f in fields:
            try:
                returnList.append(xds.xdsInpDic[f])
            except KeyError:
                sys.stderr.write("The key doesn't exist in the HKL file: " + f)
        return returnList
    
    def modifyXdsInpFile(self,xdsFolder,dict):
        '''
        This will modify the XDS.INP file (creates a backup)
                
        :dict : will be dictionary of pairs key:value 
        '''
        
        xds = xdsHandler.XdsHandler(xdsFolder)
        xds.parseXdsInpFile()
        
        # substitute / insert new values        
        for key, val in dict.items():
            xds.xdsInpDic[key]=val
        
        xds.dumpXdsInpToFile()
        
    
    def __getBaseFolderName(self,path):
        '''
        For a path like : 
        /home/leal/tips.txt
        /home/leal/
        I will @return: 'leal'
        '''
        if '/' not in path or '\\' not in path :
            return path
        if not os.path.isdir(path):
            path =  os.path.dirname(path)
        return os.path.basename(os.path.dirname(path))
    
    def addReferenceDataSetToAllXdsInpFiles(self,referenceDSFolder,listOfDS):
        '''
        Will add : REFERENCE_DATA_SET = @referenceDSFolder/XDS_ASCII.HKL
        to the @listOfDS
        '''
        referenceDSBaseFolderName = self.__getBaseFolderName(referenceDSFolder) 
        logger.debug('referenceDSBaseFolderName : ' + referenceDSBaseFolderName)
        
        if os.path.basename(referenceDSFolder) != config.Config().getPar('XDS','hkl_file_name') :
            referenceDSHklFilePath = os.path.join(referenceDSFolder,config.Config().getPar('XDS','hkl_file_name'))
        logger.debug('referenceDSHklFilePath : ' + referenceDSHklFilePath)
        
        for ds in listOfDS:
            # remove the referenceDSFolder from listOfDS
            if referenceDSBaseFolderName != self.__getBaseFolderName(ds):
                xds = xdsHandler.XdsHandler(ds)
                xds.parseXdsInpFile()
                keyWord = config.Config().getPar('XDS','reference_data_set_keyword')
                xds.xdsInpDic[keyWord]=referenceDSHklFilePath
                xds.dumpXdsInpToFile()
    

        
                
                
    
if __name__ == "__main__":
    os.system("cp -r ../data/* /tmp/")

    
    c = Controller()

    os.chdir('/tmp')        
    
    inpFile = '/tmp/xds_x2_run1_1/XDS,INP'
    print c.getDetailsFromInpFile(inpFile)
    
    logger.debug("getDetailsFromHKLFile")    
    dictFields = {'SPACE_GROUP_NUMBER' : '1',
                  'UNIT_CELL_CONSTANTS' : '10 10 10 90 90 90',
                  "FRIEDEL'S_LAW" : 'FALSE' }
    c.modifyXdsInpFile(inpFile,dictFields)
    
    logger.debug("addReferenceDataSetToAllXdsInpFiles")    
    listOfDS = ['xds_x2_run3_1/XDS.INP','xds_x2_run5_1/XDS.INP','xds_x2_run7_1/XDS.INP']
    c.addReferenceDataSetToAllXdsInpFiles('xds_x2_run1_1',listOfDS)
    
                 
    