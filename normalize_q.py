#!/usr/bin/env python
#.. This script convert a quaternion into a an angle and axis

import numpy as np
import sys, os  
from math import *

if len(sys.argv) <4 :
  print "Error: You must specifiy at least 4 arguments"
  print "Error: example: normalize_q.py q1 q2 q3 q4"
  exit

else : 
  q1=float(sys.argv[1])
  q2=float(sys.argv[2])
  q3=float(sys.argv[3])
  q4=float(sys.argv[4])
 
  print "# Quaternion input is: ",q1,q2,q3,q4
 
  normq=sqrt(q1*q1+q2*q2+q3*q3+q4*q4)
 
  normq2=(q1/normq)**2+(q2/normq)**2+(q3/normq)**2+(q4/normq)**2 
  if (normq2>=0.99 and normq2<=1.01) :   
    print "# Quaternion normalized is: "
    print q1/normq,q2/normq,q3/normq,q4/normq 
  else :
    print "The norm of the quaternion is ", normq
    print "The norm of the quaternion is not 0."
    print "Error... Exiting"
    exit(1)
