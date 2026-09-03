from pathlib import Path
from ingestion.loader import load_sales

DATA_PATH = Path("data/raw")

def main():

  files = sorted(DATA_PATH.glob("sales_*.csv"))

  if not files:
    print("No sales files found.")
    return

  for file_path in files:
    print(f"Processing {file_path.name}")
    load_sales(file_path)

if __name__ == "__main__":
  main()
