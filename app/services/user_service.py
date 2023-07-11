# app/services/user_service.py

from sqlalchemy.orm import Session
from app.models.user import User, Admin, Professor

class UserService:
    """
    A classe UserService é responsável por realizar operações CRUD para usuários.
    """

    def __init__(self, session: Session):
        """
        O construtor do UserService requer uma sessão SQLAlchemy, 
        que será usada para fazer consultas no banco de dados.
        """
        self.session = session

    def create_user(self, user: User):
        """
        Adiciona e salva um novo usuário no banco de dados.
        """
        self.session.add(user)
        self.session.commit()

    def get_user(self, user_id: int) -> User:
        """
        Obtém um usuário pelo ID.
        """
        return self.session.query(User).filter_by(id=user_id).first()

    def update_user(self, user: User):
        """
        Atualiza um usuário existente e salva as alterações no banco de dados.
        """
        self.session.commit()

    def delete_user(self, user: User):
        """
        Exclui um usuário existente do banco de dados.
        """
        self.session.delete(user)
        self.session.commit()

    def get_user_by_email(self, email: str) -> User:
        """
        Obtém um usuário pelo nome de usuário.
        """
        return self.session.query(User).filter_by(email=email).first()

