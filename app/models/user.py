# app/models/user.py
from sqlalchemy import Column, Integer, String, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
import datetime
import bcrypt

# Enum para status do usuário
USER_STATUSES = Enum("Active", "Inactive", name="user_statuses")

class User(Base):
    """
    Classe User representa um usuário genérico no sistema.
    """
    def __init__(self, email=None, password=None):
        if email:
            self.email = email
        if password:
            self.password = password 

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    email = Column(String(150))
    password_hash = Column(String(60))  # The password hash field
    status = Column(USER_STATUSES)
    creation_date = Column(DateTime, default=datetime.datetime.utcnow)
    modification_date = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    type = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity':'users',
        'polymorphic_on':type
    }

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute.')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    def check_password(self, password):
        return bcrypt.checkpw(password.encode(), self.password_hash.encode())

    @classmethod
    def factory(cls):
        """
        Factory method for creating a test User instance.
        """
        return cls(name='Test User', email='test@example.com', status='Active')



class Admin(User):
    """
    Classe Admin representa um usuário com permissões de administração no sistema.
    """
    __tablename__ = 'admins'
    id = Column(Integer, ForeignKey('users.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity':'admins',
    }

    @classmethod
    def factory(cls):
        """
        Factory method for creating a test Admin instance.
        """
        return cls(name='Test Admin', email='admin@example.com', status='Active')


class Professor(User):
    """
    Classe Professor representa um professor no sistema.
    """
    __tablename__ = 'professors'
    id = Column(Integer, ForeignKey('users.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity':'professors',
    }

    @classmethod
    def factory(cls):
        """
        Factory method for creating a test Professor instance.
        """
        return cls(name='Test Professor', email='professor@example.com', status='Active')
