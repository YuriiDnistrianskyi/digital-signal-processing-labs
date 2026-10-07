import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

y = np.array([1.0, 2.5, 3.5, 4.0, 2.0, 1.5])
x = np.array([0.1 * 3 * n for n in range(1, len(y) + 1)])

def function(x, a, b):
    return np.exp(a + b * x)

params, _ = curve_fit(function, x, y)

print(f"A = {params[0]}")
print(f"B = {params[1]}")

x_plot = np.linspace(min(x), max(x), 100)
y_plot = [function(x, params[0], params[1]) for x in x_plot]

plt.scatter(x, y, label="Parameters")
plt.plot(x_plot, y_plot, label="Exponential Approximation")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()
plt.show()
