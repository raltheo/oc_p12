import jwt
from datetime import timedelta, datetime, timezone
from app.settings import SECRET_KEY
from app.models import User, Collaborateur
import bcrypt
from app.utils import delete_jwt, get_jwt, save_jwt

def create_token(user_id, role):
    payload = {
        "collaborateur_id": user_id,
        "role" : role,
        "exp": datetime.now(timezone.utc) + timedelta(days=1)
    }
    save_jwt(jwt.encode(payload, SECRET_KEY, algorithm="HS256"))
    

def start_check_auth(session):
    try:
        token = get_jwt()
        if token == "":
            return None, None
        data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        collaborateur = session.query(Collaborateur).filter_by(collaborateurId=data["collaborateur_id"]).first()
        return collaborateur.user.nom, data["role"]
    except:
        delete_jwt()
        return None, None

def login(session, email, password):
    user = session.query(User).filter_by(email=email).first()
    if not user:
        return False, "User not found ❌"
    collaborateur = user.collaborateur
    if collaborateur and bcrypt.checkpw(password.encode('utf-8'), collaborateur.password.encode('utf-8')):
        create_token(collaborateur.collaborateurId, collaborateur.role.nom)
        return True, "Login successful ✔️"
    else:
        return False, "Incorrect password ❌"