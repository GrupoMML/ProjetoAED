# ---------------BIBLIOTECAS ---------------------
#-----------------------------------------------------------------
import customtkinter as ctk
from tkinter import messagebox
import os
import base64
from tkinter import *
from PIL import Image
import readFiles #ficheiro de funcoes para ler ficheiros (que já agora da para melhorar para ser so uma funcao(trabalho futuro))
import escolherImagem #ficheiro de funcoes para escolher imagem (por fazer) visto que vamos precisar de 2 funcionalidades semelhantes
# ---------------FUNCOES ---------------------
#-----------------------------------------------------------------


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

# ---------------SETTINGS---------------------
#-----------------------------------------------------------------
def settingsPage():
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

    topbar = ctk.CTkFrame(app, width=948, height=128, corner_radius=0, bg_color="#101010")
    topbar.pack(side=ctk.TOP, fill=ctk.X)
    
    settings_label = ctk.CTkLabel(topbar, text="SETTINGS", text_color="white", font=("Arial", 18))
    settings_label.pack(side=ctk.LEFT, padx=35, pady=50)

    user_info_frame = ctk.CTkFrame(app, width=875, height=450, fg_color="black")
    user_info_frame.place(x=370, y=160) 

    profile_circle = ctk.CTkButton(user_info_frame, width=154, height=154, corner_radius=77, fg_color="#FFA500", text="", hover_color="#FF5900")
    profile_circle.place(x=5, y=0)

    username_label = ctk.CTkLabel(user_info_frame, text="USERNAME", text_color="white", font=("Arial", 40, "bold"))
    username_label.place(x=200, y=10)

    personal_info = ctk.CTkLabel(user_info_frame, text="PERSONAL EMAIL:", text_color="white", font=("Arial", 22), justify="left")
    personal_info.place(x=200, y=60)

    change_password_button = ctk.CTkButton(user_info_frame, text="CHANGE PASSWORD", text_color="white", fg_color="#383838", font=("Arial", 22), hover_color="#5A5A5A", width=169, height=33)
    change_password_button.place(x=620, y=120)

    notifications_frame= ctk.CTkFrame (app, width=875, height=51, corner_radius=10, fg_color="#FFA500")
    notifications_frame.place(x=370, y=340)

    notifications_label = ctk.CTkLabel(notifications_frame, text="NOTIFICATIONS", text_color="black", font=("Arial", 22, "bold"))
    notifications_label.place(x=10, rely=0.5, anchor="w") 

    TxtObs = ctk.CTkTextbox(app, width=875, height=200, fg_color="white", text_color="black", font=("Arial", 14))
    TxtObs.place(x=370, y=400)

    msgSettings_frame= ctk.CTkFrame (app, width=663, height=52, corner_radius=10, fg_color="#FFA500")
    msgSettings_frame.place(x=370, y=680)

    msgSettings_label = ctk.CTkLabel(msgSettings_frame, text="YOU'RE A PRO PLAYER, DON'T GIVE UP", text_color="black", font=("Arial", 22, "bold"))
    msgSettings_label.place(relx=0.5, rely=0.5, anchor="center")

    logoutBtn = ctk.CTkButton(app, text="LOGOUT", text_color="white", fg_color="#FF5900", font=("Arial", 22, "bold"), hover_color="#FF4500", width=191, height=52)
    logoutBtn.place(x=1055, y=680)

    deleteAccountBtn= ctk.CTkButton(app, text="DELETE ACCOUNT", text_color="white", fg_color="#FF5900", font=("Arial", 22, "bold"), hover_color="#FF4500", width=875, height=35)
    deleteAccountBtn.place(x=370, y=750)

settingsPage()
app.mainloop()
