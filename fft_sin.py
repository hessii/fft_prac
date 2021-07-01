import numpy as np
import matplotlib.pyplot as plt

# sine graph
n = 100
L = 2 * np.pi
dx = L/(n-1)
x = np.linspace(0, L, n)
y = np.sin(x)

fig1 = plt.figure()
plt.plot(x, y, '.-')
plt.show()

# FFT
fft = np.fft.fft(y[:n-1])
dk = 2 * np.pi / L
kmax = dk * (n-1)
k = np.linspace(0, kmax, n)
xfft = k[:n-1]

fig2 = plt.figure()
plt.plot(xfft, fft)


fsqr = np.abs(y[:n-1]) ** 2
fsqravg = (1/(n-1)) * sum(fsqr)

csqr = np.abs(fft[:n-1]) ** 2
csqrsum = sum(csqr)

