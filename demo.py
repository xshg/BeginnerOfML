import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(5, 5))
def sigmod(x):
    return 1.0 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

x = np.arange(-10, 10, .1)
y = relu(x)
print(x)
print(y)
plt.plot(x, y)
plt.legend()
plt.show()

