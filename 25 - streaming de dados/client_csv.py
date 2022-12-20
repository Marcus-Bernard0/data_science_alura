from pyspark.sql import SparkSession
import shutil

#try para não interromper em caso de erro
for item in ['.\check', '.\csv']:
    try:
        shutil.rmtree(item)
    except OSError as err:
        print(f'Aviso: {err.strerror}')

spark = SparkSession.builder.appName("SparkStreaming").getOrCreate()

#variavel para guardar os dados em dataframe
tweets = spark.readStream\
    .format('socket')\
    .option('host', 'localhost')\
    .option('port', 9009)\
    .load()


#visualizando os dados
# Append - somente novas linhas serão escritas no armazenamento externo
query = tweets.writeStream\
    .outputMode('append')\
    .option('encoding','utf-8')\
    .format('csv')\
    .option('path', '.\csv')\
    .option('checkpointLocation', '\.check')\
    .start()

#interromper o fluxo
query.awaitTermination()