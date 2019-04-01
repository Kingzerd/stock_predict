import csv

list = []

csvfile = open('./dataset/000028.csv', newline='')  # 打开一个文件
csvReader = csv.reader(csvfile)  # 返回的可迭代类型
i = 0
for row in csvReader:
    if i > 1:
        list[i - 2].append(row[3])
    i += 1
    list.append(['sh000028', row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]])
csvfile.close()

csvfile = open('./dataset/newdataset.csv', 'w', newline='')
writer = csv.writer(csvfile)
for row in list:
    writer.writerow(row)
# writer.writerow(('编号', '网址', '关键字'))
# ss= [
#  ('1', 'http://nnzhp.cn/', '牛牛'),
#  ('2', 'http://www.baidu.com/', '百度'),
#  ('3', 'http://www.jd.com/', '京东')
# ]
# writer.writerows(list)
csvfile.close()
