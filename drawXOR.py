import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(5, 5))

# 绘制 AND(x, y) 和 0.5 * x1 + 0.5 * y = 0.7 的直线
# x1s, y1s 为 (0,0), (0,1) 和 (1,0)
x1s = (0, 1)
y1s = (0, 1)
plt.scatter(x1s, y1s, c='red', marker='o')
# x2s, y2s 为 (1,1)
x2s = (0, 1)
y2s = (1, 0)
plt.scatter(x2s, y2s, c='blue', marker='v')
# xline = np.arange(-1, 2, .1)
# yline = -1. * xline + 1.4
# plt.plot(xline, yline, '')
plt.xlim(-.5, 2)
plt.ylim(-.5, 2)
plt.xlabel('x')
plt.ylabel('y')
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
# plt.legend()
plt.show()