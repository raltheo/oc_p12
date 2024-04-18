from app.settings import SECRET_KEY
import jwt
from app.utils import get_jwt, delete_jwt


def login_require(func):
    """ Un middleware qui vérifie le JWT avant d'exécuter la fonction donnée. """
    # au final c'est bien mais si ca crash dans la fonction je perd le token car je le delete, faut faire
    # vraiment attention aux erreurs
    def wrapper(*args, **kwargs):
        try:
            data = jwt.decode(get_jwt(), SECRET_KEY, algorithms=["HS256"])
            return func(*args, collaborateur_id=data["collaborateur_id"], user_role=data["role"], **kwargs)
        except Exception as e:
            # delete_jwt()
            print("Invalid or expired token. Login required ", e)
            exit(1)
    return wrapper