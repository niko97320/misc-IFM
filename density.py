# this script plots the density distribution of a time series
# using the KDE method
# Nicolas Matin 19/09/16

from matplotlib import pyplot as plt
import numpy as np
from scipy.stats.kde import gaussian_kde
import sys

inp=sys.argv[1]
col=int(sys.argv[2])

print "Reading data from %s" %inp
print "Reading column %i" %col

data = np.genfromtxt(inp, usecols=col)
kde = gaussian_kde(data)
dist_space = np.linspace( min(data), max(data), 100)
plt.plot(dist_space, kde(dist_space), color=np.random.rand(3,1) , lw=3)
plt.show()
