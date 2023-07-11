# app/controllers/login_controller.py

from app.services.authentication_service import AuthenticationService
from app.models.user import User
from app.views.main_window import MainWindow
import tkinter as tk
from tkinter import messagebox

class LoginController:
    """
    A classe LoginController é responsável por gerenciar as ações de login.
    """

    def __init__(self, main_app, login_window):
        """
        Construtor da classe LoginController.
        """
        self.main_app = main_app
        self.login_window = login_window
        self.authentication_service = AuthenticationService()
        self.login_successful = tk.BooleanVar()  # Variável de controle para saber se o login foi bem-sucedido

        # Conecta os botões de login e esqueci minha senha aos métodos correspondentes
        self.login_window.login_button.config(command=self.handle_login)
        self.login_window.forgot_password.bind("<Button-1>", self.handle_forgot_password)


    def handle_login(self):
        """
        Este método é chamado quando o botão de login é pressionado.
        Ele pega o usuário e a senha da janela de login, e tenta autenticar o usuário.
        """
        email = self.login_window.email_entry.get()
        password = self.login_window.password_entry.get()

        if not email or not password:
            messagebox.showerror("Erro de autenticação", "Usuário e/ou senha não podem ser vazios")
            return

        user = User(email, password)

        if self.authentication_service.login(email, password):
            messagebox.showinfo("Sucesso", "Login efetuado com sucesso!")
            self.login_successful.set(True)  # Seta a variável de controle para True
        else:
            messagebox.showerror("Erro", "Falha no login! Verifique suas credenciais.")


    def handle_forgot_password(self, event):
        """
        Este método é chamado quando o link "Esqueci minha senha" é pressionado.
        """
        # Implementar lógica de recuperação de senha aqui
        pass
