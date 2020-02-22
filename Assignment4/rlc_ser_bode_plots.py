import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc

# Latex font rendering
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

R = 1000.0

L1 = 0.5
C1 = 500E-12
wN1 = 1 / np.sqrt(L1 * C1)
z1 = R/2 * np.sqrt(C1/L1)

L2 = 0.01125
C2 = 22.51E-9


def rlc_H(w):
    return (4 * (z1/wN1)**2 * w**2
            + 1j * 2 * (z1/wN1) * (w - w**3 / wN1**2)) / \
           (1 + (w/wN1)**4 + (4*(z1/wN1)**2 - 2/wN1**2)*w**2)

def bw_H(w):
    return 1 / (1 - L2*C2*w**2 + 1j * R*C2*w)

def theta(w, H):
    H = H(w)
    return np.arctan(np.imag(H), np.real(H))

f1 = np.logspace(3, 5, 1001)
magn_resp1 = np.abs(rlc_H(2*np.pi*f1))

plt.figure()
plt.title("Frequency response amplitude")
plt.loglog(f1, magn_resp1)
plt.xlabel(r"Frequency, $f$ / Hz")
plt.ylabel(r"Amplitude, $|H(f)|$", fontsize=16)
plt.grid()
plt.savefig("rlc_amp.pdf")
plt.show()

plt.figure()
plt.title("Frequency response phase")
plt.semilogx(f1, np.rad2deg(theta(2*np.pi*f1, rlc_H)))
plt.xlabel(r"Frequency, $f$ / Hz")
plt.ylabel(r"Phase angle, $\theta(f)$", fontsize=16)
plt.grid()
plt.savefig("rlc_response.pdf")
plt.show()

f2 = np.logspace(2, 5, 1001)
magn_resp2 = np.abs(bw_H(2*np.pi*f2))

plt.figure()
plt.title("Frequency response amplitude")
plt.loglog(f2, magn_resp2)
plt.plot([1E2, 1E4], [1/np.sqrt(2), 1/np.sqrt(2)], linestyle='--', c='r')
plt.plot([1E4, 1E4], [magn_resp2.min(), 1/np.sqrt(2)], linestyle='--', c='r')
plt.xlim(left = 1E2)
plt.ylim(bottom=magn_resp2.min())
plt.xlabel(r"Frequency, $f$ / Hz")
plt.ylabel(r"Amplitude, $|H(f)|$", fontsize=16)
plt.grid()
plt.savefig("butterworth_amp.pdf")
plt.show()

plt.figure()
plt.title("Frequency response phase")
plt.semilogx(f2, np.rad2deg(theta(2*np.pi*f2, bw_H)))
plt.xlabel(r"Frequency, $f$ / Hz")
plt.ylabel(r"Phase angle, $\theta(f)$", fontsize=16)
plt.grid()
plt.savefig("butterworth_phase.pdf")
plt.show()
