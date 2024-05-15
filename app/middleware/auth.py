from app.settings import SECRET_KEY
import jwt
from app.utils import get_jwt, delete_jwt
from functools import wraps


def login_require(func):
    """ Un middleware qui vérifie le JWT avant d'exécuter la fonction donnée. """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            data = jwt.decode(get_jwt(), SECRET_KEY, algorithms=["HS256"])
            return func(*args, collaborateur_id=data["collaborateur_id"], user_role=data["role"], **kwargs)
        except jwt.ExpiredSignatureError as e:
            delete_jwt()
            print("Token expired. Login required ❌", e)
            exit(1)
        except jwt.InvalidTokenError as e:
            delete_jwt()
            print("Invalid token. Login required ❌", e)
            exit(1)
        except Exception as e:
            return
    return wrapper