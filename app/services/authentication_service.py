# app/services/authentication_service.py

from app.services.user_service import UserService
from app.models.user import User
from app.database import Session

from app.services.current_user import current_user_session

class AuthenticationService:
    """
    Classe AuthenticationService é responsável por autenticar um usuário.
    """
    def __init__(self):
        self.user_service = UserService(Session())

    def login(self, email: str, password: str):
        """
        Este método tenta autenticar o usuário com o nome de usuário e senha fornecidos.
        Retorna True se a autenticação for bem-sucedida, caso contrário, retorna False.
        """
        db_user = self.user_service.get_user_by_email(email)

        if db_user and db_user.check_password(password):
            self.current_user = db_user  # seta o usuário atual
            current_user_session.login(db_user) 
            return True
        else:
            return False

    def get_current_user(self):
        """
        Retorna o usuário atual.
        """
        return self.current_user
