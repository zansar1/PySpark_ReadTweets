# PySpark_ReadTweets

This is a simple PySpark application that reads in two JSON files, performs a join operation on them, and then counts the number of tweets per state.
Getting Started

To run this application, you will need to have PySpark installed on your machine. You can download it from the official Apache Spark website: https://spark.apache.org/downloads.html.
Usage

    Clone the repository to your local machine.
    Place the tweets.json and cityStateMap.json files in the same directory as the Python script.
    Open a terminal and navigate to the directory containing the Python script and JSON files.
    Run the following command: spark-submit tweet_state_count.py
    The results will be displayed in the console.

Dependencies

This application requires PySpark to be installed on your machine.
Note

This code assumes that the tweets.json file contains a geo field that corresponds to a city in the United States. The cityStateMap.json file is a lookup table that maps cities to states.
License

This project is licensed under the MIT License - see the LICENSE file for details.
