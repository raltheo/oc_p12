from app.models import Client, Collaborateur
from app.views import show_client, menu_client_view
from app.views.auth import register_view
from app.controllers.auth import register
from app.utils.color import red_print, green_print
from app.middleware.auth import login_require

def liste_client(session):
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

def update_client(session, client_id, col_to_update, data):
    client = session.query(Client).filter_by(clientId=client_id).first()
    if client:
        try:
            setattr(client, col_to_update, data)
            client.commit()
            return True, "Client mis a jour !"
        except:
            return False, "Une erreur est survenue !"
    return False, "Client introuvable"

@login_require
def menu_client(session, collaborateur_id=None, user_role=None):
    choix = menu_client_view()
    if choix == 1:
        show_client(liste_client(session))
    if choix == 2:
        nom, email, telephone, type_user, collaborclient = register_view()
        if type_user == "client":
            state, message = register(session, nom, email, telephone, type_user, client=collaborclient)
        if type_user == "collaborateur":
            state, message = register(session, nom, email, telephone, type_user, collaborateur=collaborclient)
        if state == True:
            green_print(message)
            menu_client(session)
        else:
            red_print(message)
            menu_client(session)