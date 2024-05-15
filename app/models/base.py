from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.settings import DB_PORT, DB_HOST, DB_NAME, DB_PASSWORD, DB_USER

Base = declarative_base()

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=False) # mettre echo = True si je veux debug logs

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)