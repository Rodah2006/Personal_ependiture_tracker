from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1️⃣ Database URL — where the data will be stored
SQLALCHEMY_DATABASE_URL = "sqlite:///./expenses.db"

# 2️⃣ Create the engine (connects to the database)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # Required only for SQLite
)

# 3️⃣ Create a session (used to talk to the database)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4️⃣ Create Base class (for all models)
Base = declarative_base()
