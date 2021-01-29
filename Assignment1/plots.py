import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc

# Latex font rendering
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

a = lambda t: 5*np.exp(-t/2)
b = lambda t: 5*np.exp(-2*t)
c = lambda t: 5*np.exp(t/2)
d = lambda t: 5*(1-np.exp(-t/2))
e = lambda t: 5*(1-np.exp(-2*t))
f = lambda t: 5*(np.exp(1j*2*t) -np.exp(-1j*2*t))
g = lambda t: 5*np.exp(-2*t)*(np.exp(1j*2*t) -np.exp(-1j*2*t))
h = lambda t: 5*np.exp(-t/2)*(np.exp(1j*2*t) -np.exp(-1j*2*t))

labels = "abcdefgh"
funcs = [a,b,c,d,e,f,g,h]
t = np.linspace(0, 10, 201)

plt.figure()
plt.title(f"Functions a), b), d), and e)")
for i in [0,1,3,4]:
    plt.plot(t, funcs[i](t), label=labels[i] + ")")
plt.xlabel(r"Time, $t$ (s)", fontsize=16)
plt.ylabel(r"$x(t)$", fontsize=16)
plt.legend()
plt.grid()
plt.savefig(f"214abde.pdf")
plt.show()

plt.figure()
plt.title(f"Function c)")
plt.plot(t, funcs[2](t), label=labels[2] + ")")
plt.xlabel(r"Time, $t$ (s)", fontsize=16)
plt.ylabel(r"$x(t)$", fontsize=16)
plt.legend()
plt.grid()
plt.savefig(f"214c.pdf")
plt.show()

plt.figure()
plt.title(f"Imaginary part of functions f), g) and h)")
for i in [5, 6, 7]:
    plt.plot(t, np.imag(funcs[i](t)), label=labels[i] + ")")
plt.xlabel(r"Time, $t$ (s)", fontsize=16)
plt.ylabel(r"$\Im(x(t))$", fontsize=16)
plt.legend()
plt.grid()
plt.savefig(f"214fgh.pdf")
plt.show()