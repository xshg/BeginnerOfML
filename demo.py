import matplotlib.pyplot as plt
import numpy as np

# plt.figure(figsize=(5, 5))
# plt.show()

A = np.array([[1, 2, 3],[4, 5, 6]])
B = np.array([[1, 2], [3, 4], [5, 6]])
print(A)
print(B)
print(A * B)
print(np.dot(A, B))