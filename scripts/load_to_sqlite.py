import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database

engine = create_engine("sqlite:///bluestock_mf.db")

# Read cleaned files

nav = pd.read_csv(
    "data/processed/nav_history_cleaned.csv"
)

investor = pd.read_csv(
    "data/processed/investor_transactions_cleaned.csv"
)

scheme = pd.read_csv(
    "data/processed/scheme_performance_cleaned.csv"
)

# Load to database

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

investor.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

scheme.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("All tables loaded successfully!")