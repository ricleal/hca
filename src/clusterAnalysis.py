#!/usr/bin/python

'''
The application of hierarchical cluster analysis to the selection of isomorphous crystals
R. Giordano, R. M. F. Leal, G. P. Bourenkov, S. McSweeney and A. N. Popov
Acta Cryst. (2012). D68, 649-658

@author: ricardo.leal@esrf.fr


This is a standalone file to plot the dendrogram from a matrix file


'''

import rpy2
import rpy2.robjects as robjects
import rpy2.robjects.numpy2ri as np2r
import rpy2.rinterface as rinterface
from rpy2.robjects.packages import importr

import numpy as np
import sys
import os.path
import time
import threading

__author__ = "Ricardo M. Ferraz Leal"
__copyright__ = "Copyright 2012, European Synchrotron Radiation Facility"
__credits__ = ["Ricardo M. Ferraz Leal", "Alexander N. Popov", "Gleb P. Bourenkov",
                    "Sean McSweeney", "Rita Giordano"]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Ricardo M. Ferraz Leal"
__email__ = "ricardo.leal@esrf.fr"
__status__ = "Beta"

#
def r_refresh(interval = 0.03):
    # Ctrl-C to interrupt
    while True:
        rinterface.process_revents()
        time.sleep(interval)


class ClusterAnalysis:
    
    def __init__(self,ccMatFileName):
        self.ccMatFileName = ccMatFileName
        self.outFileName = "cluster.jpg"
        
    def plotDendogram(self):
        
        t = threading.Timer(0.1, r_refresh)
        t.start()
        
        # Define robjects
        r = robjects.r
        stats = importr('stats')
        
        # Open the data
        data=robjects.r('read.table("' + self.ccMatFileName+ '")')
        # transpose the data's matrix
        cc=r.t(data)
        
        cm=robjects.r['as.matrix'](cc)
        
        ## Convert thr robjects in numpy objects
        cm_np=np.array(cm)
        
        # define distance function
        d = np.sqrt(1-cm_np**2)
        
        ## convert from numpy to rpy2
        dist = np2r.numpy2ri(d)
        
        dm=robjects.r['as.matrix'](dist)
        
        ## Define that dit is a distance matrix
        dist_m=stats.as_dist(dm)
        # Perform the cluster analysis and plot the dendrogram
        

        
        # Open display and save plot to a file
        r.plot(stats.hclust(dist_m),sub="", xlab="Dataset number")                
        #stats.rect_hclust(stats.hclust(dist_m), h=0.1,border="red")
        #stats.rect_hclust(stats.hclust(dist_m), h=0.15,border="blue")
        r('dev.copy(jpeg, file="' + self.outFileName + '",height=600, width=800,bg="white")')
        r('dev.off()')
        
        
#        # Save plot! Does not open display!
#        r.jpeg(file=self.outFileName,height=600, width=800,bg="white")
#        r.plot(stats.hclust(dist_m),sub="", xlab="Dataset number")
#        r['dev.off']()
        
        print "Cluster file saved to: %s"%self.outFileName

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit('Usage: %s < matrix file >' % sys.argv[0])
        

    matFile = sys.argv[1]
    if not os.path.exists(matFile):
        sys.exit('ERROR: Matrix file %s was not found!' % matFile)

    # Main
    c = ClusterAnalysis(matFile)
    c.plotDendogram()
    #raw_input("Press ENTER to exit")
    
    
