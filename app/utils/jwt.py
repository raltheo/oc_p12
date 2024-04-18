import os

def save_jwt(token):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    token_file_path = os.path.join(script_dir, '..', '.token')
    open(token_file_path, "w").write(token)

def get_jwt():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    token_file_path = os.path.join(script_dir, '..', '.token')
    token = open(token_file_path, "r").read()
    return token

def delete_jwt():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    token_file_path = os.path.join(script_dir, '..', '.token')
    token = open(token_file_path, "w").close()