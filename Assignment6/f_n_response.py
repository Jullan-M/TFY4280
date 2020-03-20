import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc

# Latex font rendering
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

def yext(t):
    return np.heaviside(t, 0)*(1+np.exp(-3*t) - 2*np.exp(-2*t))

def yint(t):
    return -2*np.heaviside(t, 0)*np.e**(-2*t)

t = np.linspace(0, 10, 1001)

plt.figure()
plt.title("System output")
plt.plot(t, yext(t), c='r', label=r'Natural response, $y_{ext}(t)$')
plt.plot(t, yint(t), c='b', label=r'Forced response, $y_{int}(t)$')
plt.plot(t, yext(t) + yint(t), c='k', label=r'System response, $y(t)$', linestyle='--')
plt.xlabel(r"Time, $t$ (s)", fontsize=16)
plt.ylabel(r"Amplitude, $y(t)$", fontsize=16)
plt.grid()
plt.legend()
plt.savefig("system_output.pdf")
plt.show()