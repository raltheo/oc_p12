from app.views import show_client
from prettytable import PrettyTable

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
    print("Gestion des Clients")
    print("    1: Afficher les Contrats")
    print("    2: Crée un contrat")
    print("    3: Modifier un contrat")
    print("    4: Supprimé un contrat")
    print("    5: Retour")
    choix = input("\nEpicEvent# ")
    return int(choix)

def create_contrat_view(clients):
    show_client(clients)
    client_id = input("Choisissez l'ID du client pour le contrat : ")
    montant_total = input("Entrez le montant total : ")
    montant_restant = input("Entrez le montant restant : ")
    status_contrat = input("Entrez le status du contrat (unsigned ou signed) : ")
    return client_id, montant_total, montant_restant, status_contrat