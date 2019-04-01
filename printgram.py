import csv
import numpy as np

list = []

csvfile = open('./dataset/datas111.csv', newline='')  # 打开一个文件
csvReader = csv.reader(csvfile)  # 返回的可迭代类型
rows = [row for row in csvReader]
new_rows = rows.pop(0)
rowss = [[float(x) for x in row[1:]] for row in rows]
# print(rowss)
tmp = [row[5] for row in rowss]
# print(tmp)
list.append(tmp)
csvfile.close()

csvfile = open('./dataset/datas222.csv', newline='')  # 打开一个文件
csvReader = csv.reader(csvfile)  # 返回的可迭代类型
rows = [row for row in csvReader]
new_rows = rows.pop(0)
rowss = [[float(x) for x in row[1:]] for row in rows]
# print(rowss)
tmp = [row[5] for row in rowss]
# print(tmp)
list.append(tmp)
csvfile.close()

csvfile = open('./dataset/datas333.csv', newline='')  # 打开一个文件
csvReader = csv.reader(csvfile)  # 返回的可迭代类型
rows = [row for row in csvReader]
new_rows = rows.pop(0)
rowss = [[float(x) for x in row[1:]] for row in rows]
# print(rowss)
tmp = [row[5] for row in rowss]
# print(tmp)
list.append(tmp)
csvfile.close()

csvfile = open('./dataset/datas444.csv', newline='')  # 打开一个文件
csvReader = csv.reader(csvfile)  # 返回的可迭代类型
rows = [row for row in csvReader]
new_rows = rows.pop(0)
rowss = [[float(x) for x in row[1:]] for row in rows]
# print(rowss)
tmp = [row[5] for row in rowss]
# print(tmp)
list.append(tmp)
csvfile.close()

csvfile = open('./dataset/datas555.csv', newline='')  # 打开一个文件
csvReader = csv.reader(csvfile)  # 返回的可迭代类型
rows = [row for row in csvReader]
new_rows = rows.pop(0)
rowss = [[float(x) for x in row[1:]] for row in rows]
# print(rowss)
tmp = [row[5] for row in rowss]
# print(tmp)
list.append(tmp)
csvfile.close()

import matplotlib.pyplot as plt

p_list = []
mid = []
le = len(list[0])
for i in range(le):
    # print([row[i] for row in list])
    mean = np.mean([row[i] for row in list])
    tmp = [row[i]/mean for row in list]
    p_list.append(tmp)

print(p_list)


plt.figure(figsize=(15,6))
plt.ylim(0.0, 2.0)
plt.title('The evaluation health values of each note')
plt.xlabel('Years')
plt.ylabel('Evaluation health values')
name_list = ['1965','1970','1975','1980','1985','1990','1995','2000','2005','2010']
x = range(len(p_list))
y = [i for i in x]
x = y
print(x)
total_width, n = 0.8, 5
width = total_width / n

# y = [i+2*width for i in x]
# x = y

print([d[0] for d in p_list])
plt.bar(x, [d[0] for d in p_list], width=width, label='North America', fc='r')
y = [i+width for i in x]
x = y
print(x)
plt.bar(x, [d[1] for d in p_list], width=width, label='Oceania', tick_label=name_list, fc='y')
y = [i+width for i in x]
x = y
print(x)
plt.bar(x, [d[2] for d in p_list], width=width, label='South America', tick_label=name_list, fc='g')
y = [i+width for i in x]
x = y
print(x)
plt.bar(x, [d[3] for d in p_list], width=width, label='Europe', tick_label=name_list, fc='b')
y = [i+width for i in x]
x = y
print(x)
plt.bar(x, [d[4] for d in p_list], width=width, label='Asia', tick_label=name_list, fc='purple')
plt.legend(loc = 'upper right')
plt.show()