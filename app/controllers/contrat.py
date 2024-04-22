from pydoc import cli
from app.middleware import login_require, require_role
from app.models import Contrat, Client
from app.views import menu_contrat_view, create_contrat_view, show_contrat
from app.controllers.client import liste_client
from app.utils import red_print, green_print


@login_require
def liste_contrat(session, collaborateur_id=None, user_role=None):
    contrats = session.query(Contrat).all()
    data = []
    for contrat in contrats:
        data.append([contrat.contratId,
                     contrat.client.user.email, 
                     contrat.commercial.user.email,
                     contrat.montant_total,
                     contrat.montant_restant,
                     contrat.status_contrat,
                     contrat.created_at
                     ])
    return data

@login_require
@require_role(["admin", "gestion"])
def create_contrat(session, client_id, montant_total, montant_restant, status_contrat, collaborateur_id=None, user_role=None):
    client = session.query(Client).filter_by(clientId=client_id).first()
    if client:
        
        
        contrat = Contrat(
            clientId=client.clientId,
            commercialId=client.collaborateurId,
            montant_total=montant_total,
            montant_restant=montant_restant,
            status_contrat=status_contrat
        )
        try:
            session.add(contrat)
            session.commit()
            return True, "Contrat crée !"
        except:
            session.rollback()
            return False, "Une erreur est survenue."


    return False, "Client introuvable."

@login_require
def menu_contrat(session, collaborateur_id=None, user_role=None):
    while True:
        choix = menu_contrat_view()
        if choix == 1:
            show_contrat(liste_contrat(session))
        if choix == 2:
            client_id, montant_total, montant_restant, status_contrat = create_contrat_view(liste_client(session))
            state, message = create_contrat(session, client_id, montant_total, montant_restant, status_contrat)
            if state == True:
                green_print(message)
            else:
                red_print(message)
        if choix == 5:
            break
    return