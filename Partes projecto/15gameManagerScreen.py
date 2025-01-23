# ---------------LIBRARIES ---------------------
# -----------------------------------------------------------------

import customtkinter as ctk
from tkinter import messagebox
import os
from tkinter import ttk
from tkinter import filedialog as fd
import users
import notifications as ntf
import games
import datetime
from PIL import Image

# ---------------START OF GRAPHICAL INTERFACE  ---------------------
#-----------------------------------------------------------------
def renderWindow(appWidth, appHeight, appTitle):
    """
    Renders the app window with the given dimensions and title
    """
    app.title(appTitle)
    # Get the screen dimensions (in pixels)
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

# ---------------FUNCTIONS ---------------------
# -----------------------------------------------------------------

# ADMINISTRATOR:

def addGame():
    """
    Function to add a game to the game list
    """
    nomeJogo = entryNomeJogo.get()
    genero = entryGenero.get()
    preco = entryPreco.get()
    descricao = entryDescricao.get("1.0", "end-1c")
    dataLancamento = entryDataLancamento.get()
    classificacao = entryClassificacao.get()
    plataforma = entryPlataforma.get()
    imagem = entryImagem.get()
    if nomeJogo == "" or genero == "" or preco == "" or descricao == "" or dataLancamento == "" or classificacao == "" or plataforma == "" or imagem == "":
        messagebox.showerror("Error", "Please fill in all fields!")
    else:
        # Call notification function
        ntf.addNotification(nomeJogo, genero)
        file = open("jogos.txt", "a", encoding="utf-8")
        file.write(f"{nomeJogo};{genero};{preco};{descricao};{dataLancamento};{classificacao};{plataforma};{imagem}\n")
        file.close()
        messagebox.showinfo("Success", "Game added successfully!")
        entryNomeJogo.delete(0, "end")
        entryGenero.delete(0, "end")
        entryPreco.delete(0, "end")
        entryDescricao.delete("1.0", "end")
        entryDataLancamento.delete(0, "end")
        entryClassificacao.delete(0, "end")
        entryPlataforma.delete(0, "end")
        entryImagem.delete(0, "end")

def deleteGame():
    """
    Function to delete a game from the game list
    """
    nomeJogo = entryNomeJogo.get()
    if nomeJogo == "":
        messagebox.showerror("Error", "Please fill in all fields!")
    else:
        ntf.deleteNotification(nomeJogo)
        listaJogos = users.lerFicheiroJogos()
        for linha in listaJogos:
            jogo = linha.split(";")
            if jogo[0] == nomeJogo:
                listaJogos.remove(linha)
                file = open("jogos.txt", "w", encoding="utf-8")
                file.writelines(listaJogos)
                file.close()
                messagebox.showinfo("Success", "Game deleted successfully!")
                entryNomeJogo.delete(0, "end")
                break
        else:
            messagebox.showerror("Error", "Game not found!")

def editGame():
    """
    Function to edit a game from the game list
    """
    nomeJogo = entryNomeJogo.get()
    genero = entryGenero.get()
    preco = entryPreco.get()
    descricao = entryDescricao.get("1.0", "end-1c")
    dataLancamento = entryDataLancamento.get()
    classificacao = entryClassificacao.get()
    plataforma = entryPlataforma.get()
    imagem = entryImagem.get()
    if nomeJogo == "" or genero == "" or preco == "" or descricao == "" or dataLancamento == "" or classificacao == "" or plataforma == "" or imagem == "":
        messagebox.showerror("Error", "Please fill in all fields!")
    else:
        listaJogos = users.lerFicheiroJogos()
        for idx, linha in enumerate(listaJogos):
            jogo = linha.split(";")
            if jogo[0] == nomeJogo and jogo[1] == genero and jogo[2] == preco and jogo[3] == descricao and jogo[4] == dataLancamento and jogo[5] == classificacao and jogo[6] == plataforma and jogo[7] == imagem:
                listaJogos[idx] = f"{nomeJogo};{genero};{preco};{descricao};{dataLancamento};{classificacao};{plataforma};{imagem}\n"
                file = open("jogos.txt", "w", encoding="utf-8")
                file.writelines(listaJogos)
                file.close()
                messagebox.showinfo("Success", "Game edited successfully!")
                entryNomeJogo.delete(0, "end")
                entryGenero.delete(0, "end")
                entryPreco.delete(0, "end")
                entryDescricao.delete("1.0", "end")
                entryImagem.delete(0, "end")
                break
        else:
            messagebox.showerror("Error", "Game not found!")

# Graphical interface

# ---------------FRAME ---------------------

# Sidebar

sidebar = ctk.CTkFrame(app, width=300, bg_color="#101010")
sidebar.pack(side=ctk.LEFT, fill=ctk.Y)

#imgIcon = ctk.CTkImage(os.path.join("Images", "Logo.png"), size=(200, 75))
imgIcon_label = ctk.CTkLabel(sidebar, text="LOGO", fg_color="#2E2B2B")
imgIcon_label.place(x=61, y=26)

button_frame = ctk.CTkFrame(sidebar)
button_frame.pack(expand=True)

buttons = ["ADD GAME", "DELETE GAME", "EDIT GAME"]
for btn in buttons:
    button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                        font=("Arial", 12), hover_color="#5A5A5A", command=lambda btn=btn: print(f"{btn}"),
                        width=247, height=44)
    button.pack(pady=5, padx=42)

# Main

main = ctk.CTkFrame(app, width=980, bg_color="#101010")
main.pack(side=ctk.RIGHT, fill=ctk.BOTH)

# ---------------ADD GAME ---------------------

addGame_frame = ctk.CTkFrame(main, width=980, height=832, bg_color="#101010")
addGame_frame.pack(fill=ctk.BOTH)

addGame_label = ctk.CTkLabel(addGame_frame, text="ADD GAME", text_color="white", font=("Arial", 18))
addGame_label.pack(pady=20)

entryNomeJogo = ctk.CTkEntry(addGame_frame, font=("Arial", 16), width=300)
entryNomeJogo.pack(pady=10)

entryGenero = ctk.CTkEntry(addGame_frame, font=("Arial", 16), width=300)
entryGenero.pack(pady=10)

entryPreco = ctk.CTkEntry(addGame_frame, font=("Arial", 16), width=300)
entryPreco.pack(pady=10)

entryDescricao = ctk.CTkTextbox(addGame_frame, font=("Arial", 16), width=300, height=10)
entryDescricao.pack(pady=10)

# ---------------DELETE GAME ---------------------

deleteGame_frame = ctk.CTkFrame(main, width=980, height=832, bg_color="#101010")
deleteGame_frame.pack(fill=ctk.BOTH)

deleteGame_label = ctk.CTkLabel(deleteGame_frame, text="DELETE GAME", text_color="white", font=("Arial", 18))
deleteGame_label.pack(pady=20)

entryNomeJogo = ctk.CTkEntry(deleteGame_frame, font=("Arial", 16), width=300)
entryNomeJogo.pack(pady=10)

# ---------------EDIT GAME ---------------------

editGame_frame = ctk.CTkFrame(main, width=980, height=832, bg_color="#101010")
editGame_frame.pack(fill=ctk.BOTH)

editGame_label = ctk.CTkLabel(editGame_frame, text="EDIT GAME", text_color="white", font=("Arial", 18))
editGame_label.pack(pady=20)

entryNomeJogo = ctk.CTkEntry(editGame_frame, font=("Arial", 16), width=300)
entryNomeJogo.pack(pady=10)

entryGenero = ctk.CTkEntry(editGame_frame, font=("Arial", 16), width=300)
entryGenero.pack(pady=10)

entryPreco = ctk.CTkEntry(editGame_frame, font=("Arial", 16), width=300)
entryPreco.pack(pady=10)

entryDescricao = ctk.CTkTextbox(editGame_frame, font=("Arial", 16), width=300, height=10)
entryDescricao.pack(pady=10)

entryDataLancamento = ctk.CTkEntry(editGame_frame, font=("Arial", 16), width=300)
entryDataLancamento.pack(pady=10)

entryClassificacao = ctk.CTkEntry(editGame_frame, font=("Arial", 16), width=300)
entryClassificacao.pack(pady=10)

entryPlataforma = ctk.CTkEntry(editGame_frame, font=("Arial", 16), width=300)
entryPlataforma.pack(pady=10)

entryImagem = ctk.CTkEntry(editGame_frame, font=("Arial", 16), width=300)
entryImagem.pack(pady=10)

# ---------------END OF GRAPHICAL INTERFACE ---------------------

app.mainloop()