from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from pathlib import Path
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)
load_dotenv()

SQLALCHAMY_DATABASE = os.getenv("SQLALCHAMY_DATABASE_URL")
engine = create_engine(SQLALCHAMY_DATABASE,connect_args={"check_same_thread":False})

SessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False,)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()