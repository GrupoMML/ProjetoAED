# ---------------BIBLIOTECAS ---------------------
#-----------------------------------------------------------------
import customtkinter as ctk
from tkinter import messagebox
import os
import base64
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
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

# ---------------ADICIONAR JOGO---------------------
#-----------------------------------------------------------------
def addGameFunc():
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
    
    addUser_label = ctk.CTkLabel(topbar, text="ADD GAME", text_color="white", font=("Arial", 18))
    addUser_label.pack(side=ctk.LEFT, padx=35, pady=50)

    addGameName_entry = ctk.CTkEntry(app, fg_color="white", width=290, height=37, border_color="black", corner_radius=5, 
                            placeholder_text="Game Name", placeholder_text_color="black", text_color="black",
                            font=("Arial", 12, "bold"))
    addGameName_entry.pack(padx=(50, 10), pady=(200, 10), anchor="w")

    genre_entry = ctk.CTkEntry(app, fg_color="white", width=290, height=37, border_color="black", corner_radius=5, 
                                placeholder_text="Genre", placeholder_text_color="black", text_color="black",
                                font=("Arial", 12, "bold"))
    genre_entry.pack(padx=(50, 10), anchor="w")

    # ---------------SELECIONAR IMAGEM JOGO---------------------
    #-----------------------------------------------------------------
    def selecionarImagem():  
        file_path=filedialog.askopenfilename(initialdir="./Images", title="Select Image",
                                filetypes=(("PNG Images", "*.png"), ("JPG Images", "*.jpg")))
        if file_path:
            img = ctk.CTkImage(Image.open(file_path), size=(180, 180))
            img_label.configure(image=img)

    selectImageBtn = ctk.CTkButton(app, text="SELECT IMAGE", fg_color="#FFA500", hover_color="#FF5900",
                                width=160, height=37, border_color="black", text_color="black",
                                font=ctk.CTkFont(size=20, weight="bold"), command=selecionarImagem)
    selectImageBtn.pack(padx=(50, 10), pady=10, anchor="w")

    addUserBtn = ctk.CTkButton(app, text="ADD GAME", fg_color="#FFA500", hover_color="#FF5900", width=160, height=37,
                                border_color="black", text_color="black", font=ctk.CTkFont(size=20, weight="bold"), command="")
    addUserBtn.pack(padx=(50, 10), pady=3, anchor="w")

    img_label = ctk.CTkLabel(app, text="", width=180, height=180, fg_color="#FFA500")
    img_label.place(x=900, y=300)





addGameFunc()
app.mainloop()
