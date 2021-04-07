import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
from matplotlib import rc

# Latex font rendering
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

num = [1, -0.4, 0]
denum = [1,-1, 0.6]

n = 20
dt = 0.5e-3
sys = signal.dlti(num, denum, dt=dt)

t_imp, y_imp = sys.impulse(n=n)
t_step, y_step = sys.step(n=n)
w_b, H = sys.freqresp(n=1000)

print("Impulse response")
print(y_imp)

print("Step response")
print(y_step)

plt.figure()
plt.title(f"Step response")
plt.stem(t_step, np.squeeze(y_step))
plt.xlabel(r"Time, $t$ (s)", fontsize=16)
plt.ylabel(r"Output, $y[n]$", fontsize=16)
plt.grid()
plt.xticks(t_imp[::2])
plt.savefig(f"dig_step_response.pdf")
plt.show()

plt.figure()
plt.title(f"Impulse response")
plt.stem(t_step, np.squeeze(y_imp))
plt.xlabel(r"Time, $t$ (s)", fontsize=16)
plt.ylabel(r"Output, $y[n]$", fontsize=16)
plt.grid()
plt.xticks(t_step[::2])
plt.savefig(f"dig_impulse_response.pdf")
plt.show()