import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app.controllers.collaborateur import create_collaborateur, delete_collaborateur, liste_collaborateur, update_collaborateur, delete_collaborateur
from app.controllers.client import create_client, update_client, delete_client, liste_client
from app.controllers.auth import login
from app.models.base import SessionLocal

from app.utils import delete_jwt
from app.views import collaborateur

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
                id_collab = x [0]
        res, mess = update_collaborateur(session, id_collab, 1, "updated_name")
        assert "✔️" in mess

    def delete_collab(self):
        data = liste_collaborateur(session)
        for x in data:
            if x[2] == "gestion_test@gestion.com":
                id_collab = x [0]
        res, mess = delete_collaborateur(session, id_collab)
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
                id_collab = x [0]
        res, mess = update_client(session, id_collab, 1, "updated_name")
        assert "✔️" in mess

    def delete_client(self):
        data = liste_client(session)
        for x in data:
            if x[2] == "test_commercial@ac.com":
                id_collab = x [0]
        res, mess = delete_client(session, id_collab)
        assert "✔️" in mess



def test():
    gestion = test_gestion()
    gestion.login()
    gestion.create_collab()
    gestion.update_collab()
    gestion.delete_collab()

    commercial = test_commercial()
    commercial.login()
    commercial.create_client()
    commercial.update_client()
    commercial.delete_client()