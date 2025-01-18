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

# ---------------PÁGINA PRINCIPAL---------------------
#-----------------------------------------------------------------
def homePage():
    for widget in app.winfo_children():
        widget.destroy()
        
    sidebar = ctk.CTkFrame(app, width=330, height=830, corner_radius=0, bg_color="#101010")
    sidebar.pack(side=ctk.LEFT, fill=ctk.Y)

    imgIcon = ctk.CTkImage(Image.open("Images/Logo.png"), size=(200, 75))
    imgIcon_label = ctk.CTkLabel(sidebar, image=imgIcon, text="", fg_color="#2E2B2B")
    imgIcon_label.place(x=61, y=26)

    button_frame = ctk.CTkFrame(sidebar)
    button_frame.pack(expand=True)

    buttons = ["LIBRARY", "STORE", "WISHLIST", "DISCOVER"]
    for btn in buttons:
        button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                            font=("Arial", 12), hover_color="#5A5A5A", command=lambda btn=btn: print(f"{btn}"),
                            width=247, height=44)
        button.pack(pady=5, padx=42)

    profile_button_frame = ctk.CTkFrame(sidebar)
    profile_button_frame.pack(side=ctk.BOTTOM, pady=15)  

    profile_settingsBtn = ctk.CTkButton(profile_button_frame, text="PROFILE SETTINGS", text_color="white", fg_color="#FF5900",
                                        font=("Arial", 12), hover_color="#FF4500", command=app, width=247, height=44)
    profile_settingsBtn.pack(pady=5, padx=42)  

    topbar = ctk.CTkFrame(app, width=948, height=128, corner_radius=0, bg_color="#101010")
    topbar.pack(side=ctk.TOP, fill=ctk.X)
    
    home_label = ctk.CTkLabel(topbar, text="HOME", text_color="white", font=("Arial", 18))
    home_label.pack(side=ctk.LEFT, padx=35)

    profile_circle = ctk.CTkButton(topbar, width=50, height=50, corner_radius=25, fg_color="#FFA500",
                                   text="", hover_color="#FF5900")
    profile_circle.pack(side=ctk.RIGHT, padx=(0, 15), pady=30)

    search_entry = ctk.CTkEntry(topbar, placeholder_text="Search...", font=("Arial", 16), width=300)
    search_entry.pack(side=ctk.RIGHT, padx=20, pady=50) 

    # ---------------JOGO PRINCIPAL (JOGO 1)---------------------
    #-----------------------------------------------------------------
    game_section = ctk.CTkFrame(app, width=670, height=370, bg_color="#2E2B2B")
    game_section.place(x=335, y=260)  

    imgGame = ctk.CTkImage(Image.open("Images/game.png"), size=(670, 370))  
    imgGame_label = ctk.CTkLabel(game_section, image=imgGame, text="", fg_color="#2E2B2B")
    imgGame_label.place(x=0, y=0) 

    game_label = ctk.CTkLabel(app, text="ROCKET LEAGUE", text_color="white", font=("Arial", 16, "bold"))
    game_label.place(x=335, y=640)  

    game_price = ctk.CTkLabel(app, text="FREE", text_color="white", font=("Arial", 14, "bold"))
    game_price.place(x=335, y=660)  

    favorite_icon = ctk.CTkLabel(app, text="\u2764", text_color="#FF5900", font=("Arial", 16))
    favorite_icon.place(x=500, y=650)

    # ---------------JOGOS SECUNDÁRIOS (JOGOS 2 E 3)---------------------
    #-----------------------------------------------------------------

    imgGame2 = ctk.CTkImage(Image.open("Images/game.png"), size=(140, 140))
    imgGame_label2 = ctk.CTkLabel(app, image=imgGame2, text="", fg_color="#2E2B2B")
    imgGame_label2.place(x=1060, y=260)  

    imgGame3 = ctk.CTkImage(Image.open("Images/game.png"), size=(140, 140))
    imgGame_label3 = ctk.CTkLabel(app, image=imgGame3, text="", fg_color="#2E2B2B")
    imgGame_label3.place(x=1060, y=490) 


homePage()
app.mainloop()
