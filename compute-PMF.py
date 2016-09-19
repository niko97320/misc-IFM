# Copyright Nicolas Martin
# 18/09/16

import numpy as np
import os.path
import sys 
from matplotlib import pyplot as plt
from scipy import math

#inpW = "density.txt"
inpX = ["wind1.colvars.traj","wind2.colvars.traj","wind3.colvars.traj","wind4.colvars.traj","wind5.colvars.traj","wind6.colvars.traj","wind7.colvars.traj","wind8.colvars.traj","wind9.colvars.traj","wind10.colvars.traj","wind11.colvars.traj","wind12.colvars.traj","wind13.colvars.traj","wind14.colvars.traj","wind15.colvars.traj","wind16.colvars.traj","wind17.colvars.traj","wind18.colvars.traj","wind19.colvars.traj","wind20.colvars.traj","wind21.colvars.traj","wind22.colvars.traj","wind23.colvars.traj","wind24.colvars.traj","wind25.colvars.traj","wind26.colvars.traj","wind27.colvars.traj","wind28.colvars.traj","wind29.colvars.traj","wind30.colvars.traj","wind31.colvars.traj","wind32.colvars.traj","wind33.colvars.traj","wind34.colvars.traj","wind35.colvars.traj","wind36.colvars.traj","wind37.colvars.traj",]
#inpX = ["wind1.colvars.traj", "wind2.colvars.traj"]

Kb=0.001987191683
T = 300 #kelvin

print ("# Reading colvar files ...")

l=[]
for i in inpX :
    print ("# Reading data from %s" % i)
    # cannot take the first 1000 lines since the brwgs.sh is taking the 1000 lasts
    #~ X = np.genfromtxt(i, usecols=1, max_rows=10000)
    X = np.genfromtxt(i, usecols=1)
    print ("# Number of lines read: %i" % len(X))
    l.append(X)
print ("# Done")
print ("# Converting list to numpy array")
# ravel is used to colapse the array of array into one single 1D array
XCum = np.ravel(np.asarray(l))

np.savetxt('XCum.out', XCum, delimiter='\t')
#np.savetxt('weights.out', weights, delimiter='\t')

# remove duplicates to only loop over the uniq values of X
# /!\ np.unique use alone will sort the content, leading to a different order, 
# which is NOT what we want
XCumUniq=np.asarray([XCum[i] for i in sorted(np.unique(XCum, return_index=True)[1])])

# iterates over all the Gibbs iterations
#~ l=[]
#initialize array to collect all the PMF for all GIBBS iteration
tot = np.array([[],[]], dtype='float64')
# reshape it into a x line 2 column array
tot = np.transpose(tot)

for i in range(0,2):
    
    # Reading array containing the weight of all structures in the current Gibbs iterations
    inpW="G%i.dat" % i
    print ("# Reading weights file %s ..." % inpW)
    weights = np.genfromtxt(inpW, usecols=(0,3))
    print ("# Done")
    
    if (len(weights[weights[:,0]==i])!=len(XCum)):
    # check only the first GIBBS sampler iteration since they are all the same lenght
        print ("Weight and colvar values arrays aren't the same lenght (%i != %i)" % (len(weights[weights[:,0]==0]), len(XCum)))
        sys.exit(1)
    
    Wx = (weights[weights[:,0]==i])[:,1]
    pmf = -0.5*Kb*T*np.log(Wx)
    # produces a 2lines x column array
    merged = np.vstack((XCum, pmf))
    # transform into a x line 2 columns array
    merged = np.transpose(merged)
    Ex=np.append(tot,merged, axis=0)
    #~ l.append(merged)
    #plt.scatter(XCum[:len(Wx)], pmf)
    #plt.show()

    output = "pmf%i.dat" % i
    
    # sort Ex so it goes from the smallest to the biggest X value
    Ex = Ex[Ex[:,0].argsort()]

    np.savetxt(output, Ex, delimiter='\t')
    
###############
## PART for summing the weight per conformation
## Not working atm
###############
    #~ Wxl=[]
    #~ # loop over all the unique values of XCum array
#~ for x in XCumUniq :
    #~ # get the id where XCum is equal to x
    #~ ii = np.argwhere((XCum==x))
    #~ # since XCumUniq is shorter than Xcum some values should be repeated thus 
    #~ # the lenght of ii should be 2 sometimes
    #~ if len(ii)>=2 :
        #~ print "YOOOO"
        #~ print XCum
        #~ print XCumUniq
        #~ print ii
    #~ # in column 4 is located the weight
    #~ # creates an array with only the weights for the id of interest 
    #~ #if len(ii)!=1:
    #~ #    print weights[ii,3]
        #~ tmp = weights[ii,3]
        #~ Wx = tmp[np.sum(np.argwhere(weights[:,0]==i))]
        #~ Wx = -Kb*T*np.log(Wx)
        #~ Wxl.append(Wx)
#~ 
    #~ Wxf=np.asarray(Wxl)
###############
###############

# print "XCum is of shape {} and of length {}".format(np.shape(XCum), len(XCum))
# print "Weight is of shape {} and of length {}".format(np.shape(weights), len(weights))

# merge the X and weight array in one
#tmp = np.vstack((XCum, weights))
#np.shape(tmp)

# compute the histograms, i.e. sum of the weights for each value of X
#plt.plot(XCumUniq, Wxf)
#plt.show()
# creates an array with X and Wcum
# Sort the array by X values
# take the -KbT*log of the weights
#final = tmp[:, log()]
