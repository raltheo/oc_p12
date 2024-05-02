
from app.views import show_client
from prettytable import PrettyTable
from app.utils import input_signed, input_int
from app.middleware import require_role, login_require

def show_contrat(contrats):
    x = PrettyTable()
    x.field_names = ["id", 
                     "client", 
                     "collaborateur", 
                     "montant total", 
                     "montant restant", 
                     "status contrat",
                     "Date de creation"]
    for contrat in contrats:
        x.add_row(contrat)
    print("\n")
    print(x)
    print("\n")

def menu_contrat_view():
    print("Gestion des Contrats")
    print("    1: Afficher les Contrats")
    print("    2: Crée un contrat")
    print("    3: Modifier un contrat")
    print("    4: Supprimé un contrat")
    print("    5: Afficher les filtres d'affichage")
    print("    6: Retour")
    choix = input_int("\nEpicEvent# ")
    return choix

def filtre_contrat_view():
    print("    1: Afficher les contrats pas encore signé")
    print("    2: Afficher les contrats pas encore payé totalement")
    print("    3: Afficher mes contrats")
    choix = input_int("\nEpicEvent# ")
    return choix

@login_require
@require_role(["admin", "gestion"])
def create_contrat_view(clients, collaborateur_id=None, user_role=None):
    show_client(clients)
    client_id = input_int("Choisissez l'ID du client pour le contrat : ")
    montant_total = input_int("Entrez le montant total : ")
    montant_restant = input_int("Entrez le montant restant : ")
    status_contrat = input_signed("Entrez le status du contrat (unsigned ou signed) : ")
    return client_id, montant_total, montant_restant, status_contrat

@login_require
@require_role(["admin", "gestion"])
def delete_contrat_view(contrats, collaborateur_id=None, user_role=None):
    show_contrat(contrats)
    contrat_id = input_int("Entrez l'Id du contrat a supprimer : ")
    return contrat_id

@login_require
@require_role(["admin", "gestion", "commercial"])
def update_contrat_view(contrats, collaborateur_id=None, user_role=None):
    show_contrat(contrats)
    col_to_update = {"1": "montant total", "2": "montant restant", "3": "status du contrat"}
    id_contrat = input_int("Choisissez l'ID du contrat à modifié : ")
    [print(f"    {key}: {value}") for key, value in col_to_update.items()]
    choix = input_int("Choisissez un champ a modifier : ")
    try : 
        col_to_update[str(choix)]
    except:
        print("merci de faire correctement")
    if choix == 3:
        new_data = input_signed("Entrez la valeur (signed ou unsigned): ")
    else:
        new_data = input_int("Entrez la valeur : ")

    return id_contrat, choix, new_data