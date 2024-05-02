from datetime import datetime
from .color import red_print
import re
import getpass

def input_int(phrase):
    while True:
        data = input(phrase)
        try:
            int(data)
            break
        except:
            red_print("Un nombre est attendu ❌")
    return int(data)

def input_password(phrase):
    return getpass.getpass(prompt=phrase)


def input_date(phrase):
    while True:
        data = input(phrase)
        try:
            data = datetime.strptime(data ,'%d/%m/%Y').strftime('%Y-%m-%d')
            break
        except:
            red_print("Une date est attendu (format : jj/mm/aaaa) ❌")
    return data

def input_signed(phrase):
    while True:
        data = input(phrase)
        try:
            if data == "signed" or data == "unsigned":
                break
        except:
            red_print("Vous ne pouvez mettre que les valeurs signed ou unsigned ❌")
    return data

def input_role(phrase):
    while True:
        data = input(phrase)
        try:
            if data == "commercial" or data == "gestion" or data == "support":
                break
        except:
            red_print("Role invalide ! ❌")
    return data

def input_email(phrase):
    reg = r"^[\w.-]+@[\w.-]+\.\w+$"
    while True:
        data = input(phrase)
        try:
            m = re.match(reg, data)
            if m:
                break
            red_print("Merci d'entrer une email valide ! ❌")
        except:
            red_print("Merci d'entrer une email valide ! ❌")
    return data