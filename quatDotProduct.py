#!/usr/bin/env python
#.. This scriptcomputes the dot product of two quaternions	 

import numpy as np
import sys, os
from math import *

if len(sys.argv) <8 :
  print "Error: You must specifiy at least 8 arguments"
  printf ("Error: example: %s q1 q2 q3 q4 w1 w2 w3 w4", sys.argv[0])
  exit
else :

  q1=float(sys.argv[1])
  q2=float(sys.argv[2])
  q3=float(sys.argv[3])
  q4=float(sys.argv[4])
  w1=float(sys.argv[5])
  w2=float(sys.argv[6])
  w3=float(sys.argv[7])
  w4=float(sys.argv[8])

  #print "#Q1 specified is: (",q1,q2,q3,q4,")"
  #print "#Q2 specified is: (",w1,w2,w3,w4,")"

  dotProduct = q1*w2+q2*w2+q3*w3+q4*w4

  print dotProduct 
