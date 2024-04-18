
def login_view():
    email = input("Entrez votre email : ")
    password = input("Entrez votre mot de passe : ")
    return email, password

def register_view():
    nom = input("Entrez le nom de l'utilsateur : ")
    email = input("Entrez l'email de l'utilisateur : ")
    telephone = input("Entrez le numéro de téléphone de l'utilisateur : ")
    type_user = input("L'utilisateur sera ? (client ou collaborateur (role admin nécessaire)) : ")
    if type_user == "client":
        client = {}
        client["nom_entreprise"] = input("Entrez le nom de l'entreprise du client : ")
        return nom, email, telephone, type_user, client
    elif type_user == "collaborateur":
        collaborateur = {}
        collaborateur["role"] = input("Entrez le role du collaborateur (commercial, support ou gestion) : ")
        collaborateur["password"] = input("Entrez le mot de passe temporaire du collaborateur : ")
        return nom, email, telephone, type_user, collaborateur
    else:
        print("Erreur, merci de remplir les champs correctement")
        register_view()