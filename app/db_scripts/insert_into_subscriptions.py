import pandas as pd
from sqlalchemy import create_engine
from app.database.create_database_connection import engine

def hex_to_bytes(value):

    if pd.isna(value):
        return None

    value = str(value).strip()

    if value.lower().startswith("0x"):
        value = value[2:]

    return bytes.fromhex(value)

def insert_subscriptions():

    df = pd.read_excel("/Users/saloniswetambra/Documents/Python_and_AIML_Code/Projects/data/subscriptions.xlsx")
    print(df.head())

    df["subscription_id"] = df["subscription_id"].apply(hex_to_bytes) 
    df["user_id"] = df["user_id"].apply(hex_to_bytes)
    df["start_date"] = pd.to_datetime( df["start_date"].astype(str).str.strip(), format="mixed", utc=True ).dt.date 
    df["end_date"] = pd.to_datetime( df["end_date"].astype(str).str.strip(), format="mixed", utc=True ).dt.date
    df["created_at"] = pd.to_datetime( df["created_at"].astype(str).str.strip(), format="mixed", utc=True ).dt.tz_localize(None)
    # Insert into mysql
    df.to_sql(
        "subscriptions",
        con=engine,
        if_exists="append",
        index=False
    )

if __name__ == "__main__":
    insert_subscriptions()