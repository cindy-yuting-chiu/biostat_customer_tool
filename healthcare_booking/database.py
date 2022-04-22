"""This file creates a local database session."""
# Import SQLAlchemy parts.
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Create a database URL for SQLAlchemy.
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# Create the SQLAlchemy engine.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a database session.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Initialize base class to create ORM models.
Base = declarative_base()
