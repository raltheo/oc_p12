from prettytable import PrettyTable
from app.utils import input_int, input_role, input_email, input_password
from app.middleware import require_role, login_require

def show_collaborateur(clients):
    x = PrettyTable()
    x.field_names = ["id", "nom", "email", "téléphone", "role"]
    for client in clients:
        x.add_row(client)
    print("\n")
    print(x)
    print("\n")

@login_require
@require_role(["admin", "gestion"])
def create_collaborateur_view():
    nom = input("Entrez le nom de l'utilsateur : ")
    email = input_email("Entrez l'email de l'utilisateur : ")
    telephone = input("Entrez le numéro de téléphone de l'utilisateur : ")
    role = input_role("Entrez le role du collaborateur (gestion, commercial, support) : ")
    password = input_password("Entrez le mot de passe temporaire du collaborateur : ")
    return nom, email, telephone, role, password

@login_require
@require_role(["admin", "gestion"])
def update_collaborateur_view(collaborateurs, supports):
    show_collaborateur(collaborateurs)
    col_to_update = {"1": "nom", "2": "email", "3": "téléphone", "4" : "role", "5": "password"}
    id_collaborateur = input_int("Choisissez l'ID du collaborateur à modifié : ")
    [print(f"    {key}: {value}") for key, value in col_to_update.items()]
    choix = input_int("Choisissez un champ a modifier : ")
    try : 
        col_to_update[str(choix)]
    except:
        print("merci de faire correctement")
    if choix == 4:
        new_data = input_role("Entrez le role : ")
    elif choix == 2:
        new_data = input_email("Entrez l'email : ")
    else:
        new_data = input("Entrez la valeur : ")
    return id_collaborateur, choix, new_data

def menu_collaborateur_view():
    print("Gestion des Collaborateurs")
    print("    1: Afficher les Collaborateurs")
    print("    2: Crée un Collaborateur")
    print("    3: Modifier un Collaborateur")
    print("    4: Supprimé un Collaborateur")
    print("    5: Retour")
    choix = input_int("\nEpicEvent# ")
    return choix

@login_require
@require_role(["admin", "gestion"])
def delete_collaborateur_view(collaborateurs):
    show_collaborateur(collaborateurs)
    col_id = input_int("Entrez l'Id du collaborateur a supprimer : ")
    return col_id