# main.py
import tkinter as tk
import time
from app.views import splash_screen, login_view, main_window
from app.services.current_user import current_user_session

class MainApplication:
    def __init__(self, master): 
        self.master = master
        self.main_window = None
        self.login_view = None

    def run(self):
        # Chama a tela de Splash
        splash = splash_screen.SplashScreen(self.master)
        splash.show()

        # Aqui, faz-se uma pausa para simular o carregamento de algum recurso
        time.sleep(2)

        # Após o recurso ser carregado, a tela de Splash é ocultada
        splash.hide()

        # Finalmente, a tela de Login é exibida
        self.login_view = login_view.LoginView(self.master, self)
        self.login_view.show()

        self.login_view.login_button.config(command=self.handle_login)
        # Escuta a variável de controle e chama handle_login quando ela for setada para True
        self.login_view.login_controller.login_successful.trace("w", self.handle_login)


    def handle_login(self):
        """
        Este método é chamado quando o botão de login é pressionado.
        Ele pega o usuário e a senha da janela de login, e tenta autenticar o usuário.
        """
        if self.login_view.login_controller.login_successful:
            self.login_view.hide()  # Fecha a janela de login

            # Get the current user after successful login
            current_user = current_user_session.get_current_user()
            # Open the MainWindow
            self.open_main_window(current_user)

    def open_main_window(self, current_user):
        self.main_window = main_window.MainWindow(self.master, current_user)
        self.main_window.show()

# O código abaixo inicializa a aplicação
root = tk.Tk()
app = MainApplication(root)
app.run()
root.mainloop()

