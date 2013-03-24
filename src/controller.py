# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 16:01:16 2013

@author: leal
"""
import glob
import os
import sys

import clusterAnalysis
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
        
    
    
    def addReferenceDataSetToAllXdsInpFiles(self,referenceDS,listOfDS):
        '''
        Will add : REFERENCE_DATA_SET = @referenceDSFolder/XDS_ASCII.HKL
        to the @listOfDS
        '''
        
        if not os.path.exists(referenceDS):
            logger.error('Reference data set does not exist: ' + referenceDS)
            return
            
        
        referenceDSBaseFolderName = os.path.dirname(referenceDS) 
        logger.debug('Reference data set base folder name : ' + referenceDSBaseFolderName)
        
        if os.path.basename(referenceDS) != config.Config().getPar('XDS','hkl_file_name') :
            referenceDSHklFilePath = os.path.join(referenceDSBaseFolderName,config.Config().getPar('XDS','hkl_file_name'))
        logger.debug('Reference data set HKL file path : ' + referenceDSHklFilePath)
        
        xdsRef = xdsHandler.XdsHandler(referenceDSHklFilePath)
        xdsRef.parseXdsInpFile()
        
        for ds in listOfDS:
            xds = xdsHandler.XdsHandler(ds)
            if not xds == xdsRef:
                logger.info('Adding ref DS (%s) to %s'%(referenceDSHklFilePath,xds.xdsInpFilePath))
                xds.parseXdsInpFile()
                keyWord = config.Config().getPar('XDS','reference_data_set_keyword')
                xds.xdsInpDic[keyWord]=referenceDSHklFilePath
                xds.xdsInpDic['SPACE_GROUP_NUMBER'] = xdsRef.xdsInpDic['SPACE_GROUP_NUMBER']
                xds.xdsInpDic['UNIT_CELL_CONSTANTS'] = xdsRef.xdsInpDic['UNIT_CELL_CONSTANTS']
                xds.dumpXdsInpToFile()
    
    def buildXscaleInpFile(self,baseFolder,dataSetsToIncludeInXscale,
                           friedelsLaw,resolution):
        '''
        folder should be os.getcwd()
        '''
        xds = xdsHandler.XdsHandler(baseFolder)
        xscaleInpFilePath = xds.buildXscaleInp(dataSetsToIncludeInXscale, 
                                               friedelsLaw,resolution)
        return xscaleInpFilePath
    
    def buildDendrogram(self,baseFolder):
        
        logger.info('Building the Dendrogram...')
        
        xds = xdsHandler.XdsHandler(baseFolder)
        xds.parseXscaleLpFile()
        xds.createCcMatrix()
        dendro = clusterAnalysis.ClusterAnalysis(xds.ccMatFilePath)
        dendro.plotDendogram()

        
                
                
    
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
    c.addReferenceDataSetToAllXdsInpFiles('xds_x2_run1_1/',listOfDS)
    
                 
    