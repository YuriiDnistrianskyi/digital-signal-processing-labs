import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline

x = np.array([2, 4, 6, 7, 10, 12, 14, 16])
y = np.array([1, 3, 4, 8, 4, -2, -7, 0])

N = 8

spline = CubicSpline(x, y)

for i in range(N - 1):
    a = spline.c[0, i]
    b = spline.c[1, i]
    c = spline.c[2, i]
    d = spline.c[3, i]

    print(f"Interval {i + 1}: a = {a}; b = {b}; c = {c}; d = {d}")

x_list = np.linspace(min(x), max(x), 100)
y_list = spline(x_list)

plt.scatter(x, y, label="Parameters")
plt.plot(x_list, y_list, label="Spline")

plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()
plt.show()
