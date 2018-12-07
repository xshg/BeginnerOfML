def AND(x1, x2):
    w1, w2, theta = .5, .5, .7
    y = w1*x1 + w2*x2
    if y <= theta:
        return 0
    else:
        return 1
def OR(x1, x2):
    w1, w2, theta = .7, .7, .5
    y = w1*x1 + w2*x2
    if y <= theta:
        return 0
    else:
        return 1

def NAND(x1, x2):
    w1, w2, theta = -.7, -.7, -.5
    y = w1*x1 + w2*x2
    if y <= theta:
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
