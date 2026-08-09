select
{{dbt_utils.generate_surrogate_key([
    'flight_id',
    'dbt_valid_from'
])}} as flight_sk,
flight_id,
airline,
origin,
destination,
flight_date,
dbt_valid_from as valid_from,
dbt_valid_to as valid_to
from
{{ref('dim_flights_ss')}}