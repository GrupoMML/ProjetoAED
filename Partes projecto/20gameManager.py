# ---------------BIBLIOTECAS ---------------------
#-----------------------------------------------------------------
import customtkinter as ctk
from tkinter import messagebox
import os
from tkinter import *
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
    app.resizable(True, True)

app = ctk.CTk()
app.configure(fg_color="black")  
app.iconbitmap("Images/1-f8c98aa8.ico")
renderWindow(1180, 732, "GameON!")

# ---------------PÁGINA GESTOR JOGOS---------------------
#-----------------------------------------------------------------
def gameManager():
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
                               font=("Arial", 12), hover_color="#5A5A5A", command=lambda: "",
                               width=247, height=44)
        button.pack(pady=5, padx=42)

    topbar = ctk.CTkFrame(app, width=948, height=128, corner_radius=0, bg_color="#101010")
    topbar.pack(side=ctk.TOP, fill=ctk.X)
    
    userManager_label = ctk.CTkLabel(topbar, text="USER MANAGER", text_color="white", font=("Arial", 18))
    userManager_label.pack(side=ctk.LEFT, padx=35, pady=50)

    tree_frame = ctk.CTkFrame(app, fg_color="black")
    tree_frame.pack(pady=(125, 0), padx=10, anchor="center")

    tree = ttk.Treeview(tree_frame, height=11, selectmode='browse', 
                        columns=('NAME', 'GENRE'), show='headings')
    
    tree.column('NAME', width=200, anchor='center')
    tree.column('GENRE', width=200, anchor='center')
    tree.heading('NAME', text='NAME')
    tree.heading('GENRE', text='GENRE')
    tree.pack(side="left")

    verticalScrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
    verticalScrollbar.pack(side="right", fill="y")
    tree.configure(yscrollcommand=verticalScrollbar.set)

    button_frame = ctk.CTkFrame(app, fg_color="black")
    button_frame.pack(pady=(10, 0), anchor="center")

    addBtn = ctk.CTkButton(button_frame, text="ADD", fg_color="#FFA500", hover_color="#FF5900", 
                           width=140, height=37, text_color="black", font=ctk.CTkFont(size=20, weight="bold"), command="")
    addBtn.pack(side="left", padx=10)

    editBtn = ctk.CTkButton(button_frame, text="EDIT", fg_color="#FFA500", hover_color="#FF5900", 
                            width=140, height=37, text_color="black", font=ctk.CTkFont(size=20, weight="bold"), command="")
    editBtn.pack(side="left", padx=10)

    deleteBtn = ctk.CTkButton(button_frame, text="DELETE", fg_color="#FFA500", hover_color="#FF5900", 
                              width=140, height=37, text_color="black", font=ctk.CTkFont(size=20, weight="bold"), command="")
    deleteBtn.pack(side="left", padx=10)

gameManager()
app.mainloop()
