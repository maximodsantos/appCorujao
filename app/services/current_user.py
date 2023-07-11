# app/services/current_user.py

class CurrentUser:
    """
    Classe CurrentUser é responsável por armazenar o usuário atualmente logado.
    """
    def __init__(self):
        self.user = None

    def login(self, user):
        self.user = user

    def logout(self):
        self.user = None

    def get_current_user(self):
        return self.user

current_user_session = CurrentUser()
