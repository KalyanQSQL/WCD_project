-- staging- a view of the customer address table from raw source
{{ config(
    materialized = 'view',
    schema = 'staging'
) }}

select 
    ca_street_name as street_name, 
    ca_suite_number as suite_number,
    ca_location_type as location_type,
    ca_address_sk as address_sk,
    ca_country as country,
    ca_address_id as address_id, 
    ca_county as county,
    ca_street_number as street_number, 
    ca_zip as zip,
    ca_city as city, 
    ca_street_type as street_type, 
    ca_gmt_offset as gmt_offset, 
    _airbyte_normalized_at as airbyte_normalized_at
    from  
        {{source('airbyte_raw', 'customer_address')}}