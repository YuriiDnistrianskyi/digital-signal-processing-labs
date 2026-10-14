import matplotlib.pyplot as plt
import numpy as np

Ta = 0.1

N = 10
f_nTa = [0, -6.0, -14.0, -4.0, 0.2, 5.0, 0.8, -2.0, -0.4, -0.1]

Y = np.fft.fft(f_nTa)
A = np.abs(Y)
A_shifted = np.fft.fftshift(A)

freqs = np.fft.fftshift(np.fft.fftfreq(N, d=Ta))

plt.stem(freqs, A_shifted, label="DFT")
plt.xlabel("f")
plt.ylabel("A")
plt.grid()
plt.legend()
plt.show()
