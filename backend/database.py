# backend/database.py

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Create the database engine
engine = create_engine(DATABASE_URL, echo=True)  # echo=True logs SQL commands

# Create a session local class so we can instantiate sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)