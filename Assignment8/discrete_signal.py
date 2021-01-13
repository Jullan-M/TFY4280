import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
from matplotlib import rc

# Latex font rendering
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

num = [1, -0.4, 0]
denum = [1, -1, 0.6]

sys = signal.dlti(num, denum)
t_imp, y_imp = sys.impulse(n=20)
t_step, y_step = sys.step(n=20)

plt.figure()
plt.title(f"Step response")
plt.stem(t_step, np.squeeze(y_step))
plt.xlabel(r"Discrete time, $n$", fontsize=16)
plt.ylabel(r"Output, $y[n]$", fontsize=16)
plt.grid()
plt.xticks(np.arange(20))
plt.savefig(f"step_response.pdf")
plt.show()

plt.figure()
plt.title(f"Impulse response")
plt.stem(t_step, np.squeeze(y_imp))
plt.xlabel(r"Discrete time, $n$", fontsize=16)
plt.ylabel(r"Output, $y[n]$", fontsize=16)
plt.grid()
plt.xticks(np.arange(20))
plt.savefig(f"impulse_response.pdf")
plt.show()