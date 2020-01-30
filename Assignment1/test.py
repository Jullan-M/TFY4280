import numpy as np
from matplotlib import pyplot as plt

t = np.linspace(-7, 9, 501)
sig = 3 * np.heaviside(t + 6, 1) - np.heaviside(t - 3, 1) + np.heaviside(t - 6, 1) * (-2/3 * t + 4)

plt.figure()
plt.plot(t, sig)
plt.xlabel(r"Time, $t$ / ms")
plt.ylabel(r"Amplitude, $x(t)$", fontsize=16)
plt.grid()
plt.show()

t_ = 2 - t

plt.figure()
plt.plot(t_, sig)
plt.xlabel(r"Time, $t$ / ms")
plt.ylabel(r"Amplitude, $x(t)$", fontsize=16)
plt.grid()
plt.show()

t2 = np.linspace(-3, 3, 501)
sig2 = np.heaviside(t2, 1) * ( 3 + t2 ) - (t2 - 1) * np.heaviside(t2 - 1, 1) - 5 * np.heaviside(t2 - 2, 1)

plt.figure()
plt.plot(t2, sig2)
plt.xlabel(r"Time, $t$ / ms")
plt.ylabel(r"Amplitude, $x(t)$", fontsize=16)
plt.grid()
plt.show()

t3 = np.linspace(-5, 5, 501)
sig3 = (np.heaviside(t3 + 2, 1) - np.heaviside(t3 - 3, 1)) * (-3/5 * t3 + 4/5) \
    + (np.heaviside(t3 - 3, 1) - np.heaviside(t3 - 4, 1)) * (t3 - 4)

plt.figure()
plt.plot(t3, sig3)
plt.plot(t3, 0.5 * (sig3 + np.flip(sig3)), c='b')
plt.plot(t3, 0.5 * (sig3 - np.flip(sig3)), c='r')
plt.xlabel(r"Time, $t$ / ms")
plt.ylabel(r"Amplitude, $x(t)$", fontsize=16)
plt.grid()
plt.show()