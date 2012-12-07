import rpy2
import rpy2.robjects as robjects
import numpy as np
from numpy import *
import rpy2.robjects.numpy2ri as np2r
from rpy2.robjects.packages import importr


# Define robjects
r = robjects.r
stats = importr('stats')

print 1
# Open the data
data=robjects.r('read.table("/tmp_14_days/ric/Rita/XSCALE/cc.mat")')
# transpose the data's matrix
cc=r.t(data)

print 2

cm=robjects.r['as.matrix'](cc)

## Convert thr robjects in numpy objects
cm_np=np.array(cm)

print 3

# define distance function
d = np.sqrt(1-cm_np**2)

## convert from numpy to rpy2
dist = np2r.numpy2ri(d)

print 4

dm=robjects.r['as.matrix'](dist)

## Define that dit is a distance matrix
dist_m=stats.as_dist(dm)
# Perform the cluster analysis and plot the dendrogram

print 5

r.plot(stats.hclust(dist_m),sub="", xlab="")
## Cut the dendrogram at one desiderable value h 
stats.rect_hclust(stats.hclust(dist_m), h=0.15)
