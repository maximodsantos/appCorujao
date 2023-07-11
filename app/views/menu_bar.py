# app/views/menu_bar.py
import tkinter as tk
from tkinter import ttk

class MenuBar(ttk.Frame):
    def __init__(self, master=None, callback=None, **kw):
        super().__init__(master, **kw)
        self.pack(side=tk.LEFT, fill=tk.Y)

        self.callback = callback

        self.current_submenu = None

        self.submenu_frame = tk.Frame(master)
        self.submenu_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.admin_button = self.create_menu_button("Administração do Sistema")
        self.system_button = self.create_menu_button("Integridade do Sistema")
        self.correction_button = self.create_menu_button("Processo de Correção")
        self.report_button = self.create_menu_button("Relatórios de Desempenho")
        self.user_button = self.create_menu_button("Gestão de Usuários")
        self.student_button = self.create_menu_button("Gerenciar Alunos")
        self.class_button = self.create_menu_button("Gerenciar Turmas")

        self.admin_submenu = self.create_submenu([
            "Configurar Ambiente",
            "Atualizar Sistema",
            "Realizar Backup de Dados"
        ])
        self.system_submenu = self.create_submenu([
            "Verificar Base de Dados",
            "Verificar Conexão com a Internet",
            "Verificar Conexão com a API"
        ])

        self.admin_button.configure(command=lambda: self.menu_item_clicked(self.admin_submenu))
        self.system_button.configure(command=lambda: self.menu_item_clicked(self.system_submenu))
        self.correction_button.configure(command=lambda: self.menu_item_clicked(None))
        # Faça o mesmo para todos os seus botões e submenus...

    def create_menu_button(self, text):
        button = ttk.Button(self, text=text)
        button.pack(fill=tk.X)
        return button

    def create_submenu(self, items):
        submenu = tk.Frame(self.submenu_frame, borderwidth=1, relief="solid", background='light blue')
        for item in items:
            button = tk.Button(submenu, text=item, bg='light grey')
            button.pack(fill=tk.X)
        return submenu

    def menu_item_clicked(self, submenu):
        if self.callback is not None and submenu is not None:
            self.callback([button.cget("text") for button in submenu.winfo_children()])
        else:
            self.callback(None)
