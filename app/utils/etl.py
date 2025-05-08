import pandas as pd

# Function to ETL the data
def etl(file):
    df = pd.read_csv(file).drop_duplicates().dropna()
    df['date'] = pd.to_datetime(df['date'])
    df['amount'] = df['amount'].astype(float)
    df['description'] = df['description'].str.strip()
    df['category'] = df['category'].str.strip()
