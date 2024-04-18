import jwt
from datetime import timedelta, datetime, timezone
from app.settings import SECRET_KEY
from app.models import User, Role, Collaborateur, Client
import bcrypt
from app.utils.jwt import delete_jwt, get_jwt
from app.utils.jwt import save_jwt
from app.utils.hash_pass import hash_password
from app.middleware.auth import login_require


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
        collaborateur = session.query(Collaborateur).filter_by(userId=data["collaborateur_id"]).first()
        return collaborateur.user.nom, data["role"]
    except:
        delete_jwt()
        return None, None

def login(session, email, password):
    user = session.query(User).filter_by(email=email).first()
    if not user:
        return False, "User not found"
    collaborateur = user.collaborateur
    if collaborateur and bcrypt.checkpw(password.encode('utf-8'), collaborateur.password.encode('utf-8')):
        create_token(collaborateur.collaborateurId, collaborateur.role.nom)
        return True, "Login successful"
    else:
        return False, "Incorrect password"

@login_require
def register(session, nom, email, telephone, type_user, client={}, collaborateur={}, collaborateur_id=None, user_role=None):
    verif_mail = session.query(User).filter_by(email=email).first()
    if verif_mail:
        return False, "Email already used"
    new_user = User(
                nom=nom,
                email=email,
                telephone=telephone
            )
    session.add(new_user)
    session.flush() 
    if type_user == "client":
        new_client = Client(
            nom_entreprise=client["nom_entreprise"],
            userId=new_user.userId,
            collaborateurId=collaborateur_id
        )
        session.add(new_client)
        session.commit()
        return True, "Client crée avec success !"
    if type_user == "collaborateur":
        if user_role == "admin":
            role = session.query(Role).filter_by(nom=collaborateur["role"]).first()
            if not role:
                return False, "Invalid role"
            
            new_collaborateur = Collaborateur(
                userId=new_user.userId,
                role_id=role.roleId,
                password=hash_password(collaborateur["password"]).decode()
            )
            session.add(new_collaborateur)
            session.commit()
            return True, "Collaborateur crée avec success !"
        else:
            return False, "Vous n'êtes pas autorisé a faire ceci"