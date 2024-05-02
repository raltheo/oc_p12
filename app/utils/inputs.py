from datetime import datetime
from .color import red_print
import re
import getpass
from sentry_sdk import capture_message


def input_int(phrase):
    while True:
        data = input(phrase)
        try:
            int(data)
            break
        except:
            red_print("Un nombre est attendu ❌")
            capture_message('Input failure (int)')
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
            capture_message('Input failure (date)')
    return data

def input_signed(phrase):
    while True:
        data = input(phrase)
        try:
            if data == "signed" or data == "unsigned":
                break
        except:
            red_print("Vous ne pouvez mettre que les valeurs signed ou unsigned ❌")
            capture_message('Input failure (signed or unsigned)')
    return data

def input_role(phrase):
    while True:
        data = input(phrase)
        try:
            if data == "commercial" or data == "gestion" or data == "support":
                break
        except:
            red_print("Role invalide ! ❌")
            capture_message('Input failure (role)')
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
            capture_message('Input failure (email)')
        except:
            red_print("Merci d'entrer une email valide ! ❌")
            capture_message('Input failure (email)')
    return data