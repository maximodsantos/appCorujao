import tkinter as tk
from tkinter import ttk
import os

from PIL import Image, ImageTk
from app.controllers.login_controller import LoginController

class LoginView:
    """
    Classe LoginView que representa a janela de login.
    """
    def __init__(self, root, main_app):
        """
        Construtor da classe LoginView.
        Define e configura a janela de login.
        """
        self.root = root
        self.configure_window()
        self.create_widgets()  # Agora todos os widgets são criados primeiro
        self.login_controller = LoginController(main_app, self)  # Criando login_controller aqui
        self.set_login_button_command()  # Adiciona a ação ao botão
        self.bind_events()


    def configure_window(self):
        """
        Configura as propriedades básicas da janela.
        """
        self.root.title('Autenticação')

        window_width = 850
        window_height = 450

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.root.resizable(False, False)
        self.root.configure(bg='#FBFBFB')

        current_dir = os.path.dirname(os.path.abspath(__file__))
        ico_path = os.path.join(current_dir, 'resources', 'icons', 'simble.png')
        ico_image = ImageTk.PhotoImage(Image.open(ico_path))
        self.root.tk.call('wm', 'iconphoto', self.root._w, ico_image)
        
        #self.root.iconbitmap(ico_path)

    def create_widgets(self):
        """
        Cria os widgets da janela de login.
        """
        self.left_frame = self.create_left_frame()
        self.right_frame = self.create_right_frame()

        self.login_label, self.email_label, self.password_label, self.email_entry, self.password_entry, self.forgot_password, self.login_button = self.create_right_frame_widgets()

        self.place_widgets()

    def create_left_frame(self):
        """
        Cria o frame esquerdo da janela.
        """
        left_frame = tk.Frame(self.root, width=400, height=450, bd=0)
        left_frame.grid(row=0, column=0)

        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, 'resources', 'images', 'background-login.png')

        self.bg_image = tk.PhotoImage(file=image_path)
        bg_label = tk.Label(left_frame, image=self.bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        return left_frame

    def create_right_frame(self):
        """
        Cria o frame direito da janela.
        """
        right_frame = tk.Frame(self.root, width=400, height=450, bd=0, bg='#FBFBFB')
        right_frame.grid(row=0, column=1)

        return right_frame

    def create_right_frame_widgets(self):
        """
        Cria os widgets do frame direito.
        """
        login_label = tk.Label(self.right_frame, text="Login", bg='#FBFBFB', fg='#4A0751', font=('Arial', 18))
        email_label = tk.Label(self.right_frame, text="Email", bg='#FBFBFB', fg='#4A0751', font=('Arial', 11))
        password_label = tk.Label(self.right_frame, text="Senha", bg='#FBFBFB', fg='#4A0751', font=('Arial', 11))

        email_entry = tk.Entry(self.right_frame, font=('Arial', 16), width=25, bd=0, bg='#D0D1D3', fg='#FBFBFB')
        password_entry = tk.Entry(self.right_frame, show="*", font=('Arial', 16), width=25, bd=0, bg='#D0D1D3', fg='#FBFBFB')

        forgot_password = tk.Label(self.right_frame, text='Esqueci minha senha', font=('Arial', 12), bg='#FBFBFB', fg='#4A0751', cursor='hand2')

        # Configura o botão de login para chamar handle_login quando for clicado
        login_button = tk.Button(self.right_frame, text="Login", bg='#4A0751', fg='#FBFBFB', cursor='hand2')

        return login_label, email_label, password_label, email_entry, password_entry, forgot_password, login_button

    def place_widgets(self):
        """
        Posiciona os widgets no frame direito.
        """
        self.login_label.grid(row=0, column=0, columnspan=2, sticky='news', pady=20)
        self.email_label.grid(row=1, column=0, ipadx=10)
        self.email_entry.grid(row=1, column=1, pady=20)
        self.password_label.grid(row=2, column=0, ipadx=10)
        self.password_entry.grid(row=2, column=1, pady=20)
        self.forgot_password.grid(row=3, column=0, columnspan=2, sticky='e')
        self.login_button.grid(row=4, column=0, columnspan=2, pady=30)

    def bind_events(self):
        """
        Vincula os eventos aos widgets apropriados.
        """
        self.email_entry.bind('<FocusIn>', self.entry_on_focus_in)
        self.email_entry.bind('<FocusOut>', self.entry_on_focus_out)
        self.password_entry.bind('<FocusIn>', self.entry_on_focus_in)
        self.password_entry.bind('<FocusOut>', self.entry_on_focus_out)

        self.login_button.bind("<Enter>", self.on_enter_login_button)
        self.login_button.bind("<Leave>", self.on_leave_login_button)
        self.forgot_password.bind("<Enter>", self.on_enter_forgot_password)
        self.forgot_password.bind("<Leave>", self.on_leave_forgot_password)

    def entry_on_focus_in(self, event):
        event.widget.configure(bg='#4A0751')

    def entry_on_focus_out(self, event):
        event.widget.configure(bg='#D0D1D3')

    def on_enter_login_button(self, event):
        self.login_button.configure(bg='#AD1BD9')  # Changes the color to red when mouse hovers over

    def on_leave_login_button(self, event):
        self.login_button.configure(bg='#4A0751')  # Changes the color back to original when mouse leaves

    def on_enter_forgot_password(self, event):
        self.forgot_password.configure(fg='#AD1BD9')  # Changes the color to red when mouse hovers over

    def on_leave_forgot_password(self, event):
        self.forgot_password.configure(fg='#4A0751')  # Changes the color back to original when mouse leaves

    def set_login_button_command(self):
        """
        Define o command do botão de login para chamar o método handle_login do login_controller.
        """
        self.login_button.config(command=self.login_controller.handle_login)
        
    def show(self):
        self.root.deiconify()

    def hide(self):
        self.root.withdraw()
