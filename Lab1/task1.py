import numpy as np
import matplotlib.pyplot as plt

x = np.array([2, 4, 6, 7, 10, 12, 14, 16])
y = np.array([1, 3, 4, 8, 4, -2, -7, 0])

N = 8

A = np.array([
    [N, np.sum(x), np.sum(x**2)],
    [np.sum(x), np.sum(x**2), np.sum(x**3)],
    [np.sum(x**2), np.sum(x**3), np.sum(x**4)]
])

B = np.array([
    np.sum(y),
    np.sum(x*y),
    np.sum(x**2 * y)
])

a, b, c = np.linalg.solve(A, B)

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")


def create_function(a, b, c):
    def function(x):
        return a + b * x + c * x * x

    return function

function = create_function(a, b, c)

x_list = np.linspace(min(x), max(x), 100)
y_list = [function(i) for i in x_list]

plt.scatter(x, y, label="Parameters")
plt.plot(x_list, y_list, label="Polinom")

plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()
plt.show()
