from re import S
from app.models import Collaborateur, User, Role
from app.views import show_collaborateur, update_collaborateur_view, menu_collaborateur_view, create_collaborateur_view,delete_collaborateur_view
from app.utils import red_print, green_print, hash_password
from app.middleware import require_role, login_require

@login_require
def liste_collaborateur(session, collaborateur_id=None, user_role=None):
    collaborateurs = session.query(Collaborateur).all()

    data = []
    for collaborateur in collaborateurs:
        data.append([collaborateur.collaborateurId,
                     collaborateur.user.nom, 
                     collaborateur.user.email,
                     collaborateur.user.telephone,
                     collaborateur.role.nom
                     ])
    return data

@login_require
def get_support(session, collaborateur_id=None, user_role=None):
    collaborateurs = session.query(Collaborateur).filter_by(role_id=3).all()
    data = []
    for collaborateur in collaborateurs:
        data.append([collaborateur.collaborateurId,
                     collaborateur.user.nom, 
                     collaborateur.user.email,
                     collaborateur.user.telephone,
                     collaborateur.role.nom
                     ])
    return data

@login_require
@require_role(["admin", "gestion"])
def update_collaborateur(session, collaborator_id, col, data, collaborateur_id=None, user_role=None):
    collaborateur = session.query(Collaborateur).filter_by(collaborateurId=collaborator_id).first()
    if col == 2:
        verif_mail = session.query(User).filter_by(email=data).first()
        if verif_mail:
            return False, "Email already used ❌"
    if collaborateur:
        try:
            if col == 1: collaborateur.user.nom = data
            elif col == 2: collaborateur.user.email = data
            elif col == 3: collaborateur.user.telephone = data
            elif col == 4 : collaborateur.role = data
            elif col == 5: collaborateur.password = data
            else: return False, "Mauvais choix ❌"
            session.commit()
            return True, "Collaborateur mis a jour ! ✔️"
        except:
            session.rollback()
            return False, "Une erreur est survenue ! ❌"
    return False, "Collaborateur introuvable ❌"

@login_require
@require_role(["admin", "gestion"])
def create_collaborateur(session, nom, email, telephone, role, password, collaborateur_id=None, user_role=None):
    verif_mail = session.query(User).filter_by(email=email).first()
    if verif_mail:
        return False, "Email already used ❌"
    new_user = User(
                nom=nom,
                email=email,
                telephone=telephone
            )
    session.add(new_user)
    session.flush() 
    role = session.query(Role).filter_by(nom=role).first()
    if not role:
        return False, "Invalid role ❌"
    
    new_collaborateur = Collaborateur(
        userId=new_user.userId,
        role_id=role.roleId,
        password=hash_password(password).decode()
    )
    session.add(new_collaborateur)
    session.commit()
    return True, "Collaborateur crée avec success ! ✔️"

@login_require
@require_role(["admin", "gestion"])
def delete_collaborateur(session, col_id, collaborateur_id=None, user_role=None):
    collaborateur = session.query(Collaborateur).filter_by(collaborateurId=col_id).first()
    if collaborateur:
        user = session.query(User).filter_by(userId=collaborateur.user.userId).first()
        session.delete(collaborateur)
        session.delete(user)
        session.commit()
        return True, "Collaborateur supprimé. ✔️"
    return False, "Collaborateur introuvable ❌"

@login_require
def menu_collaborateur(session, collaborateur_id=None, user_role=None):
    while True:
        choix = menu_collaborateur_view()
        if choix == 1:
            show_collaborateur(liste_collaborateur(session))
        if choix == 2:
            nom, email, telephone, role, password = create_collaborateur_view()
            state, message = create_collaborateur(session, nom, email, telephone, role, password)
            if state == True:
                green_print(message)
            else:
                red_print(message)
        if choix == 3:
            id_collaborateur, col, new_data = update_collaborateur_view(liste_collaborateur(session))
            state, message = update_collaborateur(session, id_collaborateur, col, new_data)
            if state == True:
                green_print(message)
            else:
                red_print(message)
        if choix == 4:
            col_id = delete_collaborateur_view(liste_collaborateur(session))
            state, message = delete_collaborateur(session, col_id)
            if state == True:
                green_print(message)
            else:
                red_print(message)
        if choix == 5:
            break
    return