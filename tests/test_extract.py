import pandas as pd
import pytest

from ingestion.extract import extract_csv

def test_extract_valid_csv(tmp_path):

  file_path = tmp_path / "sales.csv"

  df = pd.DataFrame(
    {
      "order_id": [1],
      "customer_id": [10],
      "product_id": ["P001"],
      "quantity": [2],
      "unit_price": [10],
      "order_date": ["2026-08-01"],
    }
  )

  df.to_csv(file_path, index=False)

  result = extract_csv(file_path)
  assert len(result) == 1

def test_extract_missing_columns(tmp_path):

  file_path = tmp_path / "sales.csv"

  pd.DataFrame({
    "order_id": [1]
  }).to_csv(file_path, index=False,)

  with pytest.raises(ValueError):
    extract_csv(file_path)
    