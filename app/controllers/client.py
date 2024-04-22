from app.models import Client, Collaborateur, User
from app.views import show_client, menu_client_view, create_client_view, update_client_view, delete_client_view
from app.utils import red_print, green_print
from app.middleware import require_role, login_require

@login_require
def liste_client(session, collaborateur_id=None, user_role=None):
    clients = session.query(Client).all()
    data = []
    for client in clients:
        collaborateur = session.query(Collaborateur).filter_by(collaborateurId=client.collaborateurId).first()
        client.nom_collaborator = collaborateur.user.email
        data.append([client.clientId,
                     client.user.nom, 
                     client.user.email,
                     client.user.telephone,
                     client.nom_entreprise,
                     client.nom_collaborator])
    return data

@login_require
@require_role(["admin", "commercial"])
def update_client(session, client_id, col, data, collaborateur_id=None, user_role=None):
    client = session.query(Client).filter_by(clientId=client_id).first()
    if client.collaborateurId != collaborateur_id and user_role != "admin":
        return False, "Vous devez être le commercial du client pour pouvoir faire cela."
    if col == 2:
        verif_mail = session.query(User).filter_by(email=data).first()
        if verif_mail:
            return False, "Email already used"
    if client:
        try:
            if col == 1: client.user.nom = data
            elif col == 2: client.user.email = data
            elif col == 3: client.user.telephone = data
            elif col == 4: client.nom_entreprise = data
            else: return False, "Mauvais choix"
            session.commit()
            return True, "Client mis a jour !"
        except Exception as e:
            print(e)
            session.rollback()
            return False, "Une erreur est survenue !"
    return False, "Client introuvable"


@login_require
@require_role(["admin", "commercial"])
def create_client(session, nom, email, telephone, nom_entreprise, collaborateur_id=None, user_role=None):
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

    new_client = Client(
        nom_entreprise=nom_entreprise,
        userId=new_user.userId,
        collaborateurId=collaborateur_id
    )
    session.add(new_client)
    session.commit()
    return True, "Client crée avec success !"
    

@login_require
@require_role(["admin", "commercial"])
def delete_client(session, client_id, collaborateur_id=None, user_role=None):
    client = session.query(Client).filter_by(clientId=client_id).first()
    if client:
        if client.collaborateurId == collaborateur_id or user_role == "admin":
            session.delete(client)
            session.commit()
            return True, "Client supprimé."
        return False, "Vous devez être le commercial du client pour le supprimer."
    return False, "Client introuvable"

@login_require
def menu_client(session, collaborateur_id=None, user_role=None):
    while True:
        choix = menu_client_view()
        if choix == 1:
            show_client(liste_client(session))
        if choix == 2:
            nom, email, telephone, nom_entreprise = create_client_view()
            state, message = create_client(session, nom, email, telephone, nom_entreprise)
            if state == True:
                green_print(message)
            else:
                red_print(message)
        if choix == 3:
            id_client, col, new_data = update_client_view(liste_client(session))
            state, message = update_client(session, id_client, col, new_data)
            if state == True:
                green_print(message)
            else:
                red_print(message)
        if choix == 4:
            client_id = delete_client_view(liste_client(session))
            state, message = delete_client(session, client_id)
            if state == True:
                green_print(message)
            else:
                red_print(message)
        if choix == 5:
            break
        else:
            print("please enter good number")
    return