from prettytable import PrettyTable
from app.utils import input_int

def show_collaborateur(clients):
    x = PrettyTable()
    x.field_names = ["id", "nom", "email", "téléphone", "role"]
    for client in clients:
        x.add_row(client)
    print("\n")
    print(x)
    print("\n")

def create_collaborateur_view():
    nom = input("Entrez le nom de l'utilsateur : ")
    email = input("Entrez l'email de l'utilisateur : ")
    telephone = input("Entrez le numéro de téléphone de l'utilisateur : ")
    role = input("Entrez le role du collaborateur (gestion, commercial, support) : ")
    password = input("Entrez le mot de passe temporaire du collaborateur : ")
    return nom, email, telephone, role, password


def update_collaborateur_view(collaborateurs):
    show_collaborateur(collaborateurs)
    col_to_update = {"1": "nom", "2": "email", "3": "téléphone", "4" : "role", "5": "password"}
    id_collaborateur = input_int("Choisissez l'ID du collaborateur à modifié : ")
    [print(f"    {key}: {value}") for key, value in col_to_update.items()]
    choix = input_int("Choisissez un champ a modifier : ")
    try : 
        col_to_update[choix]
    except:
        print("merci de faire correctement")
    new_data = input("Entrez la valeur : ")
    return id_collaborateur, choix, new_data

def menu_collaborateur_view():
    print("\n")
    print("Gestion des Collaborateurs")
    print("    1: Afficher les Collaborateurs")
    print("    2: Crée un Collaborateur")
    print("    3: Modifier un Collaborateur")
    print("    4: Supprimé un Collaborateur")
    print("    5: Retour")
    choix = input_int("\nEpicEvent# ")
    return choix

def delete_collaborateur_view(collaborateurs):
    show_collaborateur(collaborateurs)
    col_id = input_int("Entrez l'Id du collaborateur a supprimer : ")
    return col_id