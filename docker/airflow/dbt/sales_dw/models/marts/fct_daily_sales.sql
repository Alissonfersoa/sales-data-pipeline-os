select
    order_date,
    count(distinct order_id) as total_orders,
    sum(quantity) as total_units,
    sum(total_amount) as revenue,
    avg(total_amount) as average_order_value
from {{ ref('int_sales_enriched') }}
group by order_date