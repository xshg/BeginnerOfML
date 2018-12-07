# 最好制作对应的坐标图
import numpy as np

def AND(x1, x2):
    bias = -.7
    paras = np.array((.5, .5))
    x = np.array((x1, x2))
    y = np.sum(x * paras) + bias
    if y<=0:
        return 0
    else:
        return 1

def OR(x1, x2):
    bias = -.3
    paras = np.array((.5, .5))
    x = np.array((x1, x2))
    y = np.sum(x * paras) + bias
    if y<=0:
        return 0
    else:
        return 1

def NAND(x1, x2):
    bias = .7
    paras = np.array((-.5, -.5))
    x = np.array((x1, x2))
    y = np.sum(x * paras) + bias
    if y<=0:
        return 0
    else:
        return 1


for x1 in (0, 1):
    for x2 in (0, 1):
        print('AND({}, {}) = {}'.format(x1, x2, AND(x1, x2)))
for x1 in (0, 1):
    for x2 in (0, 1):
        print('OR({}, {}) = {}'.format(x1, x2, OR(x1, x2)))
for x1 in (0, 1):
    for x2 in (0, 1):
        print('NAND({}, {}) = {}'.format(x1, x2, NAND(x1, x2)))
