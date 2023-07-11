# app/views/splash_screen.py
import tkinter as tk

class SplashScreen:
    def __init__(self, master=None):
        self.master = master
        self.splash = tk.Toplevel(self.master)
        self.splash.title('Splash Screen')
        # Defina a imagem de splash aqui
        # self.image = tk.PhotoImage(file='../resources/images/splash_image.png')
        # self.splash_label = tk.Label(self.splash, image=self.image)
        # self.splash_label.pack()

        self.splash.geometry('500x500')

    def show(self):
        self.master.withdraw()
        self.splash.deiconify()
        self.splash.after(3000, self.hide) 
        
    def hide(self):
        self.splash.withdraw()
