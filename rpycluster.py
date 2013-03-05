#!/usr/bin/python


'''
The application of hierarchical cluster analysis to the selection of isomorphous crystals
R. Giordano, R. M. F. Leal, G. P. Bourenkov, S. McSweeney and A. N. Popov
Acta Cryst. (2012). D68, 649-658

@author: Rita Giordano & Ricardo Leal

'''

import rpy2
import rpy2.robjects as robjects
import numpy as np
from numpy import *
import rpy2.robjects.numpy2ri as np2r
from rpy2.robjects.packages import importr

"""

This file is not part of the project
It is only used for testing. It reads a matrix file (CCs parsed from XSCALE.LOG)
and builds the dendrogram.

"""

# Change this!!!!
# matrix file path
filename = "/tmp_14_days/ric/Rita/XSCALE/cc.mat"

# Define robjects
r = robjects.r
stats = importr('stats')

# Open the data
data=robjects.r('read.table("' + filename  + '")')
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
r.plot(stats.hclust(dist_m),sub="", xlab="")
## Cut the dendrogram at one desiderable value h 
stats.rect_hclust(stats.hclust(dist_m), h=0.15)

