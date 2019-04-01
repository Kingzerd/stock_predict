import csv
import numpy as np

list = []

csvfile = open('./dataset/datas55.csv', newline='')  # 打开一个文件
csvReader = csv.reader(csvfile)  # 返回的可迭代类型
rows = [row for row in csvReader]
new_rows = rows.pop(0)
rowss = [new_rows]+[[float(x) for x in row] for row in rows]
print(rowss)
list.append(new_rows)
mid = []
for i in range(1, len(rowss)):
    mid.append(rowss[i][6])
mean = np.mean(mid)
for i in range(1, len(rowss)):
    # if(rowss[i][0]%5==0):
    list.append([rowss[i][0],rowss[i][1],rowss[i][2],rowss[i][3],rowss[i][4],rowss[i][5],rowss[i][6]/mean])
csvfile.close()
print(list)

csvfile = open('./dataset/datas5555.csv', 'w', newline='')
writer = csv.writer(csvfile)
for row in list:
    writer.writerow(row)
csvfile.close()
