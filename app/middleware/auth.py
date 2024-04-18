from app.settings import SECRET_KEY
import jwt
from app.utils.jwt import delete_jwt, get_jwt


def login_require(func):
    """ Un middleware qui vérifie le JWT avant d'exécuter la fonction donnée. """
    def wrapper(*args, **kwargs):
        try:
            data = jwt.decode(get_jwt(), SECRET_KEY, algorithms=["HS256"])
            return func(*args, collaborateur_id=data["collaborateur_id"], user_role=data["role"], **kwargs)
        except:
            delete_jwt()
            print("Invalid or expired token.")
            return None
    return wrapper