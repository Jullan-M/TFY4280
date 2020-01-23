__author__ = 'Jullan'
# -*- coding: utf-8 -*-
#Made by Jullan
import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
from matplotlib import rc

rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)


t_ = np.linspace(-25,15, 501)

plt.figure()
plt.title("Rectangular waveform")
plt.plot(t_ , 0.5*(signal.square(0.1*np.pi*t_)+1))
plt.xlabel(r"Time, $t$ / ms")
plt.ylabel(r"Amplitude, $x(t)$", fontsize=16)
plt.grid()
plt.savefig("waveform_rect.pdf")
plt.show()

plt.figure()
plt.title("Triangular waveform")
plt.plot(t_ , signal.sawtooth(0.4*np.pi*t_, 0.5) + 1)
plt.xlabel(r"Time, $t$ / ms")
plt.ylabel(r"Amplitude, $x(t)$", fontsize=16)
plt.grid()
plt.savefig("waveform_triang.pdf")
plt.show()

def gaussian(x, mu, sigma):
    return np.exp(-0.5*((x-mu)/sigma)**2) / np.sqrt(2.0*np.pi) / sigma

t_gauss = np.linspace(-5,5, 501)
plt.figure()
plt.title("Gaussian waveform")
plt.axhline(1/np.e, c="k", label=r"$y=1/e$")
plt.plot(t_gauss, 7*gaussian(t_gauss, 0, 1.34329), label=r"Gaussian pulse")
plt.ylim(bottom=0)
plt.xlim(left=-5, right=5)
plt.xlabel(r"Time, $t$ / ms")
plt.ylabel(r"Amplitude, $x(t)$", fontsize=16)
plt.legend()
plt.grid()
plt.savefig("waveform_gauss.pdf")
plt.show()


t = np.linspace(-20,60, 501)
p = 4
pwm_k = 2 / (p * 10.5 + 10)
pwm_duty = p * 11 / (p * 11 + 10)
sig_k = 2 / p
pwm = 0.5*(signal.square(pwm_k*np.pi*t,duty=pwm_duty)+1)
sig = 0.5*(signal.square(sig_k*np.pi*t)+1)

plt.figure()
plt.title(r"Sequence of 11 rectangular pulses")
#plt.plot(t,  0.5*(signal.square(0.5*np.pi*t)+1), c="g")
plt.plot(t,  sig * pwm, c="b", linewidth = 0.75)
plt.plot(t,  pwm, c="r", linewidth = 0.75, linestyle='-.')
plt.xlim(left=t.min(), right=t.max())
plt.xlabel(r"Time, $t$ / ms")
plt.ylabel(r"Amplitude, $x(t)$", fontsize=16)
plt.grid()
plt.savefig("waveform_11rect.pdf")
plt.show()