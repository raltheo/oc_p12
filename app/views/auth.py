from app.utils import input_email, input_password

def login_view():
    email = input_email("Entrez votre email : ")
    password = input_password("Entrez votre mot de passe : ")
    return email, password
