# numpy.fft.fft: compute the one-dimensional discrete Fourier transform
# numpy.fft.fftfreq: return the discrete Fourier Transform sample frequencies
# numpy.fft.ifft: compute the one-dimensional inverse discrete Fourier transform

import numpy as np
import matplotlib.pyplot as plt

# Setup for domain
# number of points
n = 500

# Distance (in meters) or time period (in seconds)
L = 100        # total period = 100 (total length of the graph)

# angular frequency omega
omg = 2.0 * np.pi / L

# Creating individual signals
x = np.linspace(0, L, n+1)       # [0, 0.1001001, 0,2002002, ..., 100]
x = x[:n]
y1 = 1. * np.cos(5. * omg * x)      # signal 1, angular velocity = 5w (5 times the angular velocity omg)
y2 = 2. * np.sin(10. * omg * x)     # signal 2
y3 = 0.5 * np.sin(20. * omg * x)    # signal 3
# (numpy.linspace(start, stop, num=50): #return evenly spaced numbers over a specified interval)

# Full signal
y = y1 + y2 + y3

# Preparatory steps
# Create all the necessary frequencies
#fft.fftfreq(n, d=1.0): DFT sample frequencies, n: # of samples, d: sample spacing(dx)(default=1)
dx = L / n
dk = 2 * np.pi / L     # frequency spacing
freqs = np.fft.fftshift(np.fft.fftfreq(n, dx)) #[-0.5, -0.49, ..., -0.01, 0, 0.01, ..., 0.49]

# FFT and power spectra calculations
# fft values
fft_vals = np.fft.fft(y)
fft = np.fft.fftshift(fft_vals)

# true theoretical fft
# 2*||/n for normalization
fft_theo = 2.0 * np.abs(fft) / n

plt.figure()
plt.title('Original Signal')
plt.plot(x, y, label='original')
plt.legend()

plt.figure()
plt.plot(freqs, fft, '.-', label='raw fft values')
plt.title('Raw FFT values')

plt.figure()
plt.plot(freqs[int(n/2):], fft_theo[int(n/2):], '.-', label='true fft values')
plt.title('True FFT values')

plt.show()


# want to extract the magnitudes and the x values for the peaks
#






