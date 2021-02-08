import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc

# Latex font rendering
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

def c_n(k):
    return 1j/(2*np.pi*k)*(2-np.exp(1j*k*np.pi)-np.exp(1j*k*np.pi/2))

def f_terms(t, k):
    return c_n(k)*np.exp(1j*k*np.pi/2*t) + c_n(-k)*np.exp(-1j*k*np.pi/2*t)

def f_sum(t, n):
    nscum = np.arange(n) + 1
    return 0.75 + np.sum( f_terms(t, nscum[np.newaxis].T), axis=0)


t = np.linspace(-3, 5, 1001)

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
plt.savefig("f_series_4_6b.pdf")
plt.show()