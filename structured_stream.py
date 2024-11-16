from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split
from fetch import fetch_comments
import time




def start_streaming(api_key,video_id):
    spark = SparkSession.builder.appName("stream").getOrCreate()
    comment_stream=spark.readStream \
        .format("socket") \
        .option("host","localhost") \
        .option("port","9999") \
        .load()
    

    #words_df = df.select(explode(split(df.comment, " ")).alias("word"))
    #word_count = words_df.groupBy("word").count()

    words_df = comment_stream.select(explode(split(comment_stream.value, " ")).alias("word"))
    word_count = words_df.groupBy("word").count()




    query = word_count.writeStream \
        .outputMode("complete") \
        .format("console") \
        .start()


    query.awaitTermination() 



  
    
    
    


