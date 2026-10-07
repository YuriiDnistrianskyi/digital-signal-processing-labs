import matplotlib.pyplot as plt
import numpy as np

y = np.array([1.0, 2.5, 3.5, 4.0, 2.0, 1.5])

N = 6
omega0 = 1
Ta = (2 * np.pi) / (N * omega0)
t = np.arange(N) * Ta

F = np.fft.fft(y)

a_0 = 2 * F[0].real / N
print(f"a_0 = {a_0}")

a = []
b = []

for k in range(1, N // 2):
    a_k = 2 * F[k].real / N
    b_k = -2 * F[k].imag / N

    print(f"a_{k} = {a_k}")
    print(f"b_{k} = {b_k}")

    a.append(a_k)
    b.append(b_k)

last_a = F[N // 2].real / N
print(f"a_{N // 2} = {last_a}")


def function(t):
    result = a_0 / 2

    for k in range(1, N // 2):  
        result += (
            a[k - 1] * np.cos(k * omega0 * t) + 
            b[k - 1] * np.sin(k * omega0 * t)
        )

    result += last_a * np.cos(N // 2 * omega0 * t)

    return result


x_plot = np.linspace(0, 2 * np.pi, 1000)
y_plot = [function(t) for t in x_plot]

plt.scatter(t, y, label="Parameters")
plt.plot(x_plot, y_plot, label="Fourier Approximation")
plt.xlabel("t")
plt.ylabel("y")
plt.grid()
plt.legend()
plt.show()
