import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
from matplotlib import rc

# Latex font rendering
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

def f_term(t, k):
    pi_k = np.pi * k
    return 1/k**2 * (np.cos(pi_k * t) * (1 - np.cos(pi_k)) +
                     np.sin(pi_k * t) * (pi_k - np.sin(pi_k)))

def f_sum(t, n):
    sum = 0
    for k in range(1, n + 1):
        sum += f_term(t, k)
    return 0.5 + 2/np.pi**2 * sum

t = np.linspace(-3, 3.5, 501)

plt.figure()
plt.title(r"$\mathcal{F}$ourier series expansion of $x(t)$ of order $n$")
for i in range(2, 6):
    plt.plot(t, f_sum(t, i), label='$n = $ ' +str(i), linewidth = 0.65)
plt.plot(t, f_sum(t, 150), label='$n = $ ' +str(150), c='k',linewidth = 0.65)
plt.xlim(left=t.min(), right=t.max())
plt.xlabel(r"Time, $t$")
plt.ylabel(r"$x(t)$", fontsize=16)
plt.tight_layout()
plt.legend(fancybox=True, framealpha=0)
plt.grid()
plt.savefig("fourier_series.pdf")
plt.show()