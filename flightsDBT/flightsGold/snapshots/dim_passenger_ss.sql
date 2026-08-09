{% snapshot dim_passenger_ss %}

{{
    config(
        target_schema = 'gold',
        unique_key = 'passenger_id',
        strategy = 'check',
        check_cols = [
            'name',
            'gender',
            'nationality'
        ]
    )
}}

SELECT passenger_id, name, nationality, gender
from {{ source('silver','passengers_silver') }}

{% endsnapshot %}