from prettytable import PrettyTable

def show_client(clients):
    x = PrettyTable()
    x.field_names = ["id", "nom", "email", "téléphone", "Entreprise", "Collaborateur Associé"]
    for client in clients:
        x.add_row(client)
    print("\n")
    print(x)
    print("\n")

def menu_client_view():
    print("\n")
    print("Gestion des Clients")
    print("    1: Afficher les Clients")
    print("    2: Crée un client")
    print("    3: Modifier un client")
    print("    4: Supprimé un client")
    print("    5: Retour")
    choix = input("\nEpicEvent# ")
    return int(choix)