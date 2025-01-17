# ---------------BIBLIOTECAS ---------------------
#-----------------------------------------------------------------
import customtkinter as ctk
from tkinter import messagebox
import os
import base64
from tkinter import *
from PIL import Image

#-----------------------------------------------------------------
#---------------FUNCOES ---------------------
#-----------------------------------------------------------------
def lerFicheiroUsers():
    """
    Função que lê o ficheiro users.txt e retorna a lista de utilizadores
    """
    fileUsers = open("users.txt", "r",encoding="utf-8")
    listUsers = fileUsers.readlines()
    fileUsers.close()
    return listUsers
def deleteAccount():
    """
    Função que apaga a conta do utilizador
    """
    listaUsers = lerFicheiroUsers()
    for linha in listaUsers:
        user = linha.split(",")[0]
        if user == current_user:
            


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


# ---------------AREA UTILIZADOR (APAGAR CONTA) ---------------------
#-----------------------------------------------------------------
main_frame = ctk.CTkFrame(app, width=1280, height=832, fg_color="#2E2B2B", corner_radius=0)
main_frame.pack(fill="both", expand=True)

dlt_msg_label1 = ctk.CTkLabel(main_frame, text="THIS ACTION WILL DELETE YOUR ACCOUNT", 
                              font=ctk.CTkFont(size=45, weight="bold"), text_color="#FFA500")
dlt_msg_label1.place(relx=0.5, rely=0.3, anchor="center")

dlt_msg_label2 = ctk.CTkLabel(main_frame, text="PERMANENTLY!", 
                              font=ctk.CTkFont(size=50, weight="bold"), text_color="#FF4500")
dlt_msg_label2.place(relx=0.5, rely=0.4, anchor="center")

dlt_msg_label3 = ctk.CTkLabel(main_frame, text="ARE YOU SURE?", 
                              font=ctk.CTkFont(size=70, weight="bold"), text_color="#FFA500")
dlt_msg_label3.place(relx=0.5, rely=0.55, anchor="center")

button_frame = ctk.CTkFrame(main_frame, fg_color="#2E2B2B")
button_frame.place(relx=0.5, rely=0.75, anchor="center")

noBtn = ctk.CTkButton(button_frame, text="NO, I STILL WANNA PLAY!", fg_color="#D9D9D9", hover_color="#5A5A5A", width=300, height=60, border_color="#2E2B2B", text_color="black", font=ctk.CTkFont(size=35, weight="bold"), command=lambda: print("No Button Pressed"))
noBtn.pack(side="left", padx=10)

yesBtn = ctk.CTkButton(button_frame, text="YES, UNFORTUNATELY!", fg_color="#D9D9D9", hover_color="#5A5A5A", width=300, height=60, border_color="#2E2B2B", text_color="black", font=ctk.CTkFont(size=35, weight="bold"), command=lambda: print("Yes Button Pressed"))
yesBtn.pack(side="left", padx=10)

app.mainloop()
