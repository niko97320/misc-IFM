# This script post processes the output of the gwham program written by Mahmoud Moradi
# Copyright Nicolas Martin
# 18/09/16

import numpy as np
import os
import sys 
from matplotlib import pyplot as plt
from scipy import math

# Reading parameters

print "Reading parameters"

inpX = ["wind1.colvars.traj","wind2.colvars.traj","wind3.colvars.traj","wind4.colvars.traj","wind5.colvars.traj","wind6.colvars.traj","wind7.colvars.traj","wind8.colvars.traj","wind9.colvars.traj","wind10.colvars.traj","wind11.colvars.traj","wind12.colvars.traj","wind13.colvars.traj","wind14.colvars.traj","wind15.colvars.traj","wind16.colvars.traj","wind17.colvars.traj","wind18.colvars.traj","wind19.colvars.traj","wind20.colvars.traj","wind21.colvars.traj","wind22.colvars.traj","wind23.colvars.traj","wind24.colvars.traj","wind25.colvars.traj","wind26.colvars.traj","wind27.colvars.traj","wind28.colvars.traj","wind29.colvars.traj","wind30.colvars.traj","wind31.colvars.traj","wind32.colvars.traj","wind33.colvars.traj","wind34.colvars.traj","wind35.colvars.traj","wind36.colvars.traj","wind37.colvars.traj",]
inpW="density.txt"
output = "pmf.dat"
Kb=0.001987191683
# expressed in kcal/mol
T = 300 
# kelvin
print "###########################################"
print "# List of inputs for colvar values is: %s" % inpX 
print "# Input for weights/density is: %s " % inpW
print "# Temperature is: %f" % T
print "# Results are store in the output file: %s" % output
print "###########################################"

# check if restart file exists
choiceOK = False
if os.path.exists('XCum.out') :
    while choiceOK == False : 
        print "# Previous concatenated colvar file has been found"
        print "# Do you want to use it (u) or create a new one (n)"
        choice = raw_input(">>> ")
        if choice == "u" : 
            inpX = "XCum.out" 
            XCum = np.genfromtxt(inpX)
            choiceOK=True
        elif choice == "n" : 
            print ("# Reading colvar files ...")
            l=[]
            for i in inpX :
                print ("# Reading data from %s" % i)
                X = np.genfromtxt(i, usecols=1)
                print ("# Number of lines read: %i" % len(X))
                l.append(X)
            print ("# Done reading")
            # ravel is used to collapse the array of array into one single 1D array
            XCum = np.ravel(np.asarray(l))
            np.savetxt('XCum.out', XCum, delimiter='\t')
            choiceOK=True
        else :  
            print "# Incorrect entry ..."
# if not read from colvar files 
else : 
    print ("# Reading colvar files ...")
    l=[]
    for i in inpX :
        print ("# Reading data from %s" % i)
        X = np.genfromtxt(i, usecols=1)
        print ("# Number of lines read: %i" % len(X))
        l.append(X)
    # ravel is used to collapse the array of array into one single 1D array
    XCum = np.ravel(np.asarray(l))
    print ("# Done reading")
    np.savetxt('XCum.out', XCum, delimiter='\t')

# Reading array containing the weight of all structures in the current Gibbs iterations
print ("# Reading weights file %s ..." % inpW)
weights = np.genfromtxt(inpW, usecols=(0,2))
print ("# Done")

# checking input
if (len(weights)!=len(XCum)):
    print ("Weight and colvar values arrays aren't the same lenght (%i != %i)" % (len(weights), len(XCum)))
    sys.exit(1)
    
Wx = weights[:,1]
# produces a 2lines x column array
merged = np.vstack((XCum, Wx))
# transform into a x line 2 columns array
merged = np.transpose(merged)

# nbin must be defined by user
x, binEdge = np.histogram(merged[:,0], weights=merged[:,1], bins=50)
centers = (binEdge[:-1] + binEdge[1:]) / 2
merged1 = np.vstack((centers,-Kb*T*np.log(x)))
merged1 = np.transpose(merged1)
np.savetxt(output, merged1, delimiter='\t')   

