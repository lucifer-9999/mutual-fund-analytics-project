import pandas as pd
from pathlib import Path

# Folder containing all CSV files
data_path = Path("data/Raw")

# Get all CSV files
files = list(data_path.glob("*.csv"))

print(f"Files found: {len(files)}")
print(files)

for file in files:
    print("\n" + "=" * 60)
    print(f"Dataset: {file.name}")

    df = pd.read_csv(file)

    print(f"Shape: {df.shape}")

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nFirst 5 Rows:")
    print(df.head())