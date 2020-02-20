import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
from matplotlib import rc

# Latex font rendering
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

t_ = np.linspace(-50, 50, 5001)
d_ = 0.100 / 5000

sig1 = np.heaviside(t_ + 5, 1) - np.heaviside(t_ - 5, 1)
sig1_ft = np.fft.fft(sig1) * d_
sig1_freq = 2 * np.pi * np.fft.fftfreq(len(t_), d = d_)

plt.figure()
plt.title("$\mathcal{F}$-transform of a rectangular waveform")
plt.plot(sig1_freq, np.abs(sig1_ft), c="b")
plt.xlim(left = 0, right = 4000)
plt.xlabel(r"Angular frequency, $\omega$ / Hz")
plt.ylabel(r"Magnitude spectrum, $|X(\omega)|$", fontsize=16)
plt.grid()
plt.savefig("rect_f-transform.pdf")
plt.show()



sig2 = (signal.sawtooth(0.4*np.pi*(t_ - 5/2), 0.5) + 1) \
       * (np.heaviside(t_ + 5/2, 1) - np.heaviside(t_ - 5/2, 1))
sig2_ft = np.fft.fft(sig2) * d_

plt.figure()
plt.title("$\mathcal{F}$-transform of a triangular waveform")
plt.plot(sig1_freq , np.abs(sig2_ft), c="b")
plt.xlim(left = 0, right = 7500)
plt.xlabel(r"Angular frequency, $\omega$ / Hz")
plt.ylabel(r"Magnitude spectrum, $|X(\omega)|$", fontsize=16)
plt.grid()
plt.savefig("triang_f-transform.pdf")
plt.show()

def gaussian(x, amp, width):
    sigma = np.sqrt(0.5*(width/2)**2/(1+ np.log(amp)))
    print('sigma = ', sigma)
    return amp*np.exp(-0.5*(x/sigma)**2)
t_gauss = np.linspace(-20,20, 4001)
d_gauss = 0.040 / 4000

sig3 = gaussian(t_gauss, 7, 5)
sig3_ft = np.fft.fft(sig3) * d_gauss
sig3_freq = 2 * np.pi * np.fft.fftfreq(len(t_gauss), d=d_gauss)

plt.figure()
plt.title("$\mathcal{F}$-transform of a gaussian waveform")
plt.plot(sig3_freq, np.abs(sig3_ft), c="b")
plt.xlim(left = 0, right = 5000)
plt.xlabel(r"Angular frequency, $\omega$ / Hz")
plt.ylabel(r"Magnitude spectrum, $|X(\omega)|$", fontsize=16)
plt.grid()
plt.savefig("gauss_f-tranform.pdf")
plt.show()

n = 11
p_on = 2
p_off = 8
sig_k = 2 / (p_on + p_off)
sig_duty = p_on / (p_on + p_off)

t_seq = np.linspace(- (p_on + p_off) - 100, n * (p_on + p_off) + 100, 16001)
d_seq = 0.320 / 16000

sig4 = 0.5*(signal.square(sig_k*np.pi*(t_seq + p_on/2), duty=sig_duty)+1)
pwm4 = (np.heaviside(t_seq + p_on, 1) - np.heaviside(t_seq - n * (p_on + p_off) + p_off, 1))

sig4_ft = np.fft.fft(sig4 * pwm4) * d_seq
sig4_freq = 2*np.pi*np.fft.fftfreq(len(t_seq), d=d_seq)

plt.figure()
plt.title(r"$\mathcal{F}$-transform of 11 rectangular pulses")
plt.plot(sig4_freq,  np.abs(sig4_ft), c="b", linewidth = 0.75)
plt.xlim(left = 0, right = 5000)
plt.xlabel(r"Angular frequency, $\omega$ / Hz")
plt.ylabel(r"Magnitude spectrum, $|X(\omega)|$", fontsize=16)
plt.grid()
plt.savefig("11rect_f-tranform.pdf")
plt.show()
