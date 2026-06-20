import pandas as pd

# Load data
df = pd.read_csv("data/raw/scheme_performance.csv")

print("Original Shape:", df.shape)

# Convert numeric columns

numeric_cols = [
    "aum_crore",
    "expense_ratio_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove rows with null values in important columns

df = df.dropna(subset=numeric_cols)

# Expense ratio range

df = df[
    (df["expense_ratio_pct"] >= 0.1)
    &
    (df["expense_ratio_pct"] <= 2.5)
]

# AUM should be positive

df = df[df["aum_crore"] > 0]

# Remove duplicates

df = df.drop_duplicates()

print("Final Shape:", df.shape)

# Save cleaned file

df.to_csv(
    "data/processed/scheme_performance_cleaned.csv",
    index=False
)

print("Saved Successfully!")