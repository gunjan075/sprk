from pyspark.sql import SparkSession
from pyspark import SparkConf
conf=SparkConf()


spark=SparkSession.builder.appName('hh').master('local[*]').getOrCreate()

print(spark)

df1=spark.read.csv("../Data/titanic.csv")
df1.show(5,False)
