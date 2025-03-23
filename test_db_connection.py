from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

DATABASE_URL = "postgresql://postgres:pokemon27@localhost:5432/postgres"  # Ensure it's correct

engine = create_engine(DATABASE_URL)

# Test the connection
try:
    with engine.connect() as connection:
        print("✅ Successfully connected to the database!")
except OperationalError as e:
    print("❌ Connection failed:", e)
