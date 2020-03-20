import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
from matplotlib import rc

# Latex font rendering
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

R1 = 100 # Ohm
R2 = 100 # Ohm
C1 = 0.01 # Faraday
L1 = 2 # Henry
L2 = 5 # Henry

A = [[-R1/L1, 0 , -1/L1]
    ,[0, -R2/L2, -1/L2]
    ,[1/C1, 1/C1, 0]]

B = [[1/L1], [0], [0]]

C = [[0, -R2, 0]]

D = [[0]]

lti_system1 = signal.lti(A,B,C,D)
num = [1000]
denom = [1, 70, 1070, 2000]
lti_system2 = signal.lti(num, denom)

w1, bode_mag1, bode_phase1 = signal.bode(lti_system1, n=1001)
w2, bode_mag2, bode_phase2 = signal.bode(lti_system2, n=1001)

plt.figure()
plt.title(f"Magnitude response")
plt.semilogx(w1 / (2*np.pi), bode_mag1, c='b', linewidth=1, label='State model')
plt.semilogx(w2 / (2*np.pi), bode_mag2, c='r', linewidth=1, linestyle='--', label='"Traditional"')
plt.xlabel(r"Frequency, $f$ (Hz)", fontsize=16)
plt.ylabel(r"Gain (dB)", fontsize=16)
plt.grid()
plt.legend()
plt.savefig(f"steady_state_freq_magn.pdf")
plt.show()

plt.figure()
plt.title(f"Phase response")
plt.semilogx(w1 / (2*np.pi), bode_phase1, c='b', linewidth=0.7, label='State model')
plt.semilogx(w2 / (2*np.pi), bode_phase2, c='r', linewidth=0.7, linestyle='--', label='"Traditional"')
plt.xlabel(r"Frequency, $f$ (Hz)", fontsize=16)
plt.ylabel(r"Phase, $|\theta(f)|$ (deg)", fontsize=16)
plt.grid()
plt.legend()
plt.savefig(f"steady_state_freq_phase.pdf")
plt.show()
