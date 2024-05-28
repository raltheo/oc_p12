from app.middleware import login_require, require_role
from app.models import Evenement, Contrat, Collaborateur
from app.views import show_evenement, menu_evenement_view, filtre_evenement_view, create_evenement_view, update_evenement_view, delete_evenement_view
from app.controllers.contrat import liste_my_contrat
from app.controllers.collaborateur import get_support
from app.utils import red_print, green_print
from datetime import datetime


def format_date(date):
    date_object = datetime.strptime(str(date), "%Y-%m-%d")
    return date_object.strftime("%d/%m/%Y")


@login_require
def liste_evenement_filtre(session, option, collaborateur_id=None, user_role=None):
    if option == 1 : evenements = session.query(Evenement).filter_by(supportId=None).all()
    if option == 2 : evenements = session.query(Evenement).filter_by(supportId=collaborateur_id).all()
    data = []
    for evenement in evenements:
        data.append([evenement.evenementId,
                     evenement.contratId, 
                     format_date(evenement.date_debut),
                     format_date(evenement.date_fin),
                     evenement.client.user.email,
                     evenement.lieu,
                     evenement.nombre_invites,
                     evenement.support.user.email if evenement.support else "aucun support",
                     evenement.note if evenement.note else "aucune note"
                     ])
    return data


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
                     evenement.support.user.email if evenement.support else "aucun support",
                     evenement.note if evenement.note else "aucune note"
                     ])
    return data

@login_require
@require_role(["admin", "commercial"])
def create_evenement(session, contrat_id, date_debut, date_fin, lieu, support_id, nombre_invite, note, collaborateur_id=None, user_role=None):
    contrat = session.query(Contrat).filter_by(contratId=contrat_id).first()
    if support_id != None:
        support = session.query(Collaborateur).filter_by(collaborateurId=support_id).first()
        if not support or support.role.nom != "support":
            return False, "Merci de mettre l'Id d'un support ❌"
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
            return True, "Evenement crée ! ✔️"
        except:
            session.rollback()
            return False, "Une erreur est survenue. ❌"
    return False, "Contrat introuvable. ❌"

@login_require
@require_role(["admin", "commercial"])
def delete_evenement(session, evenement_id, collaborateur_id=None, user_role=None):
    evenement = session.query(Evenement).filter_by(evenementId=evenement_id).first()
    if evenement:
            session.delete(evenement)
            session.commit()
            return True, "Evenement supprimé. ✔️"
    return False, "Evenement introuvable ❌"

@login_require
@require_role(["admin", "gestion", "support"])
def update_evenement(session, evenement_id, col, data, collaborateur_id=None, user_role=None):
    evenement = session.query(Evenement).filter_by(evenementId=evenement_id).first()
    if evenement.supportId != collaborateur_id and user_role != "admin" and user_role != "gestion":
        return False, "Vous ne pouvez pas mettre a jour les evenements ou vous n'êtes pas associer ❌"
    if col != 3 and user_role == "gestion":
        return False, "Vous pouvez mettre à jour uniquement les support en charge de cet evenement ❌"
    if col == 3:
        support = session.query(Collaborateur).filter_by(collaborateurId=data).first()
        if not support or support.role.nom != "support":
            return False, "Merci de mettre l'Id d'un support ❌"
    if evenement:
        try:
            if col == 1: evenement.date_debut = data
            elif col == 2: evenement.date_fin = data
            elif col == 3: evenement.supportId = data
            elif col == 4: evenement.lieu = data
            elif col == 5: evenement.nombre_invites = data
            elif col == 6: evenement.note = data
            else: return False, "Mauvais choix ❌"
            session.commit()
            return True, "Evenement mis a jour ! ✔️"
        except Exception as e:
            print(e)
            session.rollback()
            return False, "Une erreur est survenue ! ❌"
    return False, "Evenement introuvable ❌"


@login_require
def menu_evenement(session, collaborateur_id=None, user_role=None):
    while True:
        choix = menu_evenement_view()
        if choix == 1:
            show_evenement(liste_evenement(session))
        if choix == 2:
            contrat_id, date_debut, date_fin, lieu, support_id, nombre_invite, note = create_evenement_view(liste_my_contrat(session), get_support(session))
            state, message = create_evenement(session, contrat_id, date_debut, date_fin, lieu, support_id, nombre_invite, note)
            if state == True:
                green_print(message)
            else:
                red_print(message)
        if choix == 3:
            id_evenement, col, new_data = update_evenement_view(liste_evenement(session), get_support(session))
            state, message = update_evenement(session, id_evenement, col, new_data)
            if state == True:
                green_print(message)
            else:
                red_print(message)
        if choix == 4:
            contrat_id = delete_evenement_view(liste_evenement(session))
            state, message = delete_evenement(session, contrat_id)
            if state == True:
                green_print(message)
            else:
                red_print(message)
        if choix == 5:
            new_choice = filtre_evenement_view()
            if new_choice == 1: show_evenement(liste_evenement_filtre(session, 1))
            if new_choice == 2: show_evenement(liste_evenement_filtre(session, 2))
        if choix == 6:
            break
    return