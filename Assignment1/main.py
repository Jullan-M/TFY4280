import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
from matplotlib import rc

# Latex font rendering
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

t_ = np.linspace(-8, 8, 501)

sig1 = np.heaviside(t_ + 5, 1) - np.heaviside(t_ - 5, 1)

plt.figure()
plt.title("Rectangular waveform")
#plt.plot(t_ , 0.5*(signal.square(0.1*np.pi*t_)+1))
plt.plot(t_, sig1)
plt.xlabel(r"Time, $t$ / ms")
plt.ylabel(r"Amplitude, $x(t)$", fontsize=16)
plt.grid()
plt.savefig("waveform_rect.pdf")
plt.show()


sig2 = (signal.sawtooth(0.4*np.pi*(t_ - 5/2), 0.5) + 1) \
       * (np.heaviside(t_ + 5/2, 1) - np.heaviside(t_ - 5/2, 1))

plt.figure()
plt.title("Triangular waveform")
plt.plot(t_ , sig2)
plt.xlim(left=-5, right=5)
plt.xlabel(r"Time, $t$ / ms")
plt.ylabel(r"Amplitude, $x(t)$", fontsize=16)
plt.grid()
plt.savefig("waveform_triang.pdf")
plt.show()

def gaussian(x, amp, width):
    sigma = np.sqrt(0.5*(width/2)**2/(1+ np.log(amp)))
    return amp*np.exp(-0.5*(x/sigma)**2)
t_gauss = np.linspace(-5,5, 501)
sig3 = gaussian(t_gauss, 7, 5)

plt.figure()
plt.title("Gaussian waveform")
plt.axhline(1/np.e, c="k", label=r"$y=1/e$")
plt.plot(t_gauss, sig3, label=r"Gaussian pulse")
plt.ylim(bottom=0)
plt.xlim(left=-5, right=5)
plt.xlabel(r"Time, $t$ / ms")
plt.ylabel(r"Amplitude, $x(t)$", fontsize=16)
plt.legend()
plt.grid()
plt.savefig("waveform_gauss.pdf")
plt.show()

n = 11
p_on = 2
p_off = 8
sig_k = 2 / (p_on + p_off)
sig_duty = p_on / (p_on + p_off)

t = np.linspace(- (p_on + p_off), n * (p_on + p_off), 501)

sig4 = 0.5*(signal.square(sig_k*np.pi*(t + p_on/2), duty=sig_duty)+1)
pwm4 = (np.heaviside(t + p_on, 1) - np.heaviside(t - n * (p_on + p_off) + p_off, 1))

plt.figure()
plt.title(r"Sequence of 11 rectangular pulses")
#plt.plot(t,  0.5*(signal.square(0.5*np.pi*t)+1), c="g")
plt.plot(t,  sig4 * pwm4, c="b", linewidth = 0.75)
#plt.plot(t,  pwm, c="r", linewidth = 0.75, linestyle='-.')
plt.xlim(left=t.min(), right=t.max())
plt.xlabel(r"Time, $t$ / ms")
plt.ylabel(r"Amplitude, $x(t)$", fontsize=16)
plt.grid()
plt.savefig("waveform_11rect.pdf")
plt.show()