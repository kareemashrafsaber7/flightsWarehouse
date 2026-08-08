CREATE SCHEMA gold;


CREATE TABLE gold.dim_passengers(
    passenger_sk VARCHAR(100),
    passenger_id VARCHAR(100),
    name VARCHAR(200),
    nationality VARCHAR(200),
    gender VARCHAR(50),
    valid_from DATETIME2,
    valid_to DATETIME2
)
WITH
(
    DISTRIBUTION = ROUND_ROBIN,
    CLUSTERED COLUMNSTORE INDEX
);

CREATE TABLE gold.dim_flights(
    flight_sk VARCHAR(100),
    flight_id VARCHAR(100),
    airline VARCHAR(50),
    origin VARCHAR(50),
    destination VARCHAR(50),
    flight_date DATE,
    valid_from DATETIME2,
    valid_to DATETIME2
)
WITH
(
    DISTRIBUTION = ROUND_ROBIN,
    CLUSTERED COLUMNSTORE INDEX
);

CREATE TABLE gold.dim_airports(
    airport_sk VARCHAR(100),
    airport_id VARCHAR(100),
    airport_name VARCHAR(200),
    city VARCHAR(150),
    country VARCHAR(200),
    valid_from DATETIME2,
    valid_to DATETIME2
)
WITH
(
    DISTRIBUTION = ROUND_ROBIN,
    CLUSTERED COLUMNSTORE INDEX
);

CREATE TABLE gold.fact_bookings(
    booking_id VARCHAR(200),
    passenger_sk VARCHAR(100),
    flight_sk VARCHAR(100),
    airport_sk VARCHAR(100),
    amount DECIMAL(10,2),
    booking_date DATE
)
WITH
(
    DISTRIBUTION = ROUND_ROBIN,
    CLUSTERED COLUMNSTORE INDEX
);