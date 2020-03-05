import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
from matplotlib import rc

# Latex font rendering
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

def plot_signal(t, sig, range, name):
    plt.figure()
    plt.title(name)
    plt.plot(t , sig)
    plt.xlim(left=range[0], right=range[1])
    plt.xlabel(r"Time, $t$ / ms")
    plt.ylabel(r"Amplitude, $x(t)$", fontsize=16)
    plt.grid()

t = np.linspace(-70,70, 1401)

name1 = "Rectangular waveform"
sig1 = np.heaviside(t + 5, 1) - np.heaviside(t - 5, 1)

name2 = "Triangular waveform"
sawt_sig = 0.5*(signal.sawtooth(4/15*np.pi*t, 0) + 1)
sawt_pwm = np.heaviside(t, 1) - np.heaviside(t - 7.5, 1)
sig2 = sawt_pwm * sawt_sig

name3 = "Gaussian waveform"
def gaussian(x, amp, width):
    sigma = np.sqrt(0.5*(width/2)**2/(1+ np.log(amp)))
    return amp*np.exp(-0.5*(x/sigma)**2)

sig3 = gaussian(t, 1, 10)

name4 = "Sequence of 11 rectangular pulses"
sig_k = 0.2
rect_pwm = np.heaviside(t + 54, 1) - np.heaviside(t - 55, 1)
rect_sig = 0.5*(signal.square(sig_k*np.pi*(t+1.5), duty=3/10)+1)
sig4 = rect_pwm * rect_sig


sig1_sig1 = np.convolve(sig1, sig1) / 10000
sig1_sig2 = np.convolve(sig1, sig2) / 10000
sig3_sig4 = np.convolve(sig3, sig4) / 10000
sig2_sig4 = np.convolve(sig2, sig4) / 10000

t_ = np.linspace(-140,140, 2801)

plot_signal(t_, sig1_sig1, [-12,12], "Signal 1 convolved with signal 1")
plt.ylabel(r"Convolution area", fontsize=16)
plt.savefig("sig1_sig1.pdf")
plt.show()

plot_signal(t_, sig1_sig2, [-8,15], "Signal 1 convolved with signal 2")
plt.ylabel(r"Convolution area", fontsize=16)
plt.savefig("sig1_sig2.pdf")
plt.show()

plot_signal(t_, sig3_sig4, [-70,70], "Signal 3 convolved with signal 4")
plt.ylabel(r"Convolution area", fontsize=16)
plt.savefig("sig3_sig4.pdf")
plt.show()

plot_signal(t_, sig2_sig4, [-60,60], "Signal 2 convolved with signal 4")
plt.ylabel(r"Convolution area", fontsize=16)
plt.savefig("sig2_sig4.pdf")
plt.show()