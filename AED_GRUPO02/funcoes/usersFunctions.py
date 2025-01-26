# ---------------BIBLIOTECAS ---------------------
# -----------------------------------------------------------------

import customtkinter as ctk
from tkinter import messagebox
import os
import datetime
import AED_GRUPO02.funcoes.readFiles as rf
import semEncript
# ---------------FUNCOES ---------------------
# -----------------------------------------------------------------

# ADMINISTRADOR:

def addUser():
    """
    Função que adiciona um utilizador à lista de utilizadores
    """
    username = entryUsername.get()
    password = entryPassword.get()
    permLevel = entryNivelPerm.get()
    if username == ""  or password == "" or permLevel == "":
        messagebox.showerror("Error", "Please fill in all fields!")
    else:
        listaUsers = rf.lerFicheiroUsers()
        for linha in listaUsers:
            camposUser = linha.split(";")
            if camposUser[0] == username:
                messagebox.showerror("Error", "Username already exists!")
                return
            elif len(password) < 8:
                messagebox.showerror("Error", "Password must be at least 8 characters long!")
                return
            else:
                file = open("users.txt", "a", encoding="utf-8")
                file.write(f"{username};{password};{permLevel};\n")
                file.close()
                messagebox.showinfo("Success", "User added successfully!")
                entryUsername.delete(0, "end")
                entryPassword.delete(0, "end")
                return

def deleteUser():
    """
    Função que apaga um utilizador da lista de utilizadores
    """
    username = treeview.item(treeview.selection())["values"][0]
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

# UTILIZADOR:
def signinFunction(newUsernameEntry,newPasswordEntry):
    """
    Função que regista um utilizador na lista de utilizadores
    """
    username = newUsernameEntry.get()
    password = newPasswordEntry.get()
    if username == "" or password == "":
        messagebox.showerror("Error", "Please fill in all fields!")
    else:
        uList = rf.lerFicheiroUsers()
        if not uList:
            file = open(".\\files\\users.txt", "a", encoding="utf-8")
            file.write(f"{username};{password};1;\n")
            file.close()
            messagebox.showinfo("Success", "User added successfully!")
            newUsernameEntry.delete(0, "end")
            newPasswordEntry.delete(0, "end")
            return
        else:
            for linha in uList:
                camposUser = linha.split(";")
                if camposUser[0] == username:
                    messagebox.showerror("Error", "Username already exists!")
                    return
                elif len(password) < 8:
                    messagebox.showerror("Error", "Password must be at least 8 characters long!")
                    return
                else:
                    file = open("users.txt", "a", encoding="utf-8")
                    file.write(f"{username};{password};1;\n")
                    file.close()
                    messagebox.showinfo("Success", "User added successfully!")
                    newUsernameEntry.delete(0, "end")
                    newPasswordEntry.delete(0, "end")
                    return
            
def userLogin(userInput, password):
    """
    Função que faz login do utilizador
    """
    listaUsers = rf.lerFicheiroUsers()
    if userInput == "" or password == "":
        messagebox.showerror("Error", "Please fill in all fields!")
        return
    for user in listaUsers:
        userData = user.split(";")
        print(userData[0], userInput, userData[1], password)
        if userData[0] == userInput and userData[1] == password:
            currentUser = userInput
            messagebox.showinfo("Success", "Logged in successfully!")
            semEncript.welcomeUI()
    messagebox.showerror("Error", "Invalid username or password!")

def userLogout(currentUser,app):
    """
    Função que faz logout do utilizador
    """
    listaUsers = rf.lerFicheiroUsers()
    for linha in listaUsers:
        user = linha.split(";")
        if user[0] == currentUser:
            user[3] = str(datetime.datetime.now())
            listaUsers.remove(linha)
            file = open(".\\files\\users.txt", "w", encoding="utf-8")
            file.writelines(listaUsers)
            file.close()
            messagebox.showinfo("Success", "Logged out successfully!")
            app.destroy()
            return
            
def checkPermLevel(currentUser):
    """
    Função que verifica o nível de permissão do utilizador
    """
    listaUsers = rf.lerFicheiroUsers()
    for linha in listaUsers:
        user = linha.split(";")
        if user[0] == currentUser:
            return user[2]

            