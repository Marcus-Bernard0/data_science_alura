from pyspark.sql import SparkSession
from pyspark.sql import functions as f

spark = SparkSession.builder.appName("SparkStreaming").getOrCreate()

#variavel para guardar os dados em dataframe
line = spark.readStream\
    .format('socket')\
    .option('host', 'localhost')\
    .option('port', 9009)\
    .load()

#onde será armazenado as functions para tratamento
#explode separar uma string em um array
# ' ' espaço para separação das palavras

words = line.select(f.explode(f.split(line.value, ' ')).alias('word'))

#contabilizando as palavras
wordCounts = words.groupBy('word').count()

#visualizando os dados
# Append - somente novas linhas serão escritas no armazenamento externo
query = wordCounts.writeStream\
    .outputMode('complete')\
    .format('console')\
    .start()

#interromper o fluxo
query.awaitTermination()