import csv
import numpy as np
import xlrd

data = xlrd.open_workbook('./dataset/datas33.xlsx')
table = data.sheets()[0]
# print(table)
nrows = table.nrows  # 行数
ncols = table.ncols  # 列数
# c1=arange(0,nrows,1)
# print(c1)

start = 1  # 开始的行
end = 21  # 结束的行

list_values = []
list_values.append(['date', 'r1', 'r2', 'r3', 'r4', 'r5','r6'])
for x in range(start, nrows-5):
    row = table.row_values(x)
    list_values.append([float(row[1]), float(row[2]), float(row[3])/100, float(row[4])/100, float(row[5]), float(row[6]), 100000-(float(row[2]) + float(row[3]) + float(row[4]) + float(row[5]) + float(row[6]))])
# print(list_values)


csvfile = open('./dataset/datas33.csv', 'w', newline='')
writer = csv.writer(csvfile)
for row in list_values:
    writer.writerow(row)
csvfile.close()
