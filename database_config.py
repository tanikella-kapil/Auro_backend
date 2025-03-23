from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define the database URL
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///test.db")  # Use PostgreSQL if needed

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)

# Define Base for ORM models
Base = declarative_base()

# Create session
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Function to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
print(f"Connecting to database: {DATABASE_URL}")
