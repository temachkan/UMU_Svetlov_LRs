import matplotlib.pyplot as plt
import numpy as np
file = open('data2.csv')
l = file.readlines()
s = len(l)
sum = 0
z = 0
b = 0
u = 0
bM = 0
sumb = 0
sumbM = 0
m = []
n = []
for i in range(s):
    x = l[i].split(',')
    u = x[2].split('.')
    y = x[4].split(':')
    z = x[8]
    if y[0] == '192.168.250.59':
        m.append(u[0])
        n.append(x[8])
        if z.isdigit():
            b = int(z)
            sumb = sumb + b
        else:
            bM = float(z) * 1048576
            sumbM = sumbM + bM
sum = sumb + sumbM
X = float('{:.2f}'.format(((sum - 1000) / 1048576) * 1))
print(X, 'руб.')
n.sort()
m.sort()
plt.plot(m, n)
plt.xlabel('time')
plt.ylabel('bytes')
plt.show()
