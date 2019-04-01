import csv
import numpy as np

import matplotlib.pyplot as plt

p_list = []
mid = []


p_list = [[924.5,9844.1],[466.4,5074.7],[104.3,2750],[20.0367,155.486],[1442.1,17824.3]]
# p_list = [[532.3942,3726.7594],[579.0029,4632.023],[271.4432,1628.6592],[163.9302,1140.5114]]
xList = []
yList = []
for i in range(len(p_list)):
    xList.append(p_list[i][0])
    yList.append(p_list[i][1])

plt.figure(figsize=(10,6))
# plt.ylim(0.0, 2.0)
plt.title('Environmental degradation index values of land use project')
plt.xlabel('Environmental degradation index')
plt.ylabel('Evaluation value')
name_list = ['A_1','A_2','A_3','A_4','DC']
x = range(len(p_list))
y = [i for i in x]
x = y
print(x)
total_width, n = 0.8, 5
width = total_width / n

# y = [i+2*width for i in x]
# x = y
plt.subplot(121)
plt.title('Direct economic index values of land use project')
plt.xlabel('Direct economic index')
plt.ylabel('Cost value')

plt.bar(x, [d[0] for d in p_list], width=width*2, label='Small Project',tick_label=name_list, fc='r')
for x1, y1 in zip(x, xList):
    plt.text(x1, y1+0.3, '%.0f'%y1, ha='center', va='bottom', fontsize=8)
plt.legend()

plt.subplot(122)
plt.title('Direct economic index values of land use project')
plt.xlabel('Direct economic index')
plt.ylabel('Cost value')

plt.bar(x, [d[1] for d in p_list], width=width*2, label='Large Project', tick_label=name_list, fc='b')
for x1, y1 in zip(x, yList):
    plt.text(x1, y1+0.3, '%.0f'%y1, ha='center', va='bottom', fontsize=8)

# plt.bar(x, [d[2] for d in p_list], width=width, label='South America', tick_label=name_list, fc='g')
# y = [i+width for i in x]
# x = y
# print(x)
# plt.bar(x, [d[3] for d in p_list], width=width, label='Europe', tick_label=name_list, fc='b')
# y = [i+width for i in x]
# x = y
# print(x)
# plt.bar(x, [d[4] for d in p_list], width=width, label='Asia', tick_label=name_list, fc='purple')
plt.legend()
plt.show()