from pyspark import SparkContext, SparkConf

conf = SparkConf().setMaster('local').setAppName('Temperature_Converter')
sc = SparkContext(conf=conf)

temperature_in_Fahrenheit = [59, 57.6, 56, 55.4, 55.1, 56.3]
temperature_parallelized = sc.parallelize(temperature_in_Fahrenheit, 2)


def temperature_converter(temperature):
    centigrade = (temperature - 32) * 5 / 9
    return centigrade


temperature_in_Centigrade = temperature_parallelized.map(temperature_converter)
print("temperature_in_Centigrade : ", temperature_in_Centigrade.collect())


# Get temperature greater than 14
final_temperature = temperature_in_Centigrade.filter(lambda x: x > 14)
print(final_temperature.collect())
