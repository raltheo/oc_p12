from app.models import Client, Collaborateur, User
from app.views import show_client, menu_client_view, create_client_view, update_client_view
from app.utils import red_print, green_print
from app.middleware.auth import login_require

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
def update_client(session, client_id, col_to_update, data, collaborateur_id=None, user_role=None):
    client = session.query(Client).filter_by(clientId=client_id).first()
    # je ne sais pas qui peut faire quoi je verrai plus tard pour les auth
    if client:
        try:
            setattr(client, col_to_update, data)
            session.commit()
            return True, "Client mis a jour !"
        except:
            session.rollback()
            return False, "Une erreur est survenue !"
    return False, "Client introuvable"


@login_require
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
def menu_client(session, collaborateur_id=None, user_role=None):
    choix = menu_client_view()
    if choix == 1:
        show_client(liste_client(session))
        menu_client(session)
    if choix == 2:
        nom, email, telephone, nom_entreprise = create_client_view()
        state, message = create_client(session, nom, email, telephone, nom_entreprise)
        if state == True:
            green_print(message)
            menu_client(session)
        else:
            red_print(message)
            menu_client(session)
    if choix == 3:
        id_client, col, new_data = update_client_view(liste_client(session))
        update_client(session, id_client, col, new_data)
        state, message = menu_client(session)
        if state == True:
            green_print(message)
            menu_client(session)
        else:
            red_print(message)
            menu_client(session)
    if choix == 5:
        return