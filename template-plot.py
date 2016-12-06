#!/usr/bin/env python
#-*-encoding: utf-8-*-

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
x=np.genfromtxt("data.txt")

ax.plot(x[:,0], x[:,1], marker='o', color='black')

ax.grid()

ax.set_xlabel("title1")
ax.set_ylabel("title2")

fig.savefig("plot.png", dpi=300)
