import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
from matplotlib import rc

# Latex font rendering
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

t_ = np.linspace(-8, 8, 1601)

sig1 = np.heaviside(t_ + 5, 1) - np.heaviside(t_ - 5, 1)
sig1_ft = np.fft.fft(sig1)
sig1_freq = np.fft.fftfreq(len(t_), d = 0.001)

plt.figure()
plt.title("$\mathcal{F}$-transform of rectangular waveform")
#plt.plot(t_ , 0.5*(signal.square(0.1*np.pi*t_)+1))
plt.plot(sig1_freq, np.abs(sig1_ft))
plt.xlabel(r"Frequency, $f$ / Hz")
plt.ylabel(r"$\mathcal{F}$-amplitude, $X(t)$", fontsize=16)
plt.grid()
plt.savefig("rect_f-transform.pdf")
plt.show()



sig2 = (signal.sawtooth(0.4*np.pi*(t_ - 5/2), 0.5) + 1) \
       * (np.heaviside(t_ + 5/2, 1) - np.heaviside(t_ - 5/2, 1))
sig2_ft = np.fft.fft(sig2)

plt.figure()
plt.title("$\mathcal{F}$-transform of triangular waveform")
plt.plot(sig1_freq , np.abs(sig2_ft))
plt.xlabel(r"Frequency, $f$ / Hz")
plt.ylabel(r"$\mathcal{F}$-amplitude, $X(t)$", fontsize=16)
plt.grid()
plt.savefig("triang_f-transform.pdf")
plt.show()

def gaussian(x, amp, width):
    sigma = np.sqrt(0.5*(width/2)**2/(1+ np.log(amp)))
    return amp*np.exp(-0.5*(x/sigma)**2)
t_gauss = np.linspace(-5,5, 1001)
sig3 = gaussian(t_gauss, 7, 5)
sig3_ft = np.fft.fft(sig3)
sig3_freq = np.fft.fftfreq(len(t_gauss), d=0.001)

plt.figure()
plt.title("$\mathcal{F}$-transform of gaussian waveform")
plt.plot(sig3_freq, np.abs(sig3_ft))
plt.xlabel(r"Frequency, $f$ / Hz")
plt.ylabel(r"$\mathcal{F}$-amplitude, $X(t)$", fontsize=16)
plt.grid()
plt.savefig("gauss_f-tranform.pdf")
plt.show()

n = 11
p_on = 2
p_off = 8
sig_k = 2 / (p_on + p_off)
sig_duty = p_on / (p_on + p_off)

t = np.linspace(- (p_on + p_off), n * (p_on + p_off) + 5, 1251)

sig4 = 0.5*(signal.square(sig_k*np.pi*(t + p_on/2), duty=sig_duty)+1)
pwm4 = (np.heaviside(t + p_on, 1) - np.heaviside(t - n * (p_on + p_off) + p_off, 1))

sig4_ft = np.fft.fft(sig4 * pwm4)
sig4_freq = np.fft.fftfreq(len(t), d=0.001)

plt.figure()
plt.title(r"$\mathcal{F}$-transform of 11 rectangular pulses")
plt.plot(sig4_freq,  np.abs(sig4_ft), c="b", linewidth = 0.75)
plt.xlabel(r"Frequency, $f$ / Hz")
plt.ylabel(r"$\mathcal{F}$-amplitude, $X(t)$", fontsize=16)
plt.grid()
plt.savefig("11rect_f-tranform.pdf")
plt.show()
