import requests
import pandas as pd
from pathlib import Path

SCHEME_CODE = 125497  # HDFC Top 100

url = f"https://api.mfapi.in/mf/{SCHEME_CODE}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    output_path = Path("data/raw/hdfc_top100_nav.csv")

    nav_df.to_csv(output_path, index=False)

    print("NAV data saved successfully!")
    print(nav_df.head())

else:
    print("Failed to fetch data")