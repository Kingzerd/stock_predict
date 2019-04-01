import csv

list = []

csvfile = open('./dataset/datas3333.csv', newline='')  # 打开一个文件
csvReader = csv.reader(csvfile)  # 返回的可迭代类型
rows = [row for row in csvReader]
new_rows = rows.pop(0)
rowss = [new_rows]+[[float(x) for x in row] for row in rows]
print(2*len(rowss))
list.append(new_rows)
for i in range(1, len(rowss) - 1):
    list.append(rowss[i])
    list.append([rowss[i][0]] + [(rowss[i][j] + rowss[i + 1][j]) / 2 for j in range(1, len(rowss[i]))])
list.append(rowss[len(rowss) - 1])
csvfile.close()

csvfile = open('./dataset/datas33333.csv', 'w', newline='')
writer = csv.writer(csvfile)
for row in list:
    writer.writerow(row)
csvfile.close()
