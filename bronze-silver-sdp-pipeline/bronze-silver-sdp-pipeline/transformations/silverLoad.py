from pyspark import pipelines as dp
from pyspark.sql.functions import *
from pyspark.sql.types import *

rules_bookings = {
    "rule1" : "booking_id is not null",
    "rule2" : "passenger_id is not null",
    "rule3" : "airport_id is not null",
    "rule4" : "flight_id is not null",
    "rule5" : "amount > 0"
}

@dp.expect_all_or_fail(rules_bookings)
@dp.table(
    name = "flightsystem.silver.bookings_silver"
)
def bookings_silver():
    df = spark.readStream.table("flightsystem.bronze.bookings_bronze")
    df = df.dropna(how = 'all',subset=["booking_id","passenger_id","flight_id","airport_id","amount","booking_date"])
    df = df.withColumn("amount",col("amount").cast("double"))
    df = df.withColumn("booking_date",col("booking_date").cast("date"))
    df = df.dropDuplicates(subset = ["booking_id"])
    df = df.withColumn("last_updated",current_timestamp())
    return df

rules_airports = {
    "rule" : "airport_id is not null"
}

@dp.expect_all_or_fail(rules_airports)
@dp.table(
    name = "flightsystem.silver.airports_silver"
)
def airports_silver():
    df = spark.readStream.table("flightsystem.bronze.airports_bronze")
    df = df.withColumn("airport_name",initcap(col("airport_name")))
    df = df.withColumn("city",initcap(col("city")))
    df = df.withColumn("country",initcap(col("country")))
    return df

rules_flights = {
    "rule1" : "flight_id is not null"
}

@dp.expect_all_or_fail(rules_flights)
@dp.table(
    name = "flightsystem.silver.flights_silver"
)
def flights_silver():
    df = spark.readStream.table("flightsystem.bronze.flights_bronze")
    df = df.withColumn("flight_date",col("flight_date").cast("date"))
    df = df.withColumn("airline",initcap(col("airline")))
    df = df.withColumn("origin",initcap(col("origin")))
    df = df.withColumn("destination",initcap(col("destination")))
    df = df.dropDuplicates(subset=["flight_id"])
    return df

rules_passengers = {
    "rule" : "passenger_id is not null"
}
@dp.expect_all_or_fail(rules_passengers)
@dp.table(
    name = "flightsystem.silver.passengers_silver"
)
def passengers_silver():
    df = spark.readStream.table("flightsystem.bronze.passengers_bronze")
    df = df.withColumn("name",initcap(col("name")))
    df = df.withColumn("gender",initcap(col("gender")))
    df = df.withColumn("nationality",initcap(col("nationality")))
    df = df.dropDuplicates(subset=["passenger_id"])
    return df