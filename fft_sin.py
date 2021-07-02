import numpy as np
import matplotlib.pyplot as plt

# sine graph
n = 19
L = 2 * np.pi
dx = L/n
x = np.linspace(0, L, n + 1)
x = x[:n]
y = 10 * np.sin(1*x)

fig1 = plt.figure()
plt.plot(x, y, '.-')
plt.show()

# FFT
fft = np.fft.fft(y)
fft = np.fft.fftshift(fft)
fft_mag = 2 * np.abs(fft) / n

dk = 2 * np.pi / L
k = np.arange(-np.floor(n/2), n/2, 1)*dk
xfft = k

fig2 = plt.figure()
plt.plot(xfft[int(n/2):], fft_mag[int(n/2):], '.-')

#Parseval's theorem
fsqravg = np.mean(np.abs(y) ** 2)

csqrsum = sum(np. abs(fft) ** 2)

print(fsqravg, ', ', csqrsum/(n*n))

