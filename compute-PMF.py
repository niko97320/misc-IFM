import numpy as np
import os.path
import pylab as plt

inpW = "density.txt"
#inpX = ["wind1.colvars.traj","wind2.colvars.traj","wind3.colvars.traj","wind4.colvars.traj","wind5.colvars.traj","wind6.colvars.traj","wind7.colvars.traj","wind8.colvars.traj","wind9.colvars.traj","wind1.colvars.traj","wind1.colvars.traj","wind1.colvars.traj","wind1.colvars.traj","wind1.colvars.traj","wind1.colvars.traj","wind1.colvars.traj","wind1.colvars.traj","wind1.colvars.traj","wind1.colvars.traj","wind1.colvars.traj","wind1.colvars.traj","wind1.colvars.traj","wind1.colvars.traj","wind1.colvars.traj","wind1.colvars.traj","wind1.colvars.traj","wind1.colvars.traj","wind1.colvars.traj","wind1.colvars.traj","wind1.colvars.traj","wind1.colvars.traj","wind1.colvars.traj","wind1.colvars.traj","wind1.colvars.traj","wind1.colvars.traj","wind1.colvars.traj","wind1.colvars.traj",]
inpX = ["wind1.colvars.traj", "wind2.colvars.traj"]

Kb=0.001987191683
Temperature = 300 #kelvin

# array containing the weight for all structure and all the Gibbs iterations
print ("# Reading weights file ...")
weights = np.genfromtxt(inpW, usecols=3)
print ("# Done")
print ("# Reading colvar files ...")
l=[]
for i in inpX :
    print ("# Reading data from %s" % i)
    X = np.genfromtxt(i, usecols=1)
    l.append(X)
print ("# Done")
print ("# Converting list to numpy array")
XCum = np.asarray(l)

print "XCum is of shape {} and of length {}".format(np.shape(XCum), len(XCum))
print "Weight is of shape {} and of length {}".format(np.shape(weights), len(weights))

# merge the X and weight array in one
tmp = np.vstack((XCum, weights))
np.shape(tmp)

# compute the histograms, i.e. sum of the weights for each value of X

# creates an array with X and Wcum
# Sort the array by X values
# take the -KbT*log of the weights
final = tmp[:, log()]
