from sqlalchemy import Column, Integer, String 
from sqlalchemy.orm import relationship
from app.models.base import Base

class Role(Base):
    __tablename__ = 'role'
    roleId = Column(Integer, primary_key=True)
    nom = Column(String)
    description = Column(String)

    collaborateurs = relationship('Collaborateur', back_populates='role')