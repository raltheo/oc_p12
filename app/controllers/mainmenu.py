from app.models.base import SessionLocal

from app.views import menu_view, login_view

from app.utils import red_print, green_print, delete_jwt

from app.controllers.auth import login, start_check_auth
from app.controllers.client import menu_client
from app.controllers.collaborateur import menu_collaborateur
from app.controllers.contrat import menu_contrat
from app.controllers.evenement import menu_evenement
from app.controllers.account import menu_account

session = SessionLocal()

def start_app():
    username, role = start_check_auth(session)
    if username and role:
        while True:
            choix = menu_view(username, role)
            if choix == 1:
                menu_client(session)
            if choix == 2:
                menu_collaborateur(session)
            if choix == 3:
                menu_contrat(session)
            if choix == 4:
                menu_evenement(session)
            if choix == 5:
                menu_account(session)
            if choix == 6:
                delete_jwt()
                break
            if choix == 7:
                break
        exit(0)
    else:   
        choix = menu_view()
        if choix == 1:
            email, password = login_view()
            state, message = login(session, email, password)
            if state == True:
                green_print(message)
                start_app()
            else:
                red_print(message)
                start_app()