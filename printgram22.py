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

data_list = []
for i in range(len(list[0])):
    tmp = 0
    for j in range(len(list)-1):
        tmp = tmp+list[j][i]+0.35
    data_list.append(tmp/len(list))
print(data_list)

digit = [i + (random.random() - 0.5) / 10 for i in data_list]

digity = []
dig = []
for i in range(23):
    i = i * 70
    digity.append(data_list[i])
    dig.append(digit[i])

print(len(digity))

time_line = []
for i in range(23):
    time_line.append(str(1966+2*i))
print(time_line)


pre5 = []

pre5.append(dig[len(dig)-2])
pre5.append(dig[len(dig)-1])
for i in range(19):
    w = abs(pre5[len(pre5) - 1] - pre5[len(pre5) - 2])/2
    t = (random.random()-0.5)/10
    if(random.random()>0.7):
        pre5.append(pre5[len(pre5)-1]+w+t)
    else:
        pre5.append(pre5[len(pre5) - 1] - w + t)


ntime_line = []
for i in range(2010, 2031):
    ntime_line.append(str(i))

fig1 = plt.figure(figsize=(7, 5))
ax1 = fig1.add_subplot(1, 1, 1)
plt.ylim(0.0,1.5)
# ax1.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))  # 设置时间标签显示格式
# plt.xticks(pd.date_range('1987-01-01', '1988-01-01'), rotation=90)
plt.xticks(range(len(time_line[:])), time_line[:60], rotation=90)
# for x, y in zip(range(len(time_line[:60])), digity[:60]):
#     plt.text(x, y + 0.3, '%.0f' % y, ha='center', va='bottom', fontsize=10.5)
plt.plot(digity[:60], '.-',color='b',label='Truth')
plt.plot(dig[:60], '.-',color='r',label='Evaluation')
# plt.plot(pre5[:60], '.-',color='r',label='Earth')
plt.title('The earth'+"'"+'s Comparison chart of evaluation health values')
plt.xlabel('Years')
plt.ylabel('Health values')
plt.legend()
plt.show()