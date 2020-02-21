import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc

# Latex font rendering
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

R = 1000.0
L = 0.5
C = 500E-12

def tranfer_func(w):
    return 1j * R * C * w / (1 - L*C*w**2 + 1j * R*C*w)

def theta(w):
    H = tranfer_func(w)
    return np.arctan(np.imag(H), np.real(H))

f = np.logspace(3, 5, 1001)


plt.figure()
plt.title("Frequency response amplitude")
plt.loglog(f, np.abs(tranfer_func(2*np.pi*f)))
plt.xlabel(r"Frequency, $f$ / Hz")
plt.ylabel(r"Amplitude, $|H(f)|$", fontsize=16)
plt.grid()
plt.savefig("amp_response.pdf")
plt.show()

plt.figure()
plt.title("Frequency response phase")
plt.semilogx(f, np.rad2deg(theta(2*np.pi*f)))
plt.xlabel(r"Frequency, $f$ / Hz")
plt.ylabel(r"Phase angle, $\theta(f)$", fontsize=16)
plt.grid()
plt.savefig("phase_response.pdf")
plt.show()
