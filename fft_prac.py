import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, fftfreq, ifft
# numpy.fft.fft: compute the one-dimensional discrete Fourier transform
# numpy.fft.fftfreq: return the discrete Fourier Transform sample frequencies
# numpy.fft.ifft: compute the one-dimensional inverse discrete Fourier transform

# Setup for domain
# number of points
n = 1000

# Distance (in meters) or time period (in seconds)
Lx = 100        # period = 100

# angular frequency omega
omg = 2.0 * np.pi / Lx

# Creating individual signals
x = np.linspace(0, Lx, n)
y1 = 1. * np.cos(5. * omg * x)      # signal 1
y2 = 2. * np.sin(10. * omg * x)     # signal 2
y3 = 0.5 * np.sin(20. * omg * x)    # signal 3
# (numpy.linspace(start, stop, num=50): #return evenly spaced numbers over a specified interval)

# Full signal
y = y1 + y2 + y3

# Preparatory steps
# Create all the necessary frequencies
freqs = np.fft.fftfreq(n)      # [0, 0.001, 0.002, 0.003, ..., 0.049]

# make array to be used for power spectra
# ignoring half the values, as they are complex conjugates of the other
# (ignoring negative frequencies)
mask = freqs > 0

# FFT and power spectra calculations
# fft values
fft_vals = np.fft.fft(y)

# true theoretical fft
# 2*|| for ..?
fft_theo = 2.0 * np.abs(fft_vals/n)

plt.figure(1)
plt.title('Original Signal')
plt.plot(x, y, label='original')
plt.legend()

plt.figure(2)
plt.plot(freqs, fft_vals, label='raw fft values')
plt.title('Raw FFT values - need more processing')

plt.figure(3)
plt.plot(freqs[mask], fft_theo[mask], label='true fft values')
plt.title('True FFT values')

plt.show()









