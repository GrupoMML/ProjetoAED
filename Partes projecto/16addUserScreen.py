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
app.iconbitmap("Images/1-f8c98aa8.ico")
renderWindow(1180, 732, "GameON!")

# ---------------ADICIONAR UTILIZADOR---------------------
#-----------------------------------------------------------------
def addUserFunc():
    for widget in app.winfo_children():
        widget.destroy()
        
    sidebar = ctk.CTkFrame(app, width=330, height=830, corner_radius=0, bg_color="#101010")
    sidebar.pack(side=ctk.LEFT, fill=ctk.Y)

    imgIcon = ctk.CTkImage(Image.open("Images/Logo.png"), size=(200, 75))
    imgIcon_label = ctk.CTkLabel(sidebar, image=imgIcon, text="", fg_color="#2E2B2B")
    imgIcon_label.place(x=61, y=26)

    button_frame = ctk.CTkFrame(sidebar)
    button_frame.pack(expand=True)

    buttons = ["LIBRARY", "STORE", "DISCOVER"]
    for btn in buttons:
        if btn == "LIBRARY":
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:"",
                                width=247, height=44)
        elif btn == "STORE":
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:"",
                                width=247, height=44)
        else:  
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:"",
                                width=247, height=44)
        button.pack(pady=5, padx=42)

    topbar = ctk.CTkFrame(app, width=948, height=128, corner_radius=0, bg_color="#101010")
    topbar.pack(side=ctk.TOP, fill=ctk.X)
    
    addUser_label = ctk.CTkLabel(topbar, text="ADD USER", text_color="white", font=("Arial", 18))
    addUser_label.pack(side=ctk.LEFT, padx=35, pady=50)

    addUsername_entry = ctk.CTkEntry(app, fg_color="white", width=290, height=37, border_color="black", corner_radius=5, 
                            placeholder_text="USERNAME", placeholder_text_color="black", text_color="black",
                            font=("Arial", 12, "bold"))
    addUsername_entry.pack(padx=250, pady=(200, 10), anchor="center")

    addPassword_entry = ctk.CTkEntry(app, fg_color="white", show="*", width=290, height=37, border_color="black", corner_radius=5, 
                                placeholder_text="PASSWORD", placeholder_text_color="black", text_color="black",
                                font=("Arial", 12, "bold"))
    addPassword_entry.pack(padx=250, anchor="center")

    radioBtn_frame = ctk.CTkFrame(app, fg_color="transparent")
    radioBtn_frame.pack(pady=20, anchor="center")

    radio_value = ctk.StringVar(value="admin")

    radioBtn1 = ctk.CTkRadioButton(radioBtn_frame, text="ADMIN", fg_color="#FFA500", font=("Arial", 12), value="admin", variable=radio_value)
    radioBtn1.pack(side=ctk.LEFT, padx=10)

    radioBtn2 = ctk.CTkRadioButton(radioBtn_frame, text="USER", fg_color="#FFA500", font=("Arial", 12), value="user", variable=radio_value)
    radioBtn2.pack(side=ctk.LEFT, padx=10)

    addUserBtn = ctk.CTkButton(app, text="ADD USER", fg_color="#FFA500", hover_color="#FF5900", width=140, height=37,
                                border_color="black", text_color="black",font=ctk.CTkFont(size=20, weight="bold"), command="")
    addUserBtn.pack(pady=20, anchor="center")

addUserFunc()
app.mainloop()
