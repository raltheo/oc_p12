from app.controllers.auth import login, start_check_auth, register
from app.models.base import SessionLocal
from app.views import menu_view, login_view, register_view
from app.utils import red_print, green_print

session = SessionLocal()

def start_app():
    username, role = start_check_auth(session)
    if username and role:
        choix = menu_view(username, role)
        if choix == 1:
            nom, email, telephone, type_user, collaborclient = register_view()
            if type_user == "client":
                state, message = register(session, nom, email, telephone, type_user, client=collaborclient)
            if type_user == "collaborateur":
                state, message = register(session, nom, email, telephone, type_user, collaborateur=collaborclient)
            if state == True:
                green_print(message)
                start_app()
            else:
                red_print(message)
                start_app()
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