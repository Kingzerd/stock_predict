import csv
import numpy as np
import random
import matplotlib.pyplot as plt

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
for i in range(45):
    i = i * 35
    digity.append(digit[i])
    dig.append(tmp[i])

print(len(digity))
# time_line = []
# for i in range(1987, 2017):
#     for j in range(1, 13):
#         time_line.append(str(i) + '-' + str(j))
# print(time_line)
pre1 = []

pre1.append(dig[len(dig)-2])
pre1.append(dig[len(dig)-1])
for i in range(19):
    w = abs(pre1[len(pre1) - 1] - pre1[len(pre1) - 2])/2
    t = (random.random()-0.5)/10
    if(random.random()>0.8):
        pre1.append(pre1[len(pre1)-1]+w+t)
    else:
        pre1.append(pre1[len(pre1) - 1] - w - t)

print(pre1)


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
for i in range(45):
    i = i * 35
    digity.append(digit[i])
    dig.append(tmp[i])

print(len(digity))
# time_line = []
# for i in range(1987, 2017):
#     for j in range(1, 13):
#         time_line.append(str(i) + '-' + str(j))
# print(time_line)
pre2 = []

pre2.append(dig[len(dig)-2])
pre2.append(dig[len(dig)-1])
for i in range(19):
    w = abs(pre2[len(pre2) - 1] - pre2[len(pre2) - 2])/2
    t = (random.random()-0.5)/10
    if(random.random()>0.8):
        pre2.append(pre2[len(pre2)-1]+w+t)
    else:
        pre2.append(pre2[len(pre2) - 1] - w - t)



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
for i in range(45):
    i = i * 35
    digity.append(digit[i])
    dig.append(tmp[i])

print(len(digity))
# time_line = []
# for i in range(1987, 2017):
#     for j in range(1, 13):
#         time_line.append(str(i) + '-' + str(j))
# print(time_line)
pre3 = []

pre3.append(dig[len(dig)-2])
pre3.append(dig[len(dig)-1])
for i in range(19):
    w = abs(pre3[len(pre3) - 1] - pre3[len(pre3) - 2])/2
    t = (random.random()-0.5)/10
    if(random.random()>0.8):
        pre3.append(pre3[len(pre3)-1]+w+t)
    else:
        pre3.append(pre3[len(pre3) - 1] - w - t)

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
for i in range(45):
    i = i * 35
    digity.append(digit[i])
    dig.append(tmp[i])

print(len(digity))
# time_line = []
# for i in range(1987, 2017):
#     for j in range(1, 13):
#         time_line.append(str(i) + '-' + str(j))
# print(time_line)
pre4 = []

pre4.append(dig[len(dig)-2])
pre4.append(dig[len(dig)-1])
for i in range(19):
    w = abs(pre4[len(pre4) - 1] - pre4[len(pre4) - 2])/2
    t = (random.random()-0.5)/10
    if(random.random()>0.8):
        pre4.append(pre4[len(pre4)-1]+w+t)
    else:
        pre4.append(pre4[len(pre4) - 1] - w - t)


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
for i in range(45):
    i = i * 35
    digity.append(digit[i])
    dig.append(tmp[i])

print(len(digity))
# time_line = []
# for i in range(1987, 2017):
#     for j in range(1, 13):
#         time_line.append(str(i) + '-' + str(j))
# print(time_line)
pre5 = []

pre5.append(dig[len(dig)-2])
pre5.append(dig[len(dig)-1])
for i in range(19):
    w = abs(pre5[len(pre5) - 1] - pre5[len(pre5) - 2])/2
    t = (random.random()-0.5)/10
    if(random.random()>0.8):
        pre5.append(pre5[len(pre5)-1]+w+t)
    else:
        pre5.append(pre5[len(pre5) - 1] - w - t)


ntime_line = []
for i in range(2010, 2031):
    ntime_line.append(str(i))

time_line = []
for i in range(1965, 2011):
    time_line.append(str(i))
# print(time_line)

fig1 = plt.figure(figsize=(7, 5))
ax1 = fig1.add_subplot(1, 1, 1)
plt.ylim(0.0,1.5)
# ax1.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))  # 设置时间标签显示格式
# plt.xticks(pd.date_range('1987-01-01', '1988-01-01'), rotation=90)
plt.xticks(range(len(ntime_line[:])), ntime_line[:], rotation=90)
# for x, y in zip(range(len(time_line[:60])), digity[:60]):
#     plt.text(x, y + 0.3, '%.0f' % y, ha='center', va='bottom', fontsize=10.5)
plt.plot(pre1, '.-',color='r',label=name_list[0])
plt.plot(pre2, '.-',color='y',label=name_list[1])
plt.plot(pre3, '.-',color='g',label=name_list[2])
plt.plot(pre4, '.-',color='b',label=name_list[3])
plt.plot(pre5, '.-',color='purple',label=name_list[4])
plt.title('Each note'+"'"+'s prediction of evaluation health values')
plt.xlabel('Years')
plt.ylabel('Health values')
plt.legend()
plt.show()
