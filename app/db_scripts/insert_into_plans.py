import pandas as pd
import uuid
from sqlalchemy import create_engine
from app.database.create_database_connection import engine

def insert_plans():

    df = pd.read_excel("/Users/saloniswetambra/Documents/Python_and_AIML_Code/Projects/data/plans.xlsx")
    print(df.head())

    # Insert into mysql
    df.to_sql(
        "plans",
        con=engine,
        if_exists="append",
        index=False
    )

if __name__ == "__main__":
    insert_plans()