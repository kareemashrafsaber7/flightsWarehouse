# Databricks notebook source
df_bookings = spark.table("flightsystem.gold.fact_bookings")

synapse_url = "jdbc:sqlserver://flightssynpase.sql.azuresynapse.net:1433;database=flightsDW"

df_bookings.write \
    .format("sqlserver") \
    .option("host", "flightssynpase.sql.azuresynapse.net") \
    .option("port", "1433") \
    .option("database", "flightsDW") \
    .option("dbtable", "gold.fact_bookings") \
    .option("user", "kareemashraf") \
    .option("password", "") \
    .mode("append") \
    .save()

# COMMAND ----------

df_airports = spark.table("flightsystem.gold.dim_airports")

synapse_url = "jdbc:sqlserver://flightssynpase.sql.azuresynapse.net:1433;database=flightsDW"

df_airports.write \
    .format("sqlserver") \
    .option("host", "flightssynpase.sql.azuresynapse.net") \
    .option("port", "1433") \
    .option("database", "flightsDW") \
    .option("dbtable", "gold.dim_airports") \
    .option("user", "kareemashraf") \
    .option("password", "") \
    .mode("append") \
    .save()

# COMMAND ----------

df_flights = spark.table("flightsystem.gold.dim_flights")

synapse_url = "jdbc:sqlserver://flightssynpase.sql.azuresynapse.net:1433;database=flightsDW"

df_flights.write \
    .format("sqlserver") \
    .option("host", "flightssynpase.sql.azuresynapse.net") \
    .option("port", "1433") \
    .option("database", "flightsDW") \
    .option("dbtable", "gold.dim_flights") \
    .option("user", "kareemashraf") \
    .option("password", "") \
    .mode("append") \
    .save()

# COMMAND ----------

df_passengers = spark.table("flightsystem.gold.dim_passengers")

synapse_url = "jdbc:sqlserver://flightssynpase.sql.azuresynapse.net:1433;database=flightsDW"

df_passengers.write \
    .format("sqlserver") \
    .option("host", "flightssynpase.sql.azuresynapse.net") \
    .option("port", "1433") \
    .option("database", "flightsDW") \
    .option("dbtable", "gold.dim_passengers") \
    .option("user", "kareemashraf") \
    .option("password", "") \
    .mode("append") \
    .save()