#!/usr/bin/env python

# this script is used to check equality between two quaternions
# if the result is the identitty quaternion (0,0,0,1) then they
# are identical
#/!\ Be careful to use only normalized quaternions as input. /!\

from math import *
import numpy as np

def QuaternionProduct(q1w, q1x, q1y, q1z, q2w, q2x, q2y, q2z) :

  qw=(q1w*q2w - q1x*q2x - q1y*q2y - q1z*q2z)
  qx=(q1w*q2x + q1x*q2w + q1y*q2z - q1z*q2y)
  qy=(q1w*q2y + q1y*q2w + q1z*q2x - q1x*q2z)
  qz=(q1w*q2z + q1z*q2w + q1x*q2y - q1y*q2x)
  return qw, qx, qy, qz
# NAMD normalized
# 0.839082 , 0.541886 , -0.042631 , 0.0220057
# NM normalized
# 0.839081728245 0.126907408185 -0.528537709915 0.022005732669

#Quaternion 1
q1=0.839082
q2=0.541886
q3=-0.042631
q4=0.0220057
#Quaternion 2
r1=0.839081728245
r2=0.126907408185
r3=-0.528537709915
r4=0.022005732669

print QuaternionProduct(q1,q2,q3,q4,r1,r2,r3,r4)
