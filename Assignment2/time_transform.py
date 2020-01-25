__author__ = 'Jullan'
# -*- coding: utf-8 -*-
#Made by Jullan

import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
from matplotlib import rc
'''
# Latex font rendering
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
'''

t = np.linspace(-3,3, 501)
y = 1 - (t+1) * np.heaviside(t + 1, 0.5) + (3*t-3) * np.heaviside(t - 1, 0.5) \
    -(2*t-4) * np.heaviside(t - 2, 0.5)

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)

ax1.plot(t, y)
ax1.grid(True)
ax1.set_ylabel(r'$y(t)$')
ax1.set_title(r'$y(t) = x(t)$')
#ax1.margins(0, 0.1)

ax2.plot(4*t + 3, y)
ax2.grid(True)
ax2.set_ylabel(r'$y(t)$')
ax2.set_title(r'$y(t) = x(4t+3)$')
#ax2.margins(0, 0.1)

ax3.plot(-3*t+2, y)
ax3.grid(True)
ax3.set_ylabel(r'$y(t)$')
ax3.set_title(r'$y(t) = x(-3t+2)$')
#ax3.margins(0, 0.1)


plt.xlabel(r"$t$", fontsize=16)


fig.tight_layout()

#plt.savefig("waveform_rect.pdf")
fig.show()