select *
from {{ ref('fct_daily_sales') }}
where revenue <= 0