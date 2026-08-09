{% snapshot dim_flights_ss %}

{{config(
    target_schema = 'gold',
    unique_key = 'flight_id',
    strategy = 'check',
    check_cols = [
        'airline',
        'origin',
        'destination',
        'flight_date'
    ]
)}}

select
flight_id,
airline,
origin,
destination,
flight_date
from {{source('silver','flights_silver')}}

{% endsnapshot %}