
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
            print("     1: Gerer les Clients")
            print("     2: Gerer les Collaborateurs")
            print("     3: Gerer les Contrats")
            print("     4: Gerer les Evenements")
            print("     5: logout")
            print("     6: Quitter sans se déconnecter")
            choix = input("\nEpicEvent# ")
            return int(choix)
      else:
            print("\nConnectez vous pour avoir accès à l'application")
            print("     1: Se connecter")
            choix = input("\nEpicEvent# ")
            return int(choix)