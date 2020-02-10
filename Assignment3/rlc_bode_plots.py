import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
from matplotlib import rc
'''
# Latex font rendering
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
'''
R = 1000.0
L = 100.0E-6
C = 5.0E-9
RLC = R*L*C

def amp(f):
    return np.real(R / ( (R - RLC*(2 * np.pi * f)**2) + (2 * np.pi * f * L)**2 ) * \
           (R - RLC * (2 * np.pi * f)**2 - 2j * np.pi * f * L))

def theta(f):
    return np.arctan(2*np.pi*f * L / ((2*np.pi*f)**2 * RLC - R))

f = np.linspace(1E3, 1E6, 5001)

plt.figure()
plt.title("Amplitude")
plt.loglog(f, amp(f))
plt.xlabel(r"Frequency, $f$ / ms")
plt.ylabel(r"Amplitude, $u_2/u_1$", fontsize=16)
plt.grid()
plt.savefig("amp_response.pdf")
plt.show()

plt.figure()
plt.title("Phase response")
plt.semilogx(f, np.rad2deg(theta(f)))
plt.xlabel(r"Frequency, $f$ / ms")
plt.ylabel(r"Phase angle, $\theta(f)$", fontsize=16)
plt.grid()
plt.savefig("phase_response.pdf")
plt.show()
