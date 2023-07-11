# app/views/board_view.py
import tkinter
from .menu_bar import MenuBar

class BoardWindow:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Login Form")
        self.window.geometry('1280x800')
        self.window.configure(bg='#FBFBFB')
        self.window.resizable(False, False)  # Desabilita redimensionamento

        self.create_widgets()

        self.window.mainloop()

    def create_widgets(self):
        all_area_frame = tkinter.Frame(self.window, bg='#FBFBFB')
        all_area_frame.pack(fill='both', expand=True)
        
        self.navigation_frame = tkinter.Frame(all_area_frame, bg='blue', width=150, height=760)
        title_frame = tkinter.Frame(self.navigation_frame, bg='blue', height=40)  # Frame para o título
        menu_frame = tkinter.Frame(self.navigation_frame, bg='blue')  # Frame para o menu

        title_frame.pack(side='top', fill='x')
        menu_frame.pack(side='top', fill='both', expand=True)

        system_label = tkinter.Label(title_frame, text="Nome do Sistema", bg='blue', fg='white', height=2)
        system_label.pack()

        content_frame = tkinter.Frame(all_area_frame, bg='pink', width=1130, height=760)
        footer_frame = tkinter.Frame(all_area_frame, bg='green', width=1280, height=40)

        top_content_frame = tkinter.Frame(content_frame, bg='orange', width=1130, height=40)
        self.left_bottom_content_frame = tkinter.Frame(content_frame, bg='yellow', width=150, height=720)
        right_bottom_content_frame = tkinter.Frame(content_frame, bg='cyan', width=980, height=720)

        top_content_frame.grid(row=0, column=0, columnspan=2, sticky='nwe')
        self.left_bottom_content_frame.grid(row=1, column=0, sticky='nwe')
        right_bottom_content_frame.grid(row=1, column=1, sticky='nwe')

        self.navigation_frame.grid(row=0, column=0, sticky='nwe')
        content_frame.grid(row=0, column=1, sticky='nwe')
        footer_frame.grid(row=1, column=0, columnspan=2, sticky='nwe')

        self.menu_bar = MenuBar(master=menu_frame, callback=self.show_submenu)
        
        all_area_frame.grid_rowconfigure(0, weight=1)
        all_area_frame.grid_columnconfigure(1, weight=1)

    def show_submenu(self, items):
        # Limpando o frame
        for widget in self.left_bottom_content_frame.winfo_children():
            widget.destroy()
        
        if items is not None:
            # Adicionando botões para cada item do submenu
            for item in items:
                button = tkinter.Button(self.left_bottom_content_frame, text=item)
                button.pack(fill='x')
        

app = BoardWindow()
