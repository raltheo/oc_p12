from app.controllers.auth import login, start_check_auth
from app.models.base import SessionLocal
from app.views import menu_view, login_view
from app.utils import red_print, green_print
from app.controllers.client import menu_client



session = SessionLocal()

def start_app():
    username, role = start_check_auth(session)
    if username and role:
        choix = menu_view(username, role)
        if choix == 1:
            menu_client(session)
            start_app()
        if choix == 2:
            print("menu collaborateur")
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