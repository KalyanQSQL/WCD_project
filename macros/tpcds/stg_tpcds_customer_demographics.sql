{{ config(
    materialized = 'view',
    schema = 'staging'
) }}

SELECT
    cd_demo_sk as demo_sk,
    cd_gender as gender,
    cd_marital_status as marital_status,
    cd_education_status as education_status,
    cd_purchase_estimate as purchase_estimate,
    cd_credit_rating as credit_rating,
    cd_dep_count as dependents_count,
    cd_dep_employed_count as dependents_employed,
    cd_dep_college_count as dependents_in_college,
    _airbyte_normalized_at as airbyte_normalized_at
FROM 
    {{ source('airbyte_raw', 'customer_demographics') }}
