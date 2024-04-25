from app.views import show_client, show_contrat
from prettytable import PrettyTable
from app.utils import input_date, input_int

def show_evenement(evenements):
    x = PrettyTable()
    x.field_names = ["id", 
                     "contrat Id", 
                     "date début", 
                     "date fin", 
                     "Client email", 
                     "lieu",
                     "Nombre d'invité",
                     "support email"]
    for evenement in evenements:
        x.add_row(evenement)
    print("\n")
    print(x)
    print("\n")

def menu_evenement_view():
    print("Gestion des Evenement")
    print("    1: Afficher les Evenement")
    print("    2: Crée un Evenement")
    print("    3: Modifier un Evenement")
    print("    4: Supprimé un Evenement")
    print("    5: Retour")
    choix = input_int("\nEpicEvent# ")
    return choix

def create_evenement_view(contrats):
    show_contrat(contrats)
    contrat_id = input_int("Choisissez l'ID du contrat a rattacher a l'évenement : ")
    date_debut = input_date("Entrez la date de debut (format jj/mm/aaaa) : ")
    date_fin = input_date("Entrez la date de fin (format jj/mm/aaaa) : ")
    lieu = input("Entrez le lieu de l'evenement : ")
    y_or_n = input("Associer un support ? (y or n) : ")
    if y_or_n == "y":
        support_id = input_int("Entrez l' Id du support pour cette evenement : ") 
    else:
        support_id = None
    nombre_invite = input_int("Entrez le nombre d'invité : ") 
    note = input("Ajouter une note/remarque : ")

    return contrat_id, date_debut, date_fin, lieu, support_id, nombre_invite, note

def delete_evenement_view(evenements):
    show_evenement(evenements)
    evenement_id = input_int("Entrez l'Id du contrat a supprimer : ")
    return evenement_id

def update_evenement_view(evenements):
    show_evenement(evenements)
    col_to_update = {"1": "date début", "2": "date fin", "3": "changer / ajouter support", "4": "lieu", "5":"nombre d'invité", "6" :"note"}
    id_contrat = input_int("Choisissez l'ID de l'evenement à modifié : ")
    [print(f"    {key}: {value}") for key, value in col_to_update.items()]
    choix = input_int("Choisissez un champ a modifier : ")
    try : 
        col_to_update[str(choix)]
    except:
        print("merci de faire correctement")
    if choix == 1 or choix == 2 :
        new_data = input_date("Entrez la nouvelle valeur : ") 
    elif choix == 3:
        new_data = input_int("Entrez la nouvelle valeur (L'Id du nouveau support) : ")
    elif choix == 5:
        new_data = input_int("Entrez la nouvelle valeur : ")
    else:
        new_data = input("Entrez la nouvelle valeur : ")
    return id_contrat, choix, new_data