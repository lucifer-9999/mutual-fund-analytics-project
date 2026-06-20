import pandas as pd

# Load data

df = pd.read_csv("data/raw/nav_history.csv")

print(df.shape)


# Convert date column

df["date"] = pd.to_datetime(df["date"])


# Sort

df = df.sort_values(
    by=["amfi_code","date"]
)


# Fill missing NAV

df["nav"] = df.groupby(
    "amfi_code"
)["nav"].ffill()


# Remove duplicates

df.drop_duplicates(inplace=True)


# Keep only NAV > 0

df = df[df["nav"] > 0]


print(df.shape)


# Save cleaned file

df.to_csv(
    "data/processed/nav_history_cleaned.csv",
    index=False
)

print("Saved Successfully")