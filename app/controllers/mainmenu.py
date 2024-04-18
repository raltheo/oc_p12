from app.controllers.auth import login, start_check_auth
from app.models import user
from app.models.base import SessionLocal
from app.utils.jwt import get_jwt, delete_jwt
from app.middleware.auth import login_require
from app.views import menu_view, login_view
from app.utils.color import red_print, green_print

session = SessionLocal()
def start_app():
    username, role = start_check_auth(session)
    if username and role:
        choix = menu_view(username, role)
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