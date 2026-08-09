{{
    config(
        materialized='incremental',
        unique_key='booking_id'
    )
}}

SELECT b.booking_id, p.passenger_sk, f.flight_sk, a.airport_sk, b.amount, b.booking_date
FROM 
{{ source('silver','bookings_silver') }} as b
left join
{{ ref('dim_passengers') }} as p
on b.passenger_id = p.passenger_id
and b.booking_date >= cast(p.valid_from as date)
and(
    b.booking_date < cast(p.valid_to as date)
    or p.valid_to is null
)
left join
{{ ref('dim_flights') }} as f
on b.flight_id = f.flight_id
and b.booking_date >= cast(f.valid_from as date)
and(
    b.booking_date < cast(f.valid_to as date)
    or f.valid_to is null
)
left join
{{ ref('dim_airports') }} as a
on b.airport_id = a.airport_id
and b.booking_date >= cast(a.valid_from as date)
and(
    b.booking_date < cast(a.valid_to as date)
    or a.valid_to is null
)

{% if is_incremental() %}

where b.booking_date > (SELECT max(booking_date) FROM {{ this }})

{% endif %}