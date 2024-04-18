from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.models.base import Base

class Contrat(Base):
    __tablename__ = 'contrat'
    contratId = Column(Integer, primary_key=True)
    clientId = Column(Integer, ForeignKey('client.clientId'))
    commercialID = Column(Integer, ForeignKey('collaborateur.collaborateurId'))
    montant_total = Column(Integer)
    montant_restant = Column(Integer)
    date_created = Column(Date)
    status_contrat = Column(String)

    client = relationship('Client', back_populates='contrats')
    commercial = relationship('Collaborateur', back_populates='contrats')
    evenements = relationship('Evenement', back_populates='contrat')