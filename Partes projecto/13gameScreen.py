# ------------- BIBLIOTECAS --------------------------
# ----------------------------------------------------
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
import tkinter as tk  
import os
import base64
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
    app.resizable(True, True)

app = ctk.CTk()
app.configure(fg_color="black")  
app.iconbitmap("Images/1-f8c98aa8.ico")
app.minsize(700,600)
renderWindow(1280, 832, "GameON!")

for widget in app.winfo_children():
        widget.destroy()

# ------------------ FUNÇÕES -------------------------




# ------------------ GAME SCREEN ---------------------

sidebar = ctk.CTkFrame(app, width=330, height=830, corner_radius=0, fg_color="#2E2B2B")
sidebar.pack(side=ctk.LEFT, fill=ctk.Y)

imgIcon = ctk.CTkImage(Image.open("Images/Logo.png"), size=(200, 75))
imgIcon_label = ctk.CTkLabel(sidebar, image=imgIcon, text="", fg_color="#2E2B2B")
imgIcon_label.place(x=61, y=26)

button_frame = ctk.CTkFrame(sidebar, fg_color="#2E2B2B")
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

store_label = ctk.CTkLabel(topbar, text="STORE", text_color="white", font=("Arial", 18))
store_label.pack(side=ctk.LEFT, padx=35)

profile_circle = ctk.CTkButton(topbar, width=50, height=50, corner_radius=25,  fg_color="#FFA500",
                                text="", hover_color="#FF5900")
profile_circle.pack(side=ctk.RIGHT, padx=(0, 15), pady=30)

search_entry = ctk.CTkEntry(topbar, placeholder_text="Search...", font=("Arial", 16), width=300)
search_entry.pack(side=ctk.RIGHT, padx=20, pady=50) 

categories_frame = ctk.CTkFrame(app, fg_color="#000000", height=600)
categories_frame.pack(fill="both", padx=20, pady=10)

suggest_frame = ctk.CTkScrollableFrame(categories_frame, fg_color="#FFA500", height=600, width=580, corner_radius=10)
suggest_frame.grid(column=1, pady=(20, 10))

suggest2_frame = ctk.CTkFrame(categories_frame, fg_color="#FFA500", height=190, width=280, corner_radius=10)
suggest2_frame.grid(column=2, pady=(10, 10))

for i in range(5):
    suggest3_frame = ctk.CTkFrame(suggest_frame, fg_color="#000000", height=190, width=290, corner_radius=10)
    suggest3_frame.pack( pady=(20, 10))




app.mainloop()