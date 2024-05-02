from app.models import Collaborateur, User
from app.utils import red_print, green_print, hash_password
from app.middleware import require_role, login_require
from app.views import menu_account_view, show_account, update_account_view
import bcrypt


@login_require
def account_info(session, collaborateur_id=None, user_role=None):
    compte = session.query(Collaborateur).filter_by(collaborateurId=collaborateur_id).first()
    data = [compte.user.userId, 
            compte.collaborateurId, 
            compte.user.nom, 
            compte.user.email, 
            compte.user.telephone, 
            compte.role.nom]
    return data


@login_require
@require_role(["admin", "commercial"])
def update_account(session, col, data, collaborateur_id=None, user_role=None):
    compte = session.query(Collaborateur).filter_by(collaborateurId=collaborateur_id).first()
    if col == 2:
        verif_mail = session.query(User).filter_by(email=data).first()
        if verif_mail:
            return False, "Email already used ❌"
    if compte:
        try:
            if col == 1: compte.user.nom = data
            elif col == 2: compte.user.email = data
            elif col == 3: compte.user.telephone = data
            elif col == 4: 
                if not bcrypt.checkpw(data[0].encode('utf-8'), compte.password.encode('utf-8')):
                    return False, "Mot de passe incorect ! ❌"
                if data[1] != data[2]:
                    return False, "Merci d'entrez deux fois le même mot de passe pour votre nouveau mot de passe. ❌"
                compte.password = hash_password(data[1]).decode()
    
            else: return False, "Mauvais choix ❌"
            session.commit()
            return True, "Compte mis a jour ! ✔️"
        except Exception as e:
            print(e)
            session.rollback()
            return False, "Une erreur est survenue ! ❌"
    return False, "User introuvable ❌"



@login_require
def menu_account(session, collaborateur_id=None, user_role=None):
    while True:
        choix = menu_account_view()
        if choix == 1:
            show_account(account_info(session))
        if choix == 2:
            col, data = update_account_view()
            state, message = update_account(session, col, data)
            if state == True:
                green_print(message)
            else:
                red_print(message)
        if choix == 3:
            break
    return