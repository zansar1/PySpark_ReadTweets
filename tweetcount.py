from pyspark.sql import SparkSession

# create a SparkSession
spark = SparkSession.builder.appName("TweetStateCount").getOrCreate()

# read the tweets dataset into a Spark DataFrame
tweets_df = spark.read.json("tweets.json")

# read the city-state lookup table into a Spark DataFrame
city_state_df = spark.read.json("cityStateMap.json")

# join the two DataFrames on the 'geo' column
joined_df = tweets_df.join(city_state_df, tweets_df.geo == city_state_df.city)

# group by state and count the number of tweets
state_count_df = joined_df.groupBy("state").count().orderBy("state")

# show the results
state_count_df.show()
