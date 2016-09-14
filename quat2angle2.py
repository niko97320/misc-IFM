#!/usr/bin/env python
#.. This script convert a quaternion into a an angle and axis

import numpy as np
import sys, os
from math import *

if len(sys.argv) <4 :
  print "Error: You must specifiy at least 4 arguments"
  print "Error: example: quat2angle2.py q1 q2 q3 q4"
  exit
else :

  q1=float(sys.argv[1])
  q2=float(sys.argv[2])
  q3=float(sys.argv[3])
  q4=float(sys.argv[4])

  print "#Quaternion specified is: (",q1,q2,q3,q4,")"
  # computing and normalizing the axis of rotation

  x=q2/sqrt(1-(q1*q1))
  y=q3/sqrt(1-(q1*q1))
  z=q4/sqrt(1-(q1*q1))

  print "#Axis of rotation is (x,y,z):"
  print x,y,z

  angle=2*acos(q1) # gives an angle in radians

  print "#Angle of rotation is (deg): " #convert in degrees
  print degrees(angle)
