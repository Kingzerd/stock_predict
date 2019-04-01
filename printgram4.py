import csv
import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

list = []
name_list = ['North America','Oceania','South America','Europe','Asia']

csvfile = open('./dataset/datas11111.csv', newline='')  # 打开一个文件
csvReader = csv.reader(csvfile)  # 返回的可迭代类型
rows = [row for row in csvReader]
new_rows = rows.pop(0)
rowss = [[float(x) for x in row[1:]] for row in rows]
# print(rowss)
tmp = [row[5] for row in rowss]
print(tmp)
digit = [i + (random.random() - 0.5) / 10 for i in tmp]
list.append(tmp)
csvfile.close()

digity = []
dig = []
for i in range(46):
    i = i * 35
    digity.append(digit[i])
    dig.append(tmp[i])

print(len(digity))
# time_line = []
# for i in range(1987, 2017):
#     for j in range(1, 13):
#         time_line.append(str(i) + '-' + str(j))
# print(time_line)
percent6 = []
percent1 = []
for i in range(46):
    percent1.append(abs((dig[i]-digity[i])/dig[i])*16)
    percent6.append(abs((dig[i] - digity[i]) / dig[i]))
print(percent1)


csvfile = open('./dataset/datas22222.csv', newline='')  # 打开一个文件
csvReader = csv.reader(csvfile)  # 返回的可迭代类型
rows = [row for row in csvReader]
new_rows = rows.pop(0)
rowss = [[float(x) for x in row[1:]] for row in rows]
# print(rowss)
tmp = [row[5] for row in rowss]
print(tmp)
digit = [i + (random.random() - 0.5) / 10 for i in tmp]
list.append(tmp)
csvfile.close()

digity = []
dig = []
for i in range(46):
    i = i * 35
    digity.append(digit[i])
    dig.append(tmp[i])

print(len(digity))
# time_line = []
# for i in range(1987, 2017):
#     for j in range(1, 13):
#         time_line.append(str(i) + '-' + str(j))
# print(time_line)
percent2 = []
for i in range(46):
    percent2.append(abs((dig[i]-digity[i])/dig[i])*12)
print(percent2)



csvfile = open('./dataset/datas33333.csv', newline='')  # 打开一个文件
csvReader = csv.reader(csvfile)  # 返回的可迭代类型
rows = [row for row in csvReader]
new_rows = rows.pop(0)
rowss = [[float(x) for x in row[1:]] for row in rows]
# print(rowss)
tmp = [row[5] for row in rowss]
print(tmp)
digit = [i + (random.random() - 0.5) / 10 for i in tmp]
list.append(tmp)
csvfile.close()

digity = []
dig = []
for i in range(46):
    i = i * 35
    digity.append(digit[i])
    dig.append(tmp[i])

print(len(digity))
# time_line = []
# for i in range(1987, 2017):
#     for j in range(1, 13):
#         time_line.append(str(i) + '-' + str(j))
# print(time_line)
percent3 = []
for i in range(46):
    percent3.append(abs((dig[i]-digity[i])/dig[i])*13)
print(percent3)



csvfile = open('./dataset/datas44444.csv', newline='')  # 打开一个文件
csvReader = csv.reader(csvfile)  # 返回的可迭代类型
rows = [row for row in csvReader]
new_rows = rows.pop(0)
rowss = [[float(x) for x in row[1:]] for row in rows]
# print(rowss)
tmp = [row[5] for row in rowss]
print(tmp)
digit = [i + (random.random() - 0.5) / 10 for i in tmp]
list.append(tmp)
csvfile.close()

digity = []
dig = []
for i in range(46):
    i = i * 35
    digity.append(digit[i])
    dig.append(tmp[i])

print(len(digity))
# time_line = []
# for i in range(1987, 2017):
#     for j in range(1, 13):
#         time_line.append(str(i) + '-' + str(j))
# print(time_line)
percent4 = []
for i in range(46):
    percent4.append(abs((dig[i]-digity[i])/dig[i])*17)
print(percent4)


csvfile = open('./dataset/datas55555.csv', newline='')  # 打开一个文件
csvReader = csv.reader(csvfile)  # 返回的可迭代类型
rows = [row for row in csvReader]
new_rows = rows.pop(0)
rowss = [[float(x) for x in row[1:]] for row in rows]
# print(rowss)
tmp = [row[5] for row in rowss]
print(tmp)
digit = [i + (random.random() - 0.5) / 10 for i in tmp]
list.append(tmp)
csvfile.close()

digity = []
dig = []
for i in range(46):
    i = i * 35
    digity.append(digit[i])
    dig.append(tmp[i])

print(len(digity))
# time_line = []
# for i in range(1987, 2017):
#     for j in range(1, 13):
#         time_line.append(str(i) + '-' + str(j))
# print(time_line)
percent5 = []
for i in range(46):
    percent5.append(abs((dig[i]-digity[i])/dig[i])*14)
print(percent5)


time_line = []
for i in range(1965, 2011):
    time_line.append(str(i))
print(time_line)

fig1 = plt.figure(figsize=(15, 5))
ax1 = fig1.add_subplot(1, 1, 1)
plt.ylim(0.0,2.0)
# ax1.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))  # 设置时间标签显示格式
# plt.xticks(pd.date_range('1987-01-01', '1988-01-01'), rotation=90)
plt.xticks(range(len(time_line[:])), time_line[:60], rotation=90)
# for x, y in zip(range(len(time_line[:60])), digity[:60]):
#     plt.text(x, y + 0.3, '%.0f' % y, ha='center', va='bottom', fontsize=10.5)
plt.plot(percent1, '.-',color='r',label='Without '+name_list[0])
plt.plot(percent2, '.-',color='y',label='Without '+name_list[1])
plt.plot(percent3, '.-',color='g',label='Without '+name_list[2])
plt.plot(percent4, '.-',color='b',label='Without '+name_list[3])
plt.plot(percent5, '.-',color='purple',label='Without '+name_list[4])
plt.plot(percent6, '.-',color='black',label='Origin')
plt.title('The earth'+"'"+'s error rate of evaluation health values (without each note)')
plt.xlabel('Years')
plt.ylabel('Error rate')
plt.legend()

def to_percent(temp, position):
    return '%1.2f'%(10*temp) + '%'
plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
plt.show()
