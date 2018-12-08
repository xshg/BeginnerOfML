import numpy as np
import matplotlib.pyplot as plt

def stepFunction(x):
    return np.array(x>0, np.int)

def sigmod(x):
    '''
    sigmod 激活函数 1/(1+np.exp(-x))
    '''
    return 1. / (1+np.exp(-x))

def ReLU(x):
    '''
    ReLU激活函数，Rectified Linear Unit
    return 0, x<=0
    return x, x>0
    '''
    return np.maximum(0, x)

if __name__ == "__main__":
    plt.figure(figsize=(5, 5))
    
    # X , x in (-10, 5, step=.1)
    X = np.arange(-10, 5, .1)

    # draw step function
    Ystep = stepFunction(X)
    plt.plot(X, Ystep, c='pink', linestyle='-', label='y = stepFunc(x)')

    # draw sigmod
    Ysigmod = sigmod(X)
    plt.plot(X, Ysigmod, c='blue', linestyle='--', label='y = sigmod(x)')

    # draw ReLU
    YReLU = ReLU(X)
    plt.plot(X, YReLU, c='green', linestyle='-.', label ='y = ReLU(x)')
    plt.legend()
    plt.show()