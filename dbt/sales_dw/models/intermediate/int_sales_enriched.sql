select
    *,
    case
        when total_amount >= 300
            then 'high'
        when total_amount >= 100
            then 'medium'
        else 'low'
    end as order_category
from {{ ref('stg_sales') }}