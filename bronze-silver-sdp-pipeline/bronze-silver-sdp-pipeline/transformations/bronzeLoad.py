from pyspark import pipelines as dp
from pyspark.sql.functions import *
from pyspark.sql.types import *


@dp.table
def airports_bronze():
    df = spark.readStream.format("cloudFiles")\
        .option("cloudFiles.format","csv")\
            .option("cloudFiles.schemaLocation","abfss://raw@flightstorage100.dfs.core.windows.net/raw_csv/airports/checkpoint/")\
                .option("cloudFiles.schemaEvolutionMode","rescue")\
                    .load("abfss://raw@flightstorage100.dfs.core.windows.net/raw_csv/airports/")
    return df



@dp.table
def bookings_bronze():
    df = spark.readStream.format("cloudFiles")\
        .option("cloudFiles.format","csv")\
            .option("cloudFiles.schemaLocation","abfss://raw@flightstorage100.dfs.core.windows.net/raw_csv/bookings/checkpoint/")\
                .option("cloudFiles.schemaEvolutionMode","rescue")\
                    .load("abfss://raw@flightstorage100.dfs.core.windows.net/raw_csv/bookings/")
    return df


@dp.table
def flights_bronze():
    df = spark.readStream.format("cloudFiles")\
        .option("cloudFiles.format","csv")\
            .option("cloudFiles.schemaLocation","abfss://raw@flightstorage100.dfs.core.windows.net/raw_csv/flights_scd/checkpoint/")\
                .option("cloudFiles.schemaEvolutionMode","rescue")\
                    .load("abfss://raw@flightstorage100.dfs.core.windows.net/raw_csv/flights_scd/")
    return df
    
@dp.table
def passengers_bronze():
    df = spark.readStream.format("cloudFiles")\
        .option("cloudFiles.format","csv")\
            .option("cloudFiles.schemaLocation","abfss://raw@flightstorage100.dfs.core.windows.net/raw_csv/passengers_scd/checkpoint/")\
                .option("cloudFiles.schemaEvolutionMode","rescue")\
                    .load("abfss://raw@flightstorage100.dfs.core.windows.net/raw_csv/passengers_scd/")
    return df