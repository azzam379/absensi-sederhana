# File: backend/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Tautan Cloud Postgres dari Neon
SQLALCHEMY_DATABASE_URL = "postgresql://neondb_owner:npg_I0mvGkAbTo2B@ep-silent-hall-ao75qz51-pooler.c-2.ap-southeast-1.aws.neon.tech/neondb?sslmode=require"

# Engine Postgres tidak butuh connect_args
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency untuk mendapatkan session DB di FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
