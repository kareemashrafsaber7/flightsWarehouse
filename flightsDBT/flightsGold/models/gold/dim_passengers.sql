select 
{{ dbt_utils.generate_surrogate_key([
    'passenger_id',
    'dbt_valid_from'
]) }} as passenger_sk,
passenger_id,
name,
nationality,
gender,
dbt_valid_from as valid_from,
dbt_valid_to as valid_to

from {{ ref('dim_passenger_ss') }}