import numpy as np
import matplotlib.pyplot as plt

# Step1. Construct a time domain signal
Fs = 2000      # sampling freq
tstep = 1 / Fs   # sample time interval
f0 = 100     # signal freq

N = int(Fs / f0)     # number of samples

t = np.linspace(0, (N-1)*tstep, N)      # time steps
fstep = Fs / N      # freq interval
f = np.linspace(0, (N-1)*fstep, N)      # freq steps

y = 1 * np.sin(2 * np.pi * f0 * t)      # sine wave


# Step2. Perform fft
X = np.fft.fft(y)       # X is a series of complex numbers
X_mag = np.abs(X) / N   # get magnitude and normalize by dividing by N

f_plot = f[0:int(N/2+1)]
X_mag_plot = 2 * X_mag[0:int(N/2+1)]
X_mag_plot[0] = X_mag_plot[0] / 2       # DC component does not need to multiply by 2

# Step3. Plot
fig1 = plt.figure()
plt.plot(t, y, '.-')

fig2 = plt.figure()
plt.plot(f_plot, X_mag_plot, '.-')

plt.show()




