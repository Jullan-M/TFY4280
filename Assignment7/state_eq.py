import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
from matplotlib import rc

# Latex font rendering
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)


# NOTE: Array elements should always be FLOATs, not INTs! Otherwise this does not work.
A = [[-6.,-5.],[1.,0.]]
B = [[0.], [2.]]
C = [[1., 1.]]
D = [[2.]]

x0 = [1., 0.]
t = np.linspace(0, 3, 1001)

sys = signal.lti(A,B,C,D)
t1, yo = sys.step(x0, t, 1001)

plt.figure()
plt.title(f"System output")
plt.plot(t, yo, c='b', linewidth=0.75)
plt.plot(t, yo, c='b', linewidth=1, label='LSIM')
plt.plot(t, 12/5 + 3/5*np.exp(-5*t), c='r', linewidth=0.75, linestyle='--', label='Result from b)')
plt.xlabel(r"Time, $t$ (s)", fontsize=16)
plt.ylabel(r"Output, $y(t)$", fontsize=16)
plt.legend()
plt.ylim(2,3)
plt.grid()
plt.savefig(f"system_output.pdf")
plt.show()