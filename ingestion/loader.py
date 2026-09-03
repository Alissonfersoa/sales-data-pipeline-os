from pathlib import Path
from psycopg2.extras import execute_values
from ingestion.database import get_connection
from ingestion.extract import extract_csv

def load_sales(file_path: Path):

  df = extract_csv(file_path)
  df["source_file"] = file_path.name

  records = df[
    [
      "order_id",
      "customer_id",
      "product_id",
      "quantity",
      "unit_price",
      "order_date",
      "source_file",
    ]
  ].values.tolist()

  query = """
      INSERT INTO raw.sales(
          order_id,
          customer_id,
          product_id,
          quantity,
          unit_price,
          order_date,
          source_file
      )
      VALUES %s
      ON CONFLICT (order_id)

      DO UPDATE SET

          customer_id = EXCLUDED.customer_id,
          product_id = EXCLUDED.product_id,
          quantity = EXCLUDED.quantity,
          unit_price = EXCLUDED.unit_price,
          order_date = EXCLUDED.order_date,
          source_file = EXCLUDED.source_file;
"""
  conn = get_connection()

  try:
    with conn.cursor() as cursor:
      execute_values(cursor, query, records)
    conn.commit()

    print(
      f"{len(records)} records loaded from {file_path.name}"
    )
  except Exception:
    conn.rollback()
    raise

  finally:
    conn.close()