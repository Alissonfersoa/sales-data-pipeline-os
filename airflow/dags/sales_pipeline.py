from datetime import datetime
from airflow.sdk import DAG, task


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