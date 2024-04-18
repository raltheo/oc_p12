
def menu_view(user=None, role=None):
      banner = r""" _____       _      _____                 _       
| ____|_ __ (_) ___| ____|_   _____ _ __ | |_ ___ 
|  _| | '_ \| |/ __|  _| \ \ / / _ \ '_ \| __/ __|
| |___| |_) | | (__| |___ \ V /  __/ | | | |_\__ \
|_____| .__/|_|\___|_____| \_/ \___|_| |_|\__|___/
      |_|                                         """
      print(banner)
      if user and role:
            print(f"\nBonjour {user} (role : {role})")
            print("     1: Crée un Client ou un Collaborateur (role admin nécessaire pour crée un collaborateur) ")
            print("     2: Crée un Contrat")
            print("     3: crée un Evenement")
            print("     5: logout")
            choix = input("\nEpicEvent# ")
            return int(choix)
      else:
            print("\nConnectez vous pour avoir accès à l'application")
            print("     1: Se connecter")
            choix = input("\nEpicEvent# ")
            return int(choix)