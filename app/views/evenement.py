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

def delete_contrat_view(contrats):
    show_contrat(contrats)
    contrat_id = int(input("Entrez l'Id du contrat a supprimer : "))
    return contrat_id

def update_contrat_view(contrats):
    show_contrat(contrats)
    col_to_update = {"1": "montant total", "2": "montant restant", "3": "status du contrat"}
    id_contrat = input("Choisissez l'ID du contrat à modifié : ")
    [print(f"    {key}: {value}") for key, value in col_to_update.items()]
    choix = input("Choisissez un champ a modifier : ")
    try : 
        col_to_update[choix]
        col = int(choix)
    except:
        print("merci de faire correctement")
    while True:
        new_data = input("Entrez la valeur (signed ou unsigned): ")
        if new_data == "signed" or new_data == "unsigned":
            break
    return id_contrat, col, new_data