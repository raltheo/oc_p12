from app.middleware import login_require, require_role
from app.models import Client, Evenement, Contrat
from app.views import show_evenement, menu_evenement_view, create_evenement_view
from app.controllers.client import liste_my_client
from app.controllers.contrat import liste_my_contrat
from app.utils import red_print, green_print
from datetime import datetime


def format_date(date):
    date_object = datetime.strptime(str(date), "%Y-%m-%d")
    return date_object.strftime("%d/%m/%Y")

@login_require
def liste_evenement(session, collaborateur_id=None, user_role=None):
    evenements = session.query(Evenement).all()
    data = []
    for evenement in evenements:
        data.append([evenement.evenementId,
                     evenement.contratId, 
                     format_date(evenement.date_debut),
                     format_date(evenement.date_fin),
                     evenement.client.user.email,
                     evenement.lieu,
                     evenement.nombre_invites,
                     evenement.support.user.email if evenement.support else "aucun support"
                     ])
    return data

@login_require
@require_role(["admin", "commercial"])
def create_evenement(session, contrat_id, date_debut, date_fin, lieu, support_id, nombre_invite, note, collaborateur_id=None, user_role=None):
    contrat = session.query(Contrat).filter_by(contratId=contrat_id).first()
    if contrat:
        evenement = Evenement(
            contratId=contrat.contratId,
            date_debut=date_debut,
            date_fin=date_fin,
            clientId=contrat.client.clientId,
            supportId=support_id,
            lieu=lieu,
            nombre_invites=nombre_invite,
            note=note 
        )
        try:
            session.add(evenement)
            session.commit()
            return True, "Evenement crée !"
        except:
            session.rollback()
            return False, "Une erreur est survenue."
    return False, "Contrat introuvable."

@login_require
@require_role(["admin", "gestion"])
def delete_evenement(session, contrat_id, collaborateur_id=None, user_role=None):
    contrat = session.query(Evenement).filter_by(contratId=contrat_id).first()
    if contrat:
            session.delete(contrat)
            session.commit()
            return True, "Contrat supprimé."
    return False, "Contrat introuvable"

@login_require
@require_role(["admin", "gestion", "commercial"])
def update_evenement(session, contrat_id, col, data, collaborateur_id=None, user_role=None):
    contrat = session.query(Evenement).filter_by(contratId=contrat_id).first()
    if contrat.client.collaborateurId != collaborateur_id and user_role == "commercial":
        return False, "Vous ne pouvez pas mettre a jour les contrat d'autres clients"
    if contrat:
        try:
            if col == 1: contrat.montant_total = data
            elif col == 2: contrat.montant_restant = data
            elif col == 3: 
                if data in ["unsigned", "signed"]:
                    contrat.status_contrat = data
            else: return False, "Mauvais choix"
            session.commit()
            return True, "Contrat mis a jour !"
        except Exception as e:
            print(e)
            session.rollback()
            return False, "Une erreur est survenue !"
    return False, "Contrat introuvable"


@login_require
def menu_evenement(session, collaborateur_id=None, user_role=None):
    while True:
        choix = menu_evenement_view()
        if choix == 1:
            show_evenement(liste_evenement(session))
        if choix == 2:
            contrat_id, date_debut, date_fin, lieu, support_id, nombre_invite, note = create_evenement_view(liste_my_contrat(session))
            state, message = create_evenement(session, contrat_id, date_debut, date_fin, lieu, support_id, nombre_invite, note)
            if state == True:
                green_print(message)
            else:
                red_print(message)
        # if choix == 3:
        #     id_contrat, col, new_data = update_contrat_view(liste_contrat(session))
        #     state, message = update_contrat(session, id_contrat, col, new_data)
        #     if state == True:
        #         green_print(message)
        #     else:
        #         red_print(message)
        # if choix == 4:
        #     contrat_id = delete_contrat_view(liste_contrat(session))
        #     state, message = delete_contrat(session, contrat_id)
        #     if state == True:
        #         green_print(message)
        #     else:
        #         red_print(message)
        if choix == 5:
            break
    return