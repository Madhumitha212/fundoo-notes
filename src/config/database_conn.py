"""
Database connection configuration for Fundoo Notes project.
"""
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Load environment variables from .env
load_dotenv()

# Database credentials
USERNAME = os.getenv("DB_USERNAME")
PASSWORD = os.getenv("DB_PASSWORD")
IP = os.getenv("IP")          # e.g. ACER
PORT = os.getenv("PORT_NUMBER")  # e.g. 1433
DATABASE = os.getenv("DATABASE")
DRIVER = os.getenv("DRIVER")  # e.g. ODBC Driver 17 for SQL Server

# Build connection string
DATABASE_URL = (
    f"mssql+pyodbc://{USERNAME}:{PASSWORD}@{IP},{PORT}/"
    f"{DATABASE}?driver=ODBC+Driver+17+for+SQL+Server"
)

# Engine creation
engine = create_engine(DATABASE_URL)

# Session creation
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    """
    Provides database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

