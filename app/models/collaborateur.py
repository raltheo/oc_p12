from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base


class Collaborateur(Base):
    __tablename__ = 'collaborateur'
    collaborateurId = Column(Integer, primary_key=True)
    role_id = Column(Integer, ForeignKey('role.roleId'))
    password = Column(String)
    userId = Column(Integer, ForeignKey('user.userId'))

    role = relationship('Role', back_populates='collaborateurs', uselist=False)
    
    user = relationship('User', back_populates='collaborateur', uselist=False)
    clients = relationship('Client', back_populates='collaborateur')
    contrats = relationship('Contrat', back_populates='commercial')