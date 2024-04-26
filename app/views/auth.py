from app.utils import input_email

def login_view():
    email = input_email("Entrez votre email : ")
    password = input("Entrez votre mot de passe : ")
    return email, password
