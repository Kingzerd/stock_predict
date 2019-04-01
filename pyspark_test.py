from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster("local[*]").setAppName("First_App")
sc = SparkContext(conf=conf)
data = sc.parallelize(range(10))
ans = data.reduce(lambda x, y: x + y)
print (ans)