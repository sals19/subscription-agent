from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import (
        DB_HOST, 
        DB_NAME, 
        DB_PORT, 
        DB_USER, 
        DB_PASSWORD
    )

DATABASE_URL = (
        f"mysql+pymysql://"
        f"{DB_USER}:{DB_PASSWORD}@"
        f"{DB_HOST}:{DB_PORT}/"
        f"{DB_NAME}"
    )

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)