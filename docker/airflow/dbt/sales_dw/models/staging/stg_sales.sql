select
    order_id,
    customer_id,
    upper(product_id) as product_id,
    quantity,
    unit_price,
    quantity * unit_price as total_amount,
    order_date,
    ingestion_timestamp,
    source_file
from {{ source('raw', 'sales') }}
where quantity > 0
  and unit_price > 0