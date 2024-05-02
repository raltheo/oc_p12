from app.middleware import login_require, require_role
from app.models import Contrat, Client
from app.views import menu_contrat_view, create_contrat_view, show_contrat, delete_contrat_view, update_contrat_view, filtre_contrat_view
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
def liste_contrat_filtre(session, option, collaborateur_id=None, user_role=None):
    if option == 1 : contrats = session.query(Contrat).filter_by(status_contrat="unsigned").all()
    if option == 2 : contrats = session.query(Contrat).filter(Contrat.montant_restant != 0).all()
    if option == 3 : contrats = session.query(Contrat).filter_by(commercialId=collaborateur_id).all()
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
def liste_my_contrat(session, collaborateur_id=None, user_role=None):
    contrats = session.query(Contrat).filter_by(commercialId=collaborateur_id).all()
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
            return True, "Contrat crée ! ✔️"
        except:
            session.rollback()
            return False, "Une erreur est survenue. ❌"

    return False, "Client introuvable. ❌"

@login_require
@require_role(["admin", "gestion"])
def delete_contrat(session, contrat_id, collaborateur_id=None, user_role=None):
    contrat = session.query(Contrat).filter_by(contratId=contrat_id).first()
    if contrat:
            session.delete(contrat)
            session.commit()
            return True, "Contrat supprimé. ✔️"
    return False, "Contrat introuvable ❌"

@login_require
@require_role(["admin", "gestion", "commercial"])
def update_contrat(session, contrat_id, col, data, collaborateur_id=None, user_role=None):
    contrat = session.query(Contrat).filter_by(contratId=contrat_id).first()
    if contrat.client.collaborateurId != collaborateur_id and user_role == "commercial":
        return False, "Vous ne pouvez pas mettre a jour les contrat d'autres clients ❌"
    if contrat:
        try:
            if col == 1: contrat.montant_total = data
            elif col == 2: contrat.montant_restant = data
            elif col == 3: contrat.status_contrat = data
            else: return False, "Mauvais choix ❌" 
            session.commit()
            return True, "Contrat mis a jour ! ✔️"
        except Exception as e:
            print(e)
            session.rollback()
            return False, "Une erreur est survenue ! ❌"
    return False, "Contrat introuvable ❌"


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
        if choix == 3:
            id_contrat, col, new_data = update_contrat_view(liste_contrat(session))
            state, message = update_contrat(session, id_contrat, col, new_data)
            if state == True:
                green_print(message)
            else:
                red_print(message)
        if choix == 4:
            contrat_id = delete_contrat_view(liste_contrat(session))
            state, message = delete_contrat(session, contrat_id)
            if state == True:
                green_print(message)
            else:
                red_print(message)
        if choix == 5:
            new_choice = filtre_contrat_view()
            if new_choice == 1: show_contrat(liste_contrat_filtre(session, 1))
            if new_choice == 2: show_contrat(liste_contrat_filtre(session, 2))
            if new_choice == 3: show_contrat(liste_contrat_filtre(session, 3))
        if choix == 6:
            break
    return