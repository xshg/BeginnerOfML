import numpy as np
import matplotlib.pyplot as plt

def stepFunction(x):
    return np.array(x>0, np.int)

def sigmoid(x):
    '''
    sigmoid 激活函数 1/(1+np.exp(-x))
    '''
    return 1. / (1+np.exp(-x))

def ReLU(x):
    '''
    ReLU激活函数，Rectified Linear Unit
    return 0, x<=0
    return x, x>0
    '''
    return np.maximum(0, x)

def softmaxOverflow(a):
    '''
    softmax的原始版本，当参数a内值比较大时，会产生溢出错误
    例如：a = np.array([1010, 1000, 990])
    '''
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

def softmax(x):
    '''
    softmax 的防溢出版本
    参数a 如果为2维数组也可以处理
    '''
    if x.ndim == 2:
        x = x.T     # 将a转置
        x = x - np.max(x, axis=0)   # 溢出策略
        y = np.exp(x)/np.sum(np.exp(x), axis=0)
        return y.T
    x = x - np.max(x)
    return np.exp(x)/np.sum(np.exp(x))


def softmax_ndim1(a):
    '''
    softmax的防溢出版本
    参数a 只能是一维数组
    '''
    c = np.max(a)
    exp_a = np.exp(a-c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

if __name__ == "__main__":
    plt.figure(figsize=(5, 5))
    
    # X , x in (-10, 5, step=.1)
    X = np.arange(-10, 5, .1)

    # draw step function
    Ystep = stepFunction(X)
    plt.plot(X, Ystep, c='pink', linestyle='-', label='y = stepFunc(x)')

    # draw sigmod
    Ysigmoid = sigmoid(X)
    plt.plot(X, Ysigmoid, c='blue', linestyle='--', label='y = sigmoid(x)')

    # draw ReLU
    YReLU = ReLU(X)
    plt.plot(X, YReLU, c='green', linestyle='-.', label ='y = ReLU(x)')
    plt.legend()


    plt.show()