from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.base import Base

class User(Base):
    __tablename__ = 'user'
    userId = Column(Integer, primary_key=True)
    nom = Column(String)
    email = Column(String)
    telephone = Column(String)

    collaborateur = relationship('Collaborateur', back_populates='user', uselist=False)
    client = relationship('Client', back_populates='user', uselist=False)