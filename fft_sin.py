import numpy as np
import matplotlib.pyplot as plt

# sine graph
n = 101
L = 2 * np.pi
dx = L/n
x = np.linspace(0, L, n + 1)
x = x[:n]
y = 10 * np.sin(1*x)

fig1 = plt.figure()
plt.plot(x, y, '.-')
plt.tick_params(labelsize=11)
plt.title('sine function', fontsize=17)

# FFT
fft = np.fft.fft(y)
fft = np.fft.fftshift(fft)
fft_mag = 2 * np.abs(fft) / n

'''
dk = 2 * np.pi / L
k = np.arange(-np.floor(n/2), n/2, 1)*dk
xfft = k
'''

k = np.fft.fftshift(np.fft.fftfreq(n, dx))

fig2 = plt.figure()
plt.step(k[int(n/2):], fft_mag[int(n/2):], '.-', where='mid')
plt.tick_params(labelsize=11)
plt.title('FFT', fontsize=17)
plt.show()

#Parseval's theorem
fsqravg = np.mean(np.abs(y) ** 2)

csqrsum = sum(np. abs(fft) ** 2)x

print(fsqravg, ', ', csqrsum/(n*n))

