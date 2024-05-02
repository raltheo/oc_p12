from functools import wraps
from app.utils import red_print 

def require_role(roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user_role = kwargs.get('user_role')
            if user_role in roles:
                return func(*args, **kwargs)
            else:
                red_print(f"Accès refusé : Vous n'avez pas le rôle requis. (role requis : {', '.join([x for x in roles])}) ❌")
                return
        return wrapper
    return decorator