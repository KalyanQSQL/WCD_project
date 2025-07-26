{{ config(
    materialized = 'view',
    schema = 'staging'
) }}

SELECT
  cs_warehouse_sk as warehouse_sk,
  cs_ship_date_sk as ship_date_sk,
  cs_ext_list_price as ext_list_price,
  cs_quantity as quantity,
  cs_net_paid_inc_tax as net_paid_inc_tax,
  cs_sold_time_sk as sold_time_sk,
  cs_promo_sk as promo_sk,
  cs_list_price as list_price,
  cs_ext_ship_cost as ext_ship_cost,
  cs_net_paid as net_paid,
  cs_sold_date_sk as sold_date_sk,
  cs_ext_discount_amt as ext_discount_amt,
  cs_ship_addr_sk as ship_addr_sk,
  cs_ext_tax as ext_tax,
  cs_catalog_page_sk as catalog_page_sk,
  cs_net_profit as net_profit,
  cs_item_sk as item_sk,
  cs_bill_cdemo_sk as bill_cdemo_sk,
  cs_bill_hdemo_sk as bill_hdemo_sk,
  cs_wholesale_cost as wholesale_cost,
  cs_sales_price as sales_price,
  cs_call_center_sk as call_center_sk,
  cs_bill_customer_sk as bill_customer_sk,
  _AIRBYTE_NORMALIZED_AT AS AIRBYTE_NORMALIZED_AT
FROM {{ source('airbyte_raw', 'catalog_sales') }}
