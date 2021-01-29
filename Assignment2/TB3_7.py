import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-8, 8, 1001)
dt = t[1]-t[0]
x = 2*(np.heaviside(t, 0.5) - np.heaviside(t-1, 0.5) + np.heaviside(t-2, 0.5) - np.heaviside(t-3, 0.5))
h = 3*(np.heaviside(t-2, 0.5)-np.heaviside(t-4, 0.5))
y = np.convolve(h,x, mode='same') * dt

def u(t):
    return np.heaviside(t, 0.5)

def y_ex(t):
    return 6*t*(u(t-2)-u(t-3)-u(t-6)+u(t-7)) + 6*(-2*u(t-2)+3*u(t-3)+6*u(t-6)-7*u(t-7))

plt.figure()
plt.plot(t, y)
plt.plot(t, y_ex(t))
plt.xlim(left=0, right = 8)
plt.grid()
plt.show()