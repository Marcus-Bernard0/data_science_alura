from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SparkStreaming").getOrCreate()

#variavel para guardar os dados em dataframe
line = spark.readStream\
    .format('socket')\
    .option('host', 'localhost')\
    .option('port', 9009)\
    .load()

#visualizando os dados
# Append - somente novas linhas serão escritas no armazenamento externo
query = line.writeStream\
    .outputMode('append')\
    .format('console')\
    .start()

#interromper o fluxo
query.awaitTermination()