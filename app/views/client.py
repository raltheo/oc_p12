from prettytable import PrettyTable
from app.utils import input_int, input_email
from app.middleware import require_role, login_require

def show_client(clients):
    x = PrettyTable()
    x.field_names = ["id", "nom", "email", "téléphone", "Entreprise", "Collaborateur Associé"]
    for client in clients:
        x.add_row(client)
    print("\n")
    print(x)
    print("\n")


@login_require
@require_role(["admin", "commercial"])
def create_client_view(collaborateur_id=None, user_role=None):
    nom = input("Entrez le nom de l'utilsateur : ")
    email = input_email("Entrez l'email de l'utilisateur : ")
    telephone = input("Entrez le numéro de téléphone de l'utilisateur : ")
    nom_entreprise = input("Entrez le nom de l'entreprise du client : ")
    return nom, email, telephone, nom_entreprise

@login_require
@require_role(["admin", "commercial"])
def update_client_view(clients, collaborateur_id=None, user_role=None):
    show_client(clients)
    col_to_update = {"1": "nom", "2": "email", "3": "téléphone", "4" : "Entreprise"}
    id_client = input_int("Choisissez l'ID du client à modifié : ")
    [print(f"    {key}: {value}") for key, value in col_to_update.items()]
    choix = input_int("Choisissez un champ a modifier : ")
    try : 
        col_to_update[str(choix)]
    except:
        print("merci de faire correctement")
    if choix == 2:
        new_data = input_email("Entrez la valeur : ")
    else:
        new_data = input("Entrez la valeur : ")
    return id_client, choix, new_data

def menu_client_view():
    print("Gestion des Clients")
    print("    1: Afficher les Clients")
    print("    2: Crée un client")
    print("    3: Modifier un client")
    print("    4: Supprimé un client")
    print("    5: Retour")
    choix = input_int("\nEpicEvent# ")
    return choix

@login_require
@require_role(["admin", "commercial"])
def delete_client_view(clients, collaborateur_id=None, user_role=None):
    show_client(clients)
    client_id = input_int("Entrez l'Id du client a supprimer : ")
    return client_id