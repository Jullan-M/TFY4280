import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
from matplotlib import rc

# Latex font rendering
rc('font', **{'family': 'serif', 'serif': ['Palatino']})
rc('text', usetex=True)

num = [0.0513, 0.1026, 0.0513]
denum = [1, -1.386, 0.5913]

n = 20
dt = 0.5e-3
sys = signal.dlti(num, denum, dt=dt)

t_imp, y_imp = sys.impulse(n=n)
t_step, y_step = sys.step(n=n)
w_b, H = sys.freqresp(n=1000)

print(np.abs(H[0]), np.abs(H[200]), np.abs(H[400]))

plt.figure()
plt.title(f"Step response")
plt.stem(t_step, np.squeeze(y_step), use_line_collection=True)
plt.xlabel(r"Time, $t$ (s)", fontsize=16)
plt.ylabel(r"Output, $y[n]$", fontsize=16)
plt.grid()
plt.xticks(t_imp[::2])
plt.savefig(f"dig_step_response.pdf")
plt.show()

plt.figure()
plt.title(f"Impulse response")
plt.stem(t_step, np.squeeze(y_imp), use_line_collection=True)
plt.xlabel(r"Time, $t$ (s)", fontsize=16)
plt.ylabel(r"Output, $y[n]$", fontsize=16)
plt.grid()
plt.xticks(t_step[::2])
plt.savefig(f"dig_impulse_response.pdf")
plt.show()

plt.figure()
plt.title(f"Magnitude response")
plt.plot(w_b / (2*np.pi) * 2000, np.abs(H), c='b', linewidth=0.75)
plt.xlabel(r"Frequency, $f$ (Hz)", fontsize=16)
plt.ylabel(r"Gain", fontsize=16)
plt.grid()
plt.savefig(f"dig_amplitude_response.pdf")
plt.show()
