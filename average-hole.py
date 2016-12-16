#!/usr/bin/env python
#.. NMa 
#.. 23rd May 16


###############
### COMPUTE ###
###############

inp = "IS-IVM-prof.dat"
out = "IS-IVM-prof_avg.dat"

import numpy.ma as ma
import matplotlib.cm as cm
import numpy as np
import matplotlib.pyplot as plt
import sys

#reading argument from command line
if (len(sys.argv)!=4 and sys.argv[1]!="all" ) :
  print "Error: Please specifiy the starting frame, the number \nof bin and the width of the bin"
  print "Info: The script is used as following :"
  print "Info: script.py start nbin binwidth "
  print "Info: or use the following syntax for analysis the full\n traj at once: "
  print "Info: script.py all"
  print "Info: Exit ..."
  sys.exit()

else :
  # reading the input 
  data_dirty=np.genfromtxt(inp)
  # One has to mask INF because they screw up the calculation of the average
  data=ma.masked_invalid(data_dirty)

  if (len(sys.argv)==2 and sys.argv[1]=="all") : 

    # number of bin to devide the trajectory in
    arglist=sys.argv
    start=1
    nbin=1
    binwidth=len(data[0,:])-1
    end=start+nbin*binwidth
    #if (start<1) :
    #  print "Starting frame cannot be less than one"
    #  sys.exit()
  
    if (end>(len(data[0,:]))):
      print "You asked for frame %i and there are only %i in your input file" % (end,len(data[0,:]))
      sys.exit()

    m = data[:,0]
    for i in range(0,nbin) :
      avg=np.average(data[:,start+i*binwidth:start+(i+1)*binwidth], axis=1)
      std=np.std(data[:,start+i*binwidth:start+(i+1)*binwidth], axis = 1)
      m = np.c_[m,avg,std]
    
    np.savetxt(out,m, fmt="%3.3f", delimiter='\t')

  
  else : 

    # number of bin to devide the trajectory in
    arglist=sys.argv
    start=int(arglist[1])
    nbin=int(arglist[2])
    binwidth=int(arglist[3])
    end=start+nbin*binwidth
    if (start<1) :
      print "Starting frame cannot be less than one"
      sys.exit()

    if (end>(len(data[0,:]))):
      print "You asked for frame %i and there are only %i in your input file" % (end,len(data[0,:]))
      sys.exit()

    m = data[:,0]
    for i in range(0,nbin) :
      avg=np.average(data[:,start+i*binwidth:start+(i+1)*binwidth], axis=1)
      std=np.std(data[:,start+i*binwidth:start+(i+1)*binwidth], axis = 1)
      m = np.c_[m,avg,std]

#    np.savetxt(out,m, fmt="%3.3f", delimiter='\t')

############
### PLOT ###
############

## set figure sixe
plt.rcParams["figure.figsize"] = (16,12)

#set parameters
frameWidth = 1.5
plt.rcParams["axes.linewidth"] = frameWidth
plt.rcParams["axes.linewidth"] = frameWidth
plt.rcParams["xtick.major.width"] = frameWidth
plt.rcParams["ytick.major.width"] = frameWidth
plt.rcParams['xtick.major.pad'] = 20
plt.rcParams['ytick.major.pad'] = 20
plt.xticks(fontsize=25,weight='bold')
plt.yticks(fontsize=25,weight='bold')
plt.xlabel('Z axis [$\AA$]',fontsize=30,weight='bold')
plt.ylabel('Pore radius[$\AA$]',fontsize=30,weight='bold')

#create the color panel 
color=iter(cm.rainbow(np.linspace(0,1,nbin)))

for i in range(0,nbin) :
  #update color for the plot
  c=next(color)
  #label=str(print'{0}ns-{1}ns'.format(int(i*binwidth/100),int((i+1)*binwidth/100)))
  label=str("%ins-%ins" % (int(i*binwidth/100),int((i+1)*binwidth/100)))
  # plot the pore profile
  plt.plot(m[:,0], m[:,2*i+1],c=c, label=label)

plt.legend(fontsize=20)
plt.savefig("./IS-IVM-prof.png",bbox_inches='tight')
plt.show()

