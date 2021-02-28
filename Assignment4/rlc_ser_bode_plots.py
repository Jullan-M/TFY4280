import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
from matplotlib import rc

# Latex font rendering
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

R = 1000.0
L1 = 0.5
C1 = 500e-12

L2 = 0.1/np.sqrt(2)
C2 = np.sqrt(2)*1e-7

rlc_lti = signal.lti([0, R*C1, 0], [L1*C1, R*C1, 1])
bw_lti = signal.lti([0,0,1], [L2*C2, R*C2, 1])

w1 = 2*np.pi*np.logspace(3,5,1001)
w1, magn_rlc, phase_rlc = rlc_lti.bode(w1)
w2 = np.logspace(2,5,1001)
w2, magn_bw, phase_bw = bw_lti.bode(w2)

plt.figure()
plt.title("Frequency response amplitude")
plt.semilogx(w1/(2*np.pi), magn_rlc)
plt.xlabel(r"Frequency, $f$ [Hz]")
plt.ylabel(r"Amplitude, $|H(f)|$ [dB]", fontsize=16)
plt.grid()
plt.savefig("rlc_amp.pdf")
plt.show()

plt.figure()
plt.title("Frequency response phase")
plt.semilogx(w1/(2*np.pi), phase_rlc)
plt.xlabel(r"Frequency, $f$ [Hz]")
plt.ylabel(r"Phase angle, $\theta(f)$ [deg]", fontsize=16)
plt.grid()
plt.savefig("rlc_response.pdf")
plt.show()

plt.figure()
plt.title("Frequency response amplitude")
plt.semilogx(w2, magn_bw)
plt.plot([1E2, 1E4], [-3, -3], linestyle='--', c='r')
plt.plot([1E4, 1E4], [magn_bw.min(), -3], linestyle='--', c='r')
plt.xlim(left = 1E2)
plt.ylim(bottom=magn_bw.min())
plt.xlabel(r"Angular frequency, $\omega$ [rad/s]")
plt.ylabel(r"Amplitude, $|H(\omega)|$ [dB]", fontsize=16)
plt.grid()
plt.savefig("butterworth_amp.pdf")
plt.show()

plt.figure()
plt.title("Frequency response phase")
plt.semilogx(w2, phase_bw)
plt.xlabel(r"Angular frequency, $\omega$ [rad/s]")
plt.ylabel(r"Phase angle, $\theta(\omega)$ [deg]", fontsize=16)
plt.grid()
plt.savefig("butterworth_phase.pdf")
plt.show()
