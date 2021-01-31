import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
from matplotlib import rc

# Latex font rendering
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

R = 1000.0
L = 100.0e-3
C = 5.0e-9

lti_sys = signal.lti([R*L*C, L, 0], [R*L*C, L, R])

w, magn, phase = lti_sys.bode(n=1000)
f = w/(2*np.pi)

plt.figure()
plt.minorticks_on()
plt.title("Frequency response amplitude")
plt.semilogx(f, magn)
plt.xlabel(r"Frequency, $f$ [Hz]")
plt.ylabel(r"Magnitude response, $|H(f)|$ [dB]", fontsize=16)
plt.grid()
plt.savefig("amp_response.pdf")
plt.show()

plt.figure()
plt.title("Frequency response phase")
plt.semilogx(f, phase)
plt.xlabel(r"Frequency, $f$ [Hz]")
plt.ylabel(r"Phase angle, $\theta(f)$ [deg]", fontsize=16)
plt.grid()
plt.savefig("phase_response.pdf")
plt.show()
