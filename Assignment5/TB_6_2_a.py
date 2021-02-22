import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
from matplotlib import rc

# Latex font rendering
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)


T = 0.040
p_on = T/2
p_off = T/2
sig_omega = 2*np.pi / (p_on + p_off)
sig_duty = p_on / (p_on + p_off)

x = lambda t: 0.5*signal.square(sig_omega*(t + p_on/2), duty=sig_duty) + 0.5
y = lambda t: 0.5 + 2/np.pi * np.cos(50*np.pi*t) -2/(3*np.pi)*np.cos(150*np.pi*t)


t = np.linspace(-0.06, 0.06, 501)

plt.figure()
plt.title(r"Input signal $x(t)$ vs output signal $y(t)$")
plt.plot(t, x(t), label='$x(t)$', c='b', linewidth = 0.8)
plt.plot(t, y(t), label='$y(t)$', c='r', linewidth = 0.8)
plt.legend()
plt.xlabel(r"Time, $t$ [s]", fontsize=16)
plt.ylabel(r"Amplitude", fontsize=16)
plt.tight_layout()
plt.legend(fancybox=True, framealpha=0)
plt.grid()
plt.savefig("TB_6_2_a.pdf")
plt.show()