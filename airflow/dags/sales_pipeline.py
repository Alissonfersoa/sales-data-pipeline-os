from datetime import datetime
from airflow import DAG, task

with DAG(
    dag_id="sales_data_pipeline",
    start_date=datetime(2026, 8, 1),
    schedule="@daily",
    catchup=False,
    tags=["portfolio", "data-engineering"],
) as dag:

    @task
    def start():
        print("Starting sales pipeline")

    @task
    def ingest():
        from ingestion.main import main

        main()

    @task.bash
    def dbt_run():
        return """
        cd /opt/airflow/dbt/sales_dw &&
        dbt run --profiles-dir .
        """

    @task.bash
    def dbt_test():
        return """
        cd /opt/airflow/dbt/sales_dw &&
        dbt test --profiles-dir .
        """

    start() >> ingest() >> dbt_run() >> dbt_test()