import pandas as pd
import uuid
from sqlalchemy import create_engine
from app.database.create_database_connection import engine

def insert_users():

    df = pd.read_excel("/Users/saloniswetambra/Documents/Python_and_AIML_Code/Projects/data/users.xlsx")
    print(df.head())

    # Convert UUID strings to 16 byte binary values
    df["user_id"] = df["user_id"].apply(
        lambda x: uuid.UUID(str(x)).bytes
    )
    # Insert into mysql
    df.to_sql(
        "users",
        con=engine,
        if_exists="append",
        index=False
    )

if __name__ == "__main__":
    insert_users()