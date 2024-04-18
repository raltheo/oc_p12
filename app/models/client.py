from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.models.base import Base
from datetime import datetime


class Client(Base):
    __tablename__ = 'client'
    clientId = Column(Integer, primary_key=True)
    nom_entreprise = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    mise_a_jour = Column(DateTime, onupdate=datetime.now)
    collaborateurId = Column(Integer, ForeignKey('collaborateur.collaborateurId'))
    userId = Column(Integer, ForeignKey('user.userId'))

    collaborateur = relationship('Collaborateur', back_populates='clients')
    contrats = relationship('Contrat', back_populates='client')
    user = relationship('User', back_populates='client', uselist=False)