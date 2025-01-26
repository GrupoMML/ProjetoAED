
# ---------------BIBLIOTECAS ---------------------
# -----------------------------------------------------------------

import customtkinter as ctk
from tkinter import messagebox
import os
import datetime
import readFiles as rf
# ---------------FUNCOES ---------------------
# -----------------------------------------------------------------

#Retorna o caminho absoluto do ficheiro Python atualmente em execução.
root_dir = os.path.dirname(os.path.abspath(__file__))
#Altera o diretório atual para o diretório do ficheiro python
os.chdir(root_dir)

# ADMINISTRADOR:

def addUser(entryUsername,entryEmail,entryPassword,entryPermLevel):
    """
    Função que adiciona um utilizador à lista de utilizadores
    """
    username = entryUsername.get()
    email = entryEmail.get()
    password = entryPassword.get()
    nivelPerm = entryPermLevel.get()
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
                file.write(f"{username};{email};{password};{nivelPerm}\n")
                file.close()
                messagebox.showinfo("Success", "User added successfully!")
                entryUsername.delete(0, "end")
                entryEmail.delete(0, "end")
                entryPassword.delete(0, "end")
                entryPermLevel.delete(0, "end")
                return

def deleteUser(entryUsername):
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

def editUser(uName,uEmail,uPassword,uPermLevel):
    """
    Função que edita um utilizador da lista de utilizadores
    """
    if uName == "" or uEmail == "" or uPassword == "" or uPermLevel == "":
        messagebox.showerror("Error", "Please fill in all fields!")
    else:
        lUsers = rf.lerFicheiroUsers()
        for line in lUsers:
            user = line.split(";")
            if user[0] == uName:
                lUsers.remove(line)
                file = open("users.txt", "w", encoding="utf-8")
                file.writelines(lUsers)
                file.close()
                file = open("users.txt", "a", encoding="utf-8")
                file.write(f"{uName};{uEmail};{uPassword};{uPermLevel};\n")
                file.close()
                messagebox.showinfo("Success", "User edited successfully!")
                entryUsername.delete(0, "end")
                entryEmail.delete(0, "end")
                entryPassword.delete(0, "end")
                entryPermLevel.delete(0, "end")
                return
        messagebox.showerror("Error", "User not found!")

# UTILIZADOR:
def signinFunction(newUsernameEntry,newEmailEntry,newPasswordEntry):
    """
    Função que regista um utilizador na lista de utilizadores
    """
    username = newUsernameEntry.get()
    email = newEmailEntry.get()
    password = newPasswordEntry.get()
    if username == "" or email == "" or password == "":
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
                file.write(f"{username};{email};{password};1;\n")
                file.close()
                messagebox.showinfo("Success", "User added successfully!")
                newUsernameEntry.delete(0, "end")
                newEmailEntry.delete(0, "end")
                newPasswordEntry.delete(0, "end")
                return

def userLogout(currentUser,app):
    """
    Função que faz logout do utilizador
    Nesta função é atualizada a data do último logout do utilizador
    caso o utilizador não tenha feito logout adiciona a data de logout quando
    o mesmo fizer logout
    """
    listaUsers = rf.lerFicheiroUsers()
    for linha in listaUsers:
        user = linha.split(";")
        if user[0] == currentUser:
            user[4] = str(datetime.datetime.now())
            listaUsers.remove(linha)
            file = open("users.txt", "w", encoding="utf-8")
            file.writelines(listaUsers)
            file.close()
            messagebox.showinfo("Success", "Logged out successfully!")
            app.destroy()
            return
            

            