# read_csv
import os
import pandas as pd # pyright: ignore[reportMissingModuleSource]

csv_path = r"C:\Users\Asus\Downloads\F1Drivers_Dataset.csv"

if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
    print("✅:")
    print(df.head())
    print(df.info())
else:
    print(f"⚠️ : {csv_path}")
