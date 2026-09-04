FROM apache/airflow:3.3.1-python3.12

USER airflow

RUN pip install --no-cache-dir \
    dbt-postgres \
    pandas \
    psycopg2-binary

COPY --chown=airflow:root ingestion /opt/airflow/app/ingestion
COPY --chown=airflow:root pyproject.toml /opt/airflow/app/pyproject.toml

RUN pip install --no-cache-dir /opt/airflow/app