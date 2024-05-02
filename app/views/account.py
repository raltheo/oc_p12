from prettytable import PrettyTable
from app.utils import input_int, input_email, input_password


def show_account(account):
    x = PrettyTable()
    x.field_names = ["user Id", "collaborateur Id", "nom", "email", "téléphone", "role"]
    x.add_row(account)
    print("\n")
    print(x)
    print("\n")


def update_account_view():
    col_to_update = {"1": "nom", "2": "email", "3": "téléphone", "4" : "mot de passe"}
    [print(f"    {key}: {value}") for key, value in col_to_update.items()]
    choix = input_int("Choisissez un champ a modifier : ")
    try : 
        col_to_update[str(choix)]
    except:
        print("merci de faire correctement")
    if choix == 2:
        new_data = input_email("Entrez la valeur : ")
    elif choix == 4:
        old_pass = input_password("Entrez votre ancien mot de passe : ")
        new_pass1 = input_password("Entrez votre nouveau mot de passe : ")
        new_pass2 = input_password("Entrez encore votre nouveau mot de passe : ")
        new_data = [old_pass, new_pass1, new_pass2]
    else:
        new_data = input("Entrez la valeur : ")
    return choix, new_data

def menu_account_view():
    print("Gerer mon Compte")
    print("    1: Afficher mes informations")
    print("    2: Modifier mon compte")
    print("    3: Retour")
    choix = input_int("\nEpicEvent# ")
    return choix
