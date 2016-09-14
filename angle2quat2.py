#!/usr/bin/env python
#.. This script convert a quaternion into a an angle and axis

import numpy as np
import sys, os  
from math import *

if len(sys.argv) <4 :
  print "Error: You must specifiy at least 4 arguments"
  print "Error: example: angle2quat2.py angle[deg] x y z"
  exit

else : 
  theta=float(sys.argv[1])
  x=float(sys.argv[2])
  y=float(sys.argv[3])
  z=float(sys.argv[4])
 
  print "#Angle specified is: ",theta,"deg"
 
  # Axis must be normalized
 
  norm=sqrt(x*x+y*y+z*z)
  x_norm=x/norm
  y_norm=y/norm
  z_norm=z/norm
  
  #print x_norm,y_norm,z_norm 
  
  # computing the quaternion
  
  q2=x*sin(radians(theta)/2)
  q3=y*sin(radians(theta)/2)
  q4=z*sin(radians(theta)/2)
  q1=cos(radians(theta)/2)
  
  normq=sqrt(q1*q1+q2*q2+q3*q3+q4*q4)
  
  #print "Quaternion is (",q1/norm,q2/norm,q3/norm,q4/norm,")" #convert in degrees
  print "#Quaternion is: " 
  print q1,q2,q3,q4
