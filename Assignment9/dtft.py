import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
from matplotlib import rc

# Latex font rendering
rc('font', **{'family': 'serif', 'serif': ['Palatino']})
rc('text', usetex=True)

num = [0, 0.25, 0.5, 0.25]
denum = [1, 0, 0, 0]

sys = signal.dlti(num, denum)
n = np.arange(-14, 15)

a = 0.5
# dlsim method
x = a**n * np.heaviside(n, 1)
td, yd = sys.output(x, n)

# Convolve method
h = 0.25*(n == 1)+0.5*(n == 2)+0.25*(n == 3)
y_conv = np.convolve(h, x, 'same')[14:]

# Plot a = 0.5
plt.figure()
plt.title(f"System output, $a=0.5$")
plt.stem(td, x[14:], label="Input, $x[n]$",
         use_line_collection=True, markerfmt="bo")
plt.stem(td, np.squeeze(yd), label="dlsim method",
         use_line_collection=True, markerfmt="ko")
plt.stem(td, y_conv, label="Convolve method",
         use_line_collection=True, markerfmt="yx")
plt.xlabel(r"Discrete time, $n$", fontsize=16)
plt.ylabel(r"Output, $y[n]$", fontsize=16)
plt.grid()
plt.legend()
plt.xticks(np.arange(15))
plt.savefig(f"dtft_a_0_5.pdf")
plt.show()

a = 0.9
x = a**n * np.heaviside(n, 1)

td, yd = sys.output(x, n)  # dlsim method
y_conv = np.convolve(h, x, 'same')[14:]  # Convolve method

# Plot a = 0.9
plt.figure()
plt.title(f"System output, $a=0.9$")
plt.stem(td, x[14:], label="Input $x[n]$",
         use_line_collection=True, markerfmt="bo")
plt.stem(td, np.squeeze(yd), label="dlsim method",
         use_line_collection=True, markerfmt="ko")
plt.stem(td, y_conv, label="Convolve method",
         use_line_collection=True, markerfmt="yx")
plt.xlabel(r"Discrete time, $n$", fontsize=16)
plt.ylabel(r"Output, $y[n]$", fontsize=16)
plt.grid()
plt.legend()
plt.xticks(np.arange(15))
plt.savefig(f"dtft_a_0_9.pdf")
plt.show()
