import warnings
warnings.filterwarnings('ignore')
from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf = conf)
lines = sc.textFile("/home/my_hduser/BigData/Big-Data-Hadoop/Apache Pig/Word_Count/input.txt")
print(lines)
ratings = lines.map(lambda x: x.split()[2])
result = ratings.countByValue()

sortedResults = collections.OrderedDict(sorted(result.items()))
for key, value in sortedResults.items():
    print("%s %i" % (key, value))



