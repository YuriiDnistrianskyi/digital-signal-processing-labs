import matplotlib.pyplot as plt
import numpy as np

Ta = 0.1
N = 10
f_nTa = [0, -6.0, -14.0, -4.0, 0.2, 5.0, 0.8, -2.0, -0.4, -0.1]


def dft(f):
    X = []
    for k in range(N):
        result = 0j

        for n in range(N):
            result += f[n] * np.exp(-1j * 2 * (np.pi / N) * k * n)

        X.append(result)

    return np.array(X)

Y = dft(f_nTa)
A = abs(Y)
freqs = np.fft.fftfreq(N, d=Ta)
A_shifted = np.concatenate((A[N // 2:], A[:N // 2]))
freqs_shifted = np.concatenate((freqs[N // 2:], freqs[:N // 2]))

plt.stem(freqs_shifted, A_shifted, label="DFT")
plt.xlabel("f")
plt.ylabel("A")
plt.grid()
plt.legend()
plt.show()
