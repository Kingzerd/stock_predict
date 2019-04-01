import csv

list = []

csvfile = open('./dataset/datas1111.csv', newline='')  # 打开一个文件
csvReader = csv.reader(csvfile)  # 返回的可迭代类型
rows = [row for row in csvReader]
new_rows = rows.pop(0)
rowss1 = [new_rows]+[[float(x) for x in row] for row in rows]
list.append(new_rows)
csvfile.close()

csvfile = open('./dataset/datas2222.csv', newline='')  # 打开一个文件
csvReader = csv.reader(csvfile)  # 返回的可迭代类型
rows = [row for row in csvReader]
new_rows = rows.pop(0)
rowss2 = [new_rows]+[[float(x) for x in row] for row in rows]
csvfile.close()

csvfile = open('./dataset/datas3333.csv', newline='')  # 打开一个文件
csvReader = csv.reader(csvfile)  # 返回的可迭代类型
rows = [row for row in csvReader]
new_rows = rows.pop(0)
rowss3 = [new_rows]+[[float(x) for x in row] for row in rows]
csvfile.close()

csvfile = open('./dataset/datas4444.csv', newline='')  # 打开一个文件
csvReader = csv.reader(csvfile)  # 返回的可迭代类型
rows = [row for row in csvReader]
new_rows = rows.pop(0)
rowss4 = [new_rows]+[[float(x) for x in row] for row in rows]
csvfile.close()

csvfile = open('./dataset/datas5555.csv', newline='')  # 打开一个文件
csvReader = csv.reader(csvfile)  # 返回的可迭代类型
rows = [row for row in csvReader]
new_rows = rows.pop(0)
rowss5 = [new_rows]+[[float(x) for x in row] for row in rows]
csvfile.close()

for i in range(1, len(rowss1) - 1):
    tmp = []
    tmp.append(int(rowss1[i][0]))
    tmp.append(float(rowss1[i][6]))
    tmp.append(float(rowss2[i][6]))
    tmp.append(float(rowss3[i][6]))
    tmp.append(float(rowss4[i][6]))
    tmp.append(float(rowss5[i][6]))
    list.append(tmp)

csvfile = open('./dataset/final_data.csv', 'w', newline='')
writer = csv.writer(csvfile)
for row in list:
    writer.writerow(row)
csvfile.close()