{% snapshot dim_airports_ss %}

{{config(
    target_schema = 'gold',
    unique_key = 'airport_id',
    strategy = 'check',
    check_cols = [
        'airport_name',
        'city',
        'country'
    ]
)}}


select 
airport_id,
airport_name,
city,
country
from {{source('silver','airports_silver')}}

{% endsnapshot %}