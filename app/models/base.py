from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

DATABASE_URL = "postgresql://postgres:root@localhost:5432/epicevents"

engine = create_engine(DATABASE_URL, echo=False) # mettre echo = True si je veux debug logs

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)