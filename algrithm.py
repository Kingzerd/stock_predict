import numpy as np
import matplotlib.pyplot as plt
import math
import time


def route_print(mark):
    if mark == 0:
        print("A -> ", end='')
    if mark == 1:
        print("B -> ", end='')
    if mark == 2:
        print("C -> ", end='')
    if mark == 3:
        print("D -> ", end='')
    if mark == 4:
        print("E -> ", end='')
    if mark == 5:
        print("F -> ", end='')
    if mark == 6:
        print("G -> ", end='')
    if mark == 7:
        print("H -> ", end='')
    if mark == 8:
        print("I -> ", end='')
    if mark == 9:
        print("J -> ", end='')


data = np.array([
    [1, 40, 44],
    [2, 24, 14],
    [3, 17, 22],
    [4, 22, 76],
    [5, 51, 94],
    [6, 87, 65],
    [7, 68, 52],
    [8, 84, 36],
    [9, 66, 25],
    [10, 61, 26],
])
data_copy = data
dist = np.zeros((data.shape[0], data_copy.shape[0]))

# 计算城市之间的距离矩阵
for i in range(data.shape[0]):
    for j in range(data_copy.shape[0]):
        dist[i, j] = math.sqrt(np.sum((data[i, 1:] - data_copy[j, 1:]) ** 2))
"""
passed:已经遍历过的城市
dist：城市间距离矩阵
min_distance:目前的最小路径总长度
min_current：当前最小距离
flag：访问标记
"""
i = 1
n = data.shape[0]
j = 0
min_distance = 0
passed = []
passed.append(0)
# start = time.clock()
while True:
    k = 1
    min_current = 10000000
    while True:
        l = 0
        flag = 0
        if k in passed:
            flag = 1
        if (flag == 0) and (dist[k][passed[i - 1]] < min_current):
            j = k;
            min_current = dist[k][passed[i - 1]];
        k += 1
        if k >= n:
            break;
    passed.append(j)
    i += 1;
    min_distance += min_current
    if i >= n:
        break;
min_distance += dist[0][j]
# end = time.clock()
print("最少里程：")
print(min_distance)

route_x = []
route_y = []
print("最少里程路线：")
for m in range(n):
    route_print(passed[m])
    route_x.append(data[:, 1][passed[m]])
    route_y.append(data[:, 2][passed[m]])
print("A")
route_x.append(data[:, 1][0])
route_y.append(data[:, 2][0])
# print("程序运行时间：%s s" % (end - start))
plt.figure()
plt.plot(data[:, 1][0], data[:, 2][0], 'o', color='red')
plt.plot(data[:, 1][1:], data[:, 2][1:], '.', color='red')
for m in range(n):
    plt.plot(route_x, route_y, '-', color='blue')
plt.show()
