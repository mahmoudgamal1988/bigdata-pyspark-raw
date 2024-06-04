import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

# Initialize Spark session
spark = SparkSession.builder \
    .appName('IrisClassifier') \
    .config('spark.hadoop.fs.defaultFS', 'hdfs://namenode:9000') \
    .config('spark.executor.memory', '1g') \
    .config('spark.executor.cores', '1') \
    .config('spark.yarn.am.memory', '1g') \
    .getOrCreate()

print("add whatever task you need here")

# Stop Spark session
spark.stop()
