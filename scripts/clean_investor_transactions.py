import pandas as pd

# Load data
df = pd.read_csv("data/raw/investor_transactions.csv")

print("Original Shape:", df.shape)

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .astype(str)
    .str.strip()
    .str.upper()
)

# Keep only valid transaction types
valid_types = ["SIP", "LUMPSUM", "REDEMPTION"]

df = df[df["transaction_type"].isin(valid_types)]

# Amount should be greater than 0
df = df[df["amount_inr"] > 0]

# Convert dates
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# Remove invalid dates
df = df.dropna(subset=["transaction_date"])

# Standardize KYC values
df["kyc_status"] = (
    df["kyc_status"]
    .astype(str)
    .str.strip()
)

# Remove duplicates
df = df.drop_duplicates()

print("Final Shape:", df.shape)

# Save cleaned file
df.to_csv(
    "data/processed/investor_transactions_cleaned.csv",
    index=False
)

print("Saved Successfully!")