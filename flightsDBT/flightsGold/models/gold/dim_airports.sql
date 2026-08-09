select
{{dbt_utils.generate_surrogate_key(['airport_id','dbt_valid_from'])}} as airport_sk,
airport_id,
airport_name,
city,
country,
dbt_valid_from as valid_from,
dbt_valid_to as valid_to
from {{ref('dim_airports_ss')}}