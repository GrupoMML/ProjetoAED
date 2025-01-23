# ---------------BIBLIOTECAS ---------------------
#-----------------------------------------------------------------
import customtkinter as ctk
from tkinter import messagebox
import os
import base64
from tkinter import *
from PIL import Image
import datetime
import readFiles as rf

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

# ---------------ADMIN---------------------
#-----------------------------------------------------------------

# Funcoes da pagina admin
def addUser():
    """
    Função que adiciona um utilizador à lista de utilizadores
    """
    username = entryUsername.get()
    email = entryEmail.get()
    password = entryPassword.get()
    nivelPerm = entryNivelPerm.get()
    if username == "" or email == "" or password == "" or nivelPerm == "":
        messagebox.showerror("Error", "Please fill in all fields!")
    else:
        listaUsers = rf.lerFicheiroUsers()
        for linha in listaUsers:
            camposUser = linha.split(";")
            if camposUser[0] == username:
                messagebox.showerror("Error", "Username already exists!")
                return
            elif email.count("@") != 1 or email.count(".") == 0:
                messagebox.showerror("Error", "Invalid email!")
                return
            elif camposUser[1] == email:
                messagebox.showerror("Error", "Email already exists!")
                return
            elif len(password) < 8:
                messagebox.showerror("Error", "Password must be at least 8 characters long!")
                return
            else:
                file = open("users.txt", "a", encoding="utf-8")
                file.write(f"{username};{email};{password};{nivelPerm}; \n")
                file.close()
                messagebox.showinfo("Success", "User added successfully!")
                entryUsername.delete(0, "end")
                entryEmail.delete(0, "end")
                entryPassword.delete(0, "end")
                entryNivelPerm.delete(0, "end")
                return

def deleteUser():
    """
    Função que apaga um utilizador da lista de utilizadores
    """
    username = entryUsername.get()
    if username == "":
        messagebox.showerror("Error", "Please fill in all fields!")
    else:
        listaUsers = rf.lerFicheiroUsers()
        for linha in listaUsers:
            user = linha.split(";")
            if user[0] == username:
                listaUsers.remove(linha)
                file = open("users.txt", "w", encoding="utf-8")
                file.writelines(listaUsers)
                file.close()
                messagebox.showinfo("Success", "User deleted successfully!")
                entryUsername.delete(0, "end")
                return
        messagebox.showerror("Error", "User not found!")

def editUser():
    """
    Função que edita um utilizador da lista de utilizadores
    """
    username = entryUsername.get()
    email = entryEmail.get()
    password = entryPassword.get()
    nivelPerm = entryNivelPerm.get()
    if username == "" or email == "" or password == "" or nivelPerm == "":
        messagebox.showerror("Error", "Please fill in all fields!")
    else:
        listaUsers = rf.lerFicheiroUsers()
        for linha in listaUsers:
            user = linha.split(";")
            if user[0] == username:
                lastLogout = user[4]
                listaUsers.remove(linha)
                file = open("users.txt", "w", encoding="utf-8")
                file.writelines(listaUsers)
                file.close()
                file = open("users.txt", "a", encoding="utf-8")
                file.write(f"{username};{email};{password};{nivelPerm};{lastLogout}\n")
                file.close()
                messagebox.showinfo("Success", "User edited successfully!")
                entryUsername.delete(0, "end")
                entryEmail.delete(0, "end")
                entryPassword.delete(0, "end")
                entryNivelPerm.delete(0, "end")
                return
        messagebox.showerror("Error", "User not found!")


# ---------------INTERFACE GRAFICA---------------------
#-----------------------------------------------------------------

def adminPage():
    for widget in app.winfo_children():
        widget.destroy()
        
    sidebar = ctk.CTkFrame(app, width=330, height=830, corner_radius=0, bg_color="#101010")
    sidebar.pack(side=ctk.LEFT, fill=ctk.Y)

    imgIcon = ctk.CTkImage(Image.open("Images/Logo.png"), size=(200, 75))
    imgIcon_label = ctk.CTkLabel(sidebar, image=imgIcon, text="", fg_color="#2E2B2B")
    imgIcon_label.place(x=61, y=26)

    button_frame = ctk.CTkFrame(sidebar)
    button_frame.pack(expand=True)

    buttons = ["USERS", "GAMES", "STATISTICS", "SETTINGS"]
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

    topbar.pack(side=ctk.RIGHT, fill=ctk.Y)

    labelUsername = ctk.CTkLabel(topbar, text="Username", text_color="white", font=("Arial", 12), bg_color="#101010")
    labelUsername.place(x=50, y=30)

    entryUsername = ctk.CTkEntry(topbar, width=30)
    entryUsername.place(x=150, y=30)

    labelEmail = ctk.CTkLabel(topbar, text="Email", text_color="white", font=("Arial", 12), bg_color="#101010")
    labelEmail.place(x=50, y=60)

    entryEmail = ctk.CTkEntry(topbar, width=30)
    entryEmail.place(x=150, y=60)

    labelPassword = ctk.CTkLabel(topbar, text="Password", text_color="white", font=("Arial", 12), bg_color="#101010")
    labelPassword.place(x=50, y=90)

    entryPassword = ctk.CTkEntry(topbar, width=30)
    entryPassword.place(x=150, y=90)


    labelNivelPerm = ctk.CTkLabel(topbar, text="Permission Level", text_color="white", font=("Arial", 12), bg_color="#101010")
    labelNivelPerm.place(x=50, y=120)

    entryNivelPerm = ctk.CTkEntry(topbar, width=30)
    entryNivelPerm.place(x=150, y=120)

    addUserBtn = ctk.CTkButton(topbar, text="Add User", text_color="white", fg_color="#FF5900", font=("Arial", 12), bg_color="#101010", hover_color="#FF4500", command=addUser)
    addUserBtn.place(x=50, y=160)

    deleteUserBtn = ctk.CTkButton(topbar, text="Delete User", text_color="white", fg_color="#FF5900", font=("Arial", 12), bg_color="#101010", hover_color="#FF4500", command=deleteUser)
    deleteUserBtn.place(x=150, y=160)

    editUserBtn = ctk.CTkButton(topbar, text="Edit User", text_color="white", fg_color="#FF5900", font=("Arial", 12), bg_color="#101010", hover_color="#FF4500", command=editUser)
    editUserBtn.place(x=250, y=160)

    app.mainloop()

adminPage()

