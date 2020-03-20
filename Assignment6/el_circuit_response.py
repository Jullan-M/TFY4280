import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
from matplotlib import rc

# Latex font rendering
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

R1 = 10 # Ohm
R2 = 10 # Ohm
C1 = 10E-6 # Faraday
L1 = 100E-3 # Henry
L2 = 100E-3 # Henry

A = [[-R1/L1, 0 , -1/L1]
    ,[0, -R2/L2, -1/L2]
    ,[1/C1, 1/C1, 0]]

B = [[1/L1], [0], [0]]

C = [[0, -R2, 0]]

D = [[0]]

lti_system = signal.lti(A,B,C,D)

t, sys_impulse = signal.impulse(lti_system, N=1001)
sys_step = signal.step(lti_system, T=t)[1]
w, bode_mag, bode_phase = signal.bode(lti_system, n=1001)

plt.figure()
plt.title(f"System impulse response, $C={C1:.2e}$ F")
plt.plot(t, sys_impulse, c='k', linewidth=0.7)
plt.xlabel(r"Time, $t$ (s)", fontsize=16)
plt.ylabel(r"Impulse response, $h(t)$", fontsize=16)
plt.grid()
plt.savefig(f"impulse_response_E-6.pdf")
plt.show()

plt.figure()
plt.title(f"System step response, $C={C1:.2e}$ F")
plt.plot(t, sys_step, c='k', linewidth=0.7)
plt.xlabel(r"Time, $t$ (s)", fontsize=16)
plt.ylabel(r"Step response, $s(t)$", fontsize=16)
plt.grid()
plt.savefig(f"step_response_E-6.pdf")
plt.show()

plt.figure()
plt.title(f"Magnitude response, $C={C1:.2e}$ F")
plt.semilogx(w / (2*np.pi), bode_mag, c='k', linewidth=0.7)
plt.xlabel(r"Frequency, $f$ (Hz)", fontsize=16)
plt.ylabel(r"Gain (dB)", fontsize=16)
plt.grid()
plt.savefig(f"bode_mag_E-6.pdf")
plt.show()

plt.figure()
plt.title(f"Phase response, $C={C1:.2e}$ F")
plt.semilogx(w / (2*np.pi), bode_phase, c='k', linewidth=0.7)
plt.xlabel(r"Frequency, $f$ (Hz)", fontsize=16)
plt.ylabel(r"Phase, $|\theta(f)|$ (deg)", fontsize=16)
plt.grid()
plt.savefig(f"bode_phase_E-6.pdf")
plt.show()
