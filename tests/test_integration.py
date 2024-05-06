import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from datetime import datetime
import pytest
from app.controllers.collaborateur import create_collaborateur, delete_collaborateur, liste_collaborateur, update_collaborateur, delete_collaborateur
from app.controllers.client import create_client, update_client, delete_client, liste_client
from app.controllers.contrat import create_contrat, liste_contrat, delete_contrat, update_contrat
from app.controllers.evenement import create_evenement, delete_evenement, update_evenement, liste_evenement
from app.controllers.auth import login
from app.models.base import SessionLocal


session = SessionLocal()

class test_gestion:

    def login(self):
        login(session, "gestion@example.com", "gestion")

    def create_collab(self):
        res, mess = create_collaborateur(session, "gestion_test" , "gestion_test@gestion.com", "12345", "gestion", "password")
        assert "✔️" in mess

    def update_collab(self):
        data = liste_collaborateur(session)
        for x in data:
            if x[2] == "gestion_test@gestion.com":
                id_collab = x[0]
        res, mess = update_collaborateur(session, id_collab, 1, "updated_name")
        assert "✔️" in mess

    def delete_collab(self):
        data = liste_collaborateur(session)
        for x in data:
            if x[2] == "gestion_test@gestion.com":
                id_collab = x[0]
        res, mess = delete_collaborateur(session, id_collab)
        assert "✔️" in mess

    def cre_contrat(self):
        data = liste_client(session)
        for x in data:
            if x[2] == "test_commercial@ac.com":
                id_client = x[0]
        res, mess = create_contrat(session, id_client, 123456789, 123456789, "signed")
        assert "✔️" in mess

    def del_contrat(self):
        data = liste_contrat(session)
        for x in data:
            if x[1] == "test_commercial@ac.com":
                id_contrat = x[0]
        res, mess = delete_contrat(session, id_contrat)
        assert "✔️" in mess

    def up_evenement(self):
        data = liste_evenement(session)
        for x in data:
            if x[4] == "test_commercial@ac.com":
                id_ev = x[0]
        cols = liste_collaborateur(session)
        for x in cols:
            if x[4] == "support":
                id_support = x[0]
                break
        res, mess = update_evenement(session, id_ev, 3, id_support)
        assert "✔️" in mess

class test_commercial:
    def login(self):
        login(session, "commercial@example.com", "commercial")

    def create_client(self):
        res, mess = create_client(session, "test_commercial", "test_commercial@ac.com", "123456789","fake")
        assert "✔️" in mess

    def update_client(self):
        data = liste_client(session)
        for x in data:
            if x[2] == "test_commercial@ac.com":
                id_client = x[0]
        res, mess = update_client(session, id_client, 1, "updated_name")
        assert "✔️" in mess

    def delete_client(self):
        data = liste_client(session)
        for x in data:
            if x[2] == "test_commercial@ac.com":
                id_client = x[0]
        res, mess = delete_client(session, id_client)
        assert "✔️" in mess

    def update_contrat(self):
        data = liste_contrat(session)
        for x in data:
            if x[1] == "test_commercial@ac.com":
                id_contrat = x[0]
        res, mess = update_contrat(session, id_contrat, 3, "unsigned")
        assert "✔️" in mess

    def cre_evenement(self):
        data = liste_contrat(session)
        for x in data:
            if x[1] == "test_commercial@ac.com":
                id_contrat = x[0]
        res, mess = create_evenement(session, 
                         id_contrat, 
                         datetime.strptime("27/10/2024" ,'%d/%m/%Y').strftime('%Y-%m-%d'), 
                         datetime.strptime("30/10/2024",'%d/%m/%Y').strftime('%Y-%m-%d'),
                         "paris",
                         None,
                         50,
                         "test"
                         )
        assert "✔️" in mess

    def del_evenement(self):
        data = liste_evenement(session)
        for x in data:
            if x[4] == "test_commercial@ac.com":
                id_ev = x[0]
        res, mess = delete_evenement(session, id_ev)

def test():
    """
    Actuellement check :
        - creation, modification, suppression collaborateur
        - creation, modification, suppression client
        - creation, suppression contrat
        - creation, modification, suppression evenement
        - login, affichage de clients, collaborateurs, contrat, evenement
    """
    gestion = test_gestion()
    commercial = test_commercial()

    ## creation
    commercial.login()
    commercial.create_client()
    gestion.login()
    gestion.create_collab()
    gestion.cre_contrat()
    commercial.login()
    commercial.cre_evenement()

    ## modif
    commercial.update_client()
    commercial.update_contrat()
    gestion.login()
    gestion.up_evenement()
    gestion.update_collab()

    ## delete

    commercial.login()
    commercial.del_evenement()
    gestion.login()
    gestion.del_contrat()
    commercial.login()
    commercial.delete_client()
    gestion.login()
    gestion.delete_collab()