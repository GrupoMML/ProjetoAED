# ---------------BIBLIOTECAS ---------------------
#-----------------------------------------------------------------
import customtkinter as ctk
from tkinter import messagebox
import os
import base64
from tkinter import *
from PIL import Image

# ---------------INICIO DA INTERFACE GRAFICA  ---------------------
#-----------------------------------------------------------------
def renderWindow(appWidth, appHeight, appTitle):
    """
    Renderiza a window da app, com as dimensões e título dos argumentos
    """
    app.title(appTitle)
    # Obter as dimensões do meu screen (em pixeis)
    screenWidth = app.winfo_screenwidth()
    screenHeight = app.winfo_screenheight()
    x = (screenWidth / 2) - (appWidth / 2)
    y = (screenHeight / 2) - (appHeight / 2)
    app.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
    app.resizable(False, False)

app = ctk.CTk()
app.configure(fg_color="black")  
app.iconbitmap(".\\Images\\1-f8c98aa8.ico")
renderWindow(1280, 832, "GameON!")

# ---------------ECRÃ INICIAL ---------------------
#-----------------------------------------------------------------
imgIcon = ctk.CTkImage(Image.open(".\\Images\\Logo.png"), size=(450, 150))
imgIcon_label = ctk.CTkLabel(app, image=imgIcon, text="")
imgIcon_label.place(relx=0.5, rely=0.35, anchor="center")

initial_msg_label = ctk.CTkLabel(app,text="WELCOME TO YOUR FAVORITE PLACE TO PLAY GAMES!",font=ctk.CTkFont(size=24, weight="bold"),text_color="white")
initial_msg_label.place(relx=0.5, rely=0.5, anchor="center")

button_frame = ctk.CTkFrame(app,width=480, height=85, fg_color="#202020",  corner_radius=15)
button_frame.place(relx=0.5, rely=0.6, anchor="center")  

initialBtn = ctk.CTkButton(button_frame,text="CLICK HERE IF YOU’RE ON!",text_color="black",fg_color="#FFA500",font=ctk.CTkFont(size=20, weight="bold"), hover_color="#FF5900",command=lambda: print("Button clicked!"),width=480,  height=85   )
initialBtn.place(relx=0.5, rely=0.5, anchor="center") 

app.mainloop()
