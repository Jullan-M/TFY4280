__author__ = 'Jullan'
# -*- coding: utf-8 -*-
#Made by Jullan

import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
from matplotlib import rc

# Latex font rendering
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

t_ = np.linspace(-10, 10, 501)


plt.figure()
plt.title("Rectangular waveform")
plt.plot(t_ , np.heaviside(t_ + 5, 1) - np.heaviside(t_ - 5, 1))
plt.xlabel(r"Time, $t$ / ms")
plt.ylabel(r"Amplitude, $x(t)$", fontsize=16)
plt.grid()
#plt.savefig("waveform_rect.pdf")
plt.show()

sawt_sig = 0.5*(signal.sawtooth(4/15*np.pi*t_, 0) + 1)
sawt_pwm = np.heaviside(t_, 1) - np.heaviside(t_ - 7.5, 1)

plt.figure()
plt.title("Triangular waveform")
plt.plot(t_ , sawt_pwm * sawt_sig)
plt.xlabel(r"Time, $t$ / ms")
plt.ylabel(r"Amplitude, $x(t)$", fontsize=16)
plt.grid()
#plt.savefig("waveform_triang.pdf")
plt.show()

def gaussian(x, amp, width):
    sigma = np.sqrt(0.5*(width/2)**2/(1+ np.log(amp)))
    return amp*np.exp(-0.5*(x/sigma)**2)

t_gauss = np.linspace(-20,20, 501)
plt.figure()
plt.title("Gaussian waveform")
plt.axhline(1/np.e, c="k", label=r"$y=1/e$")
plt.plot(t_gauss, gaussian(t_gauss, 1, 10), label=r"Gaussian pulse")
plt.ylim(bottom=0)
plt.xlabel(r"Time, $t$ / ms")
plt.ylabel(r"Amplitude, $x(t)$", fontsize=16)
plt.legend()
plt.grid()
#plt.savefig("waveform_gauss.pdf")
plt.show()


t = np.linspace(-60,60, 501)
sig_k = 0.2


pwm = np.heaviside(t + 54, 1) - np.heaviside(t - 55, 1)
sig = 0.5*(signal.square(sig_k*np.pi*(t+1.5), duty=3/10)+1)

plt.figure()
plt.title(r"Sequence of 11 rectangular pulses")
#plt.plot(t,  0.5*(signal.square(0.5*np.pi*t)+1), c="g")
plt.plot(t,  pwm*sig, c="b", linewidth = 0.75)
#plt.plot(t,  pwm, c="r", linewidth = 0.75, linestyle='-.')
plt.xlim(left=t.min(), right=t.max())
plt.xlabel(r"Time, $t$ / ms")
plt.ylabel(r"Amplitude, $x(t)$", fontsize=16)
plt.grid()
#plt.savefig("waveform_11rect.pdf")
plt.show()