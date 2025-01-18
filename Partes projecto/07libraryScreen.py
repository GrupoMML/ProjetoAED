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
renderWindow(1280, 832, "GameON!")

# ---------------LIBRARY---------------------
#-----------------------------------------------------------------
def libraryPage():
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
        button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                            font=("Arial", 12), hover_color="#5A5A5A", command=lambda btn=btn: print(f"{btn}"),
                            width=247, height=44)
        button.pack(pady=5, padx=42)
    """listaUsers = lerFicheiroUsers()
    for user in listaUsers:
        campos = user.split(";")
        if campos[3] == "2": #verifica se tem permissao de administrador
            button = ctk.CTkButton(button_frame, text="ADMIN", text_color="white", fg_color="#383838",
                            font=("Arial", 12), hover_color="#5A5A5A", command=lambda btn=btn: print(f"{btn}"),
                            width=247, height=44)
            button.pack(pady=5, padx=42)"""

    profile_button_frame = ctk.CTkFrame(sidebar)
    profile_button_frame.pack(side=ctk.BOTTOM, pady=15)  

    profile_settingsBtn = ctk.CTkButton(profile_button_frame, text="PROFILE SETTINGS", text_color="white", fg_color="#FF5900",
                                        font=("Arial", 12), hover_color="#FF4500", command=app, width=247, height=44)
    profile_settingsBtn.pack(pady=5, padx=42)  

    topbar = ctk.CTkFrame(app, width=948, height=128, corner_radius=0, bg_color="#101010")
    topbar.pack(side=ctk.TOP, fill=ctk.X)
    
    discover_label = ctk.CTkLabel(topbar, text="MY LIBRARY", text_color="white", font=("Arial", 18))
    discover_label.pack(side=ctk.LEFT, padx=35)

    profile_circle = ctk.CTkButton(topbar, width=50, height=50, corner_radius=25,  fg_color="#FFA500",
                                   text="", hover_color="#FF5900")
    profile_circle.pack(side=ctk.RIGHT, padx=(0, 15), pady=30)

    search_entry = ctk.CTkEntry(topbar, placeholder_text="Search...", font=("Arial", 16), width=300)
    search_entry.pack(side=ctk.RIGHT, padx=20, pady=50) 

    categories = ["ACTION", "ADVENTURE", "RPG"]
    for idx, category in enumerate(categories):
        category_label = ctk.CTkLabel(app, text=category, font=("Arial", 14, "bold"), text_color="white")
        category_label.pack(anchor="w", padx=20, pady=10)
    
        games_frame = ctk.CTkFrame(app, fg_color="#101010")
        games_frame.pack(fill="x", padx=20, pady=10)

        for i in range(3):
            game_card = ctk.CTkFrame(games_frame, fg_color="#D9D9D9", width=250, height=295, corner_radius=10)
            game_card.pack(side=ctk.LEFT, padx=30)

            game_label = ctk.CTkLabel(game_card, text=f"GAME {i + 1}", font=("Arial", 12, "bold"), text_color="black")
            game_label.place(relx=0.5, rely=0.4, anchor="center")

            price_label = ctk.CTkLabel(game_card, text="Name game\nPrice", font=("Arial", 10), text_color="black")
            price_label.place(relx=0.5, rely=0.7, anchor="center")

            heart_icon = ctk.CTkLabel(game_card, text="\u2764", font=("Arial", 14), text_color="#FF5900")
            heart_icon.place(relx=0.9, rely=0.9, anchor="center")

libraryPage()
app.mainloop()
