from prettytable import PrettyTable

def show_client(clients):
    x = PrettyTable()
    x.field_names = ["id", "nom", "email", "téléphone", "Entreprise", "Collaborateur Associé"]
    for client in clients:
        x.add_row(client)
    print("\n")
    print(x)
    print("\n")

def create_client_view():
    nom = input("Entrez le nom de l'utilsateur : ")
    email = input("Entrez l'email de l'utilisateur : ")
    telephone = input("Entrez le numéro de téléphone de l'utilisateur : ")
    nom_entreprise = input("Entrez le nom de l'entreprise du client : ")
    return nom, email, telephone, nom_entreprise


def update_client_view(clients):
    show_client(clients)
    col_to_update = {"1": "nom", "2": "email", "3": "téléphone", "4" : "Entreprise"}
    id_client = input("Choisissez l'ID du client à modifié : ")
    [print(f"    {key}: {value}") for key, value in col_to_update.items()]
    choix = input("Choisissez un champ a modifier : ")
    try : 
        col_to_update[choix]
        col = int(choix)
    except:
        print("merci de faire correctement")
    new_data = input("Entrez la valeur : ")
    return id_client, col, new_data

def menu_client_view():
    print("Gestion des Clients")
    print("    1: Afficher les Clients")
    print("    2: Crée un client")
    print("    3: Modifier un client")
    print("    4: Supprimé un client")
    print("    5: Retour")
    choix = input("\nEpicEvent# ")
    return int(choix)


def delete_client_view(clients):
    show_client(clients)
    client_id = int(input("Entrez l'Id du client a supprimer : "))
    return client_id