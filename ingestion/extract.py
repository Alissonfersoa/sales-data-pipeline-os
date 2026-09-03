from pathlib import Path
import pandas as pd

REQUIRED_COLUMNS =[
  "order_id",
  "customer_id",
  "product_id",
  "quantity",
  "unit_price",
  "order_date",
]

def extract_csv(file_path: Path) -> pd.DataFrame:

  df = pd.read_csv(file_path)
  missing_columns = set(REQUIRED_COLUMNS) - set(df.columns)

  if missing_columns:
    raise ValueError(
      f"Missing required columns: {missing_columns}"
    )

  return df