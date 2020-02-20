import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc

# Latex font rendering
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

R = 1000.0
L = 100.0E-6
C = 5.0E-9
RLC = R*L*C

def amp(w):
    return np.real(R / ( (R - RLC * w**2) + (w * L)**2 ) * \
           (R - RLC * w**2 - 1j * w * L))

def theta(w):
    return np.arctan(w * L / (w**2 * RLC - R))

f = np.logspace(3, 6, 1001)


plt.figure()
plt.title("Amplitude")
plt.loglog(f, amp(2*np.pi*f))
plt.xlabel(r"Frequency, $f$ / ms")
plt.ylabel(r"Amplitude, $u_2/u_1$", fontsize=16)
plt.grid()
plt.savefig("amp_response.pdf")
plt.show()

plt.figure()
plt.title("Phase response")
plt.semilogx(f, np.rad2deg(theta(2*np.pi*f)))
plt.xlabel(r"Frequency, $f$ / ms")
plt.ylabel(r"Phase angle, $\theta(f)$", fontsize=16)
plt.grid()
plt.savefig("phase_response.pdf")
plt.show()
