# app/views/main_window.py
import tkinter as tk
from tkinter import ttk
from .menu_bar import MenuBar

from app.services.current_user import current_user_session

class MainWindow:
    def __init__(self, master=None, current_user=None):
        self.master = tk.Tk()  # Mudamos de ThemedTk para Tk
        self.current_user = current_user
        self.master.title('Tela Principal')
        self.master.geometry('1280x720')  # você pode ajustar o tamanho conforme sua necessidade
        self.master.resizable(False, False)  # Desativa a opção de redimensionar a janela

        current_user = current_user_session.get_current_user()
        if current_user is not None:
            self.welcome_message = ttk.Label(
                self.master, 
                text=f"Bem-vindo à Tela Principal, {current_user.name}!", 
                font=("Arial", 24)
            )
        else:
            self.welcome_message = ttk.Label(
                self.master, 
                text="Bem-vindo à Tela Principal!", 
                font=("Arial", 24)
            )

        # Centraliza a janela na tela
        window_width = self.master.winfo_reqwidth()
        window_height = self.master.winfo_reqheight()
        position_right = int(self.master.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(self.master.winfo_screenheight() / 2 - window_height / 2)
        self.master.geometry("+{}+{}".format(position_right, position_down))

        # Aqui você pode adicionar widgets à sua janela principal

        # Cria o menu personalizado
        self.custom_menu = MenuBar(self.master)

        # Por exemplo, uma mensagem de boas-vindas:
        self.welcome_message = ttk.Label(self.master, text="Bem-vindo à Tela Principal!", font=("Arial", 24))
        self.welcome_message.pack(pady=20)

    def show(self):
        self.master.deiconify()

    def hide(self):
        self.master.withdraw()

