from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.models.base import Base

class Evenement(Base):
    __tablename__ = 'evenements'
    evenementId = Column(Integer, primary_key=True)
    contratId = Column(Integer, ForeignKey('contrat.contratId'))
    date_debut = Column(Date)
    date_fin = Column(Date)
    clientId = Column(Integer, ForeignKey('client.clientId'))
    supportId = Column(Integer, ForeignKey('collaborateur.collaborateurId'), nullable=True)
    lieu = Column(String)
    nombre_invites = Column(Integer)
    note = Column(String)

    contrat = relationship('Contrat', back_populates='evenements')
    client = relationship('Client', back_populates='evenements')
    support = relationship('Collaborateur', back_populates='evenements_support')