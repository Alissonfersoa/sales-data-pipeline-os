# Sales Data Engineering Pipeline

End-to-end batch data pipeline demonstrating
modern data engineering practices using
open-source technologies.

## Architecture

CSV
↓
Python
↓
PostgreSQL Raw
↓
dbt Staging
↓
dbt Intermediate
↓
Analytics Mart

Apache Airflow orchestrates the complete workflow.

## Tech Stack

Python
PostgreSQL
dbt Core
Apache Airflow
Docker
Pytest
GitHub Actions

## Engineering Concepts

- Batch ingestion
- ELT architecture
- Incremental loading
- Idempotency
- Data quality
- Data lineage
- Data modeling
- Orchestration
- Containerization
- CI