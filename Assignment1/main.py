__author__ = 'Jullan'
# -*- coding: utf-8 -*-
#Made by Jullan
import numpy as np
from scipy import signal
from matplotlib import pyplot as plt

t_ = np.linspace(-20,20, 501)

plt.figure()
plt.plot(t_ , 0.5*(signal.square(0.1*np.pi*t_)+1))
plt.xlabel(r"Time, $t$ / ms")
plt.ylabel(r"Amplitude, $x(t)$", fontsize=16)
plt.grid()
#plt.savefig(".pdf")
plt.show()

plt.figure()
plt.plot(t_ , signal.sawtooth(0.4*np.pi*t_, 0.5) + 1)
plt.xlabel(r"Time, $t$ / ms")
plt.ylabel(r"Amplitude, $x(t)$", fontsize=16)
plt.grid()
#plt.savefig(".pdf")
plt.show()

plt.figure()
plt.plot(t_, 7*signal.gausspulse(0.4*np.pi*t_, 1 / np.e))
plt.xlabel(r"Time, $t$ / ms")
plt.ylabel(r"Amplitude, $x(t)$", fontsize=16)
plt.grid()
#plt.savefig(".pdf")
plt.show()


t = np.linspace(-20,60, 501)
p = 4
pwm_k = 2 / (p * 10.5 + 10)
pwm_duty = p * 11 / (p * 11 + 10)
sig_k = 2 / p
pwm = 0.5*(signal.square(pwm_k*np.pi*t,duty=pwm_duty)+1)
sig = 0.5*(signal.square(sig_k*np.pi*t)+1)

plt.figure()
#plt.plot(t,  0.5*(signal.square(0.5*np.pi*t)+1), c="g")
plt.plot(t,  sig * pwm, c="b", linewidth = 0.75)
plt.plot(t,  pwm, c="r", linewidth = 0.75, linestyle='-.')
plt.xlim(left=t.min(), right=t.max())
plt.xlabel(r"Time, $t$ / ms")
plt.ylabel(r"Amplitude, $x(t)$", fontsize=16)
plt.grid()
#plt.savefig(".pdf")
plt.show()