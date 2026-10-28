import matplotlib.pyplot as plt
import numpy as np

from Lab2.task1 import y_plot

N = 6
fg = 200
fa = 2000

x = []
fg_fa = fg / fa

for k in range(N + 1):
    if k == 0:
        x_k = 2 * fg_fa
    else:
        x_k = 2 * fg_fa * ((np.sin(2 * np.pi * k * fg_fa)) / (2 * np.pi * k * fg_fa))
    x.append(x_k)

print(f"yn = {x[0]}*x0 ", end="")
for n in range(N + 1):
    print(f"+ {x[n]}*x{n} ", end="")

f = np.linspace(0, 500, 10)
H = np.array([
    sum(
        x[k] * np.exp(-1j * 2 * np.pi * freq * k / fa)
        for k in range(N + 1)
    )
    for freq in f
])

amplitude = np.abs(H)
phase = np.unwrap(np.angle(H))

y_plot = np.array(y_plot)
y = np.convolve(
    y_plot, 
    np.array(x), 
    mode='full'
)

plt.figure(figsize=(10, 10))

plt.subplot(3, 1, 1)
plt.plot(f, amplitude, label="АЧХ")
plt.xlabel('f')
plt.ylabel('A')
plt.grid()
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(f, phase, label="ФЧХ")
plt.xlabel('f')
plt.ylabel('P')
plt.grid()
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(y_plot, label="Signal")
plt.plot(y, label="Filter signal")
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()

plt.show()
