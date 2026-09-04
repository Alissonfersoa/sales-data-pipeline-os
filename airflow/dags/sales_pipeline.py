from datetime import datetime

from airflow.sdk import DAG, task
from airflow.providers.standard.operators.bash import BashOperator


default_args = {
    "retries": 2,
}


with DAG(
    dag_id="sales_data_pipeline",
    start_date=datetime(2026, 8, 1),
    schedule=None,
    catchup=False,
    tags=["portfolio", "data-engineering"],
    default_args=default_args,
) as dag:

    @task
    def start():
        print("Starting sales pipeline")

    @task
    def ingest():
        from ingestion.main import main
        main()

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="""
        cd /opt/airflow/dbt/sales_dw &&
        dbt run --profiles-dir .
        """,
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command="""
        cd /opt/airflow/dbt/sales_dw &&
        dbt test --profiles-dir .
        """,
    )

    start() >> ingest() >> dbt_run >> dbt_test