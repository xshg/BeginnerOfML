import numpy as np
import matplotlib.pyplot as plt

def mean_squared_error(y, t):
    return .5 * np.sum((y-t)**2)

def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t*np.log(y+delta))

if __name__ == "__main__":
    y=np.array([.1,.05,.6,.0,.05,.1,.0,.1,.0,.0])
    t = np.array([0, 0, 1, 0, 0, 0, 0, 0, 0, 0])
    print(mean_squared_error(y, t))
    y1 = np.array([0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0])
    print(mean_squared_error(y1, t))

    print('-'*20)
    print(cross_entropy_error(y, t))
    print(cross_entropy_error(y1, t))