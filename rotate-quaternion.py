#!/usr/bin/env python

# this script takes as input two quaternion and accumalate the rotations
# in other word it multiplies q1 by q2 (Beware multiplication of quaternions
# is not cummutative)

from math import *
import numpy as np
debug=0

def QuaternionProduct(q1w, q1x, q1y, q1z, q2w, q2x, q2y, q2z) :

  qw=(q1w*q2w - q1x*q2x - q1y*q2y - q1z*q2z)
  qx=(q1w*q2x + q1x*q2w + q1y*q2z - q1z*q2y)
  qy=(q1w*q2y + q1y*q2w + q1z*q2x - q1x*q2z)
  qz=(q1w*q2z + q1z*q2w + q1x*q2y - q1y*q2x)
  return qw, qx, qy, qz

def ConjugateQuaternion(qw, qx, qy, qz):
  return qw, -qx, -qy, -qz

def NormQuaternion (qw, qx, qy, qz):
  return sqrt(qw**2+qx**2+qy**2+qz**2)

def NormalizeQuaternion(qw, qx, qy, qz):
  norm=NormQuaternion(qw, qx, qy, qz)
  return qw/norm, qx/norm, qy/norm, qz/norm
  
# quaternion to rotate
# chainE
#9.88145937561436e-01 ,  1.30785604897633e-01 ,  8.01509061100203e-02 , -6.20998245843420e-03
q_w=0.0 # contains the angle
q_x=1.30785604897633e-01
q_y=8.01509061100203e-02
q_z=-6.20998245843420e-03

qw, qx, qy, qz = NormalizeQuaternion(q_w, q_x, q_y, q_z)

#print the initial quaternion
print("%4.14e\t%4.14e\t%4.14e\t%4.14e" % (qw, qx, qy, qz)) 

# loop over the four subunits

for incr in range(1,5) :
	# quaternion describing the rotation
	# user defined
	# rotation of theta deg around z
	theta=incr*2*np.pi/5
	q_rotw=cos(theta/2)
	q_rotx=0
	q_roty=0
	q_rotz=sin(theta/2)
	qrotw, qrotx, qroty, qrotz = NormalizeQuaternion(q_rotw, q_rotx, q_roty, q_rotz)
	if debug==1 :
          print ("Theta is degrees is: ", degrees(theta))


	#..1 product of qrot and qIni	
	qrotw_int, qrotx_int, qroty_int, qrotz_int = QuaternionProduct(qrotw, qrotx, qroty, qrotz, qw, qx, qy, qz)

	#..2 calculate the inverse of qrot
	#..2.1 calculate the conjugate 
	qrotw_conj, qrotx_conj, qroty_conj, qrotz_conj = ConjugateQuaternion(qrotw, qrotx, qroty, qrotz)

	#..2.2 divide by the square norm

	qrotw_inv = qrotw_conj/NormQuaternion(qrotw, qrotx, qroty, qrotz)**2
	qrotx_inv = qrotx_conj/NormQuaternion(qrotw, qrotx, qroty, qrotz)**2
	qroty_inv = qroty_conj/NormQuaternion(qrotw, qrotx, qroty, qrotz)**2
	qrotz_inv = qrotz_conj/NormQuaternion(qrotw, qrotx, qroty, qrotz)**2

	qw_f, qx_f, qy_f, qz_f = QuaternionProduct(qrotw_int, qrotx_int, qroty_int, qrotz_int, qrotw_inv, qrotx_inv, qroty_inv, qrotz_inv)
	
	qwf, qxf, qyf, qzf = NormalizeQuaternion(qw_f, qx_f, qy_f, qz_f)

        if debug==0 : 
	  print("%4.14e\t%4.14e\t%4.14e\t%4.14e" % (qwf, qxf, qyf, qzf)) 
	  #print("%4.14e\t%4.14e\t%4.14e\t%4.14e" % (qw_f, qx_f, qy_f, qz_f)) 

#..DEBUG
if debug==1 :
  # quat
  print "Initial quaternion"
  print("%4.14e\t%4.14e\t%4.14e\t%4.14e" % (q_w, q_x, q_y, q_z))
  print "Initial quaternion normalized"
  print("%4.14e\t%4.14e\t%4.14e\t%4.14e" % (qw, qx, qy, qz))
  print "Rotationnal quaternion"
  print("%4.14e\t%4.14e\t%4.14e\t%4.14e" % (q_rotw, q_rotx, q_roty, q_rotz))
  print "Rotationnal quaternion normalized"
  print("%4.14e\t%4.14e\t%4.14e\t%4.14e" % (qrotw, qrotx, qroty, qrotz))
  # norms 
  print "norm initial quaternion"
  print NormQuaternion(q_w, q_x, q_y, q_z)
  print "norm Initial quaternion normalized"
  print NormQuaternion(qw, qx, qy, qz)
  print "norm rotationnal quaternion"
  print NormQuaternion(q_rotw, q_rotx, q_roty, q_rotz)
  print "norm rotationnal quaternion normalized"
  print NormQuaternion(qrotw, qrotx, qroty, qrotz)
  print "conjugate rotationnal quaternion normalized"
  print ("%4.14e\t%4.14e\t%4.14e\t%4.14e" % (qrotw_conj, qrotx_conj, qroty_conj, qrotz_conj))
  print "inverse rotationnal quaternion normalized"
  print  ("%4.14e\t%4.14e\t%4.14e\t%4.14e" % (qrotw_inv, qrotx_inv, qroty_inv, qrotz_inv))
  print "Resulting quaternion"
  print("%4.14e\t%4.14e\t%4.14e\t%4.14e" % (qw_f, qx_f, qy_f, qz_f))
  print "Resulting quaternion normalized"
  print("%4.14e\t%4.14e\t%4.14e\t%4.14e" % (qwf, qxf, qyf, qzf))
  print "Norm of resulting quaternion normalized"
  print NormQuaternion(qwf, qxf, qyf, qzf)
 
