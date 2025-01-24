#-----------------------------------------------------------------
#Ficheiro com todas a funções relacionadas com os jogos
# -----------------------------------------------------------------

# ---------------BIBLIOTECAS ---------------------
# -----------------------------------------------------------------

import customtkinter as ctk
from tkinter import messagebox
import os
import notifications as ntf
import users

# ---------------FUNCOES ---------------------
# -----------------------------------------------------------------

# ADMINISTRADOR:

def addGame():
    """
    Função que adiciona um jogo à lista de jogos
    """
    nomeJogo = entryNomeJogo.get()
    genero = entryGenero.get()
    descricao = entryDescricao.get("1.0", "end-1c")
    imagem = entryImagem.get()
    if nomeJogo == "" or genero == "" or preco == "" or descricao == "" or dataLancamento == "" or classificacao == "" or plataforma == "" or imagem == "":
        messagebox.showerror("Error", "Please fill in all fields!")
    else:
        #chamar função de notificações
        ntf.addNotification(nomeJogo,genero)
        file = open("jogos.txt", "a", encoding="utf-8")
        file.write(f"{nomeJogo};{genero};{preco};{descricao};{dataLancamento};{classificacao};{plataforma};{imagem}\n")
        file.close()
        messagebox.showinfo("Success", "Game added successfully!")
        entryNomeJogo.delete(0, "end")
        entryGenero.delete(0, "end")
        entryDescricao.delete("1.0", "end")
        entryImagem.delete(0, "end")

def deleteGame():
    """
    Função que apaga um jogo da lista de jogos
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
    Função que edita um jogo da lista de jogos
    """
    nomeJogo = entryNomeJogo.get()
    genero = entryGenero.get()
    descricao = entryDescricao.get("1.0", "end-1c")
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
                entryDescricao.delete("1.0", "end")
                entryImagem.delete(0, "end")
                break
        else:
            messagebox.showerror("Error", "Game not found!")

# UTILIZADOR:

def addGameFav(nomeJogo, currentUser,generoJogo):
    """
    Função que adiciona um jogo aos favoritos do utilizador
    """
    if nomeJogo == "":
        messagebox.showerror("Error", "Please fill in all fields!")
    else:
        listaJogos = users.lerFicheiroJogos()
        for linha in listaJogos:
            jogo = linha.split(";")
            if jogo[0] == nomeJogo:
                file = open("jogosFavoritos.txt", "a", encoding="utf-8")
                file.write(f"{currentUser};{nomeJogo};{generoJogo}\n")
                file.close()
                messagebox.showinfo("Success", "Game added to favorites successfully!")
                break
        else:
            messagebox.showerror("Error", "Game not found!")

def deleteGameFav(nomeJogo, currentUser):
    """
    Função que apaga um jogo dos favoritos do utilizador
    """
    if nomeJogo == "":
        messagebox.showerror("Error", "Please fill in all fields!")
    else:
        listaJogosFav = users.lerFicheiroJogosFavoritos()
        for linha in listaJogosFav:
            jogo = linha.split(";")
            if jogo[1] == nomeJogo and jogo[0] == currentUser:
                listaJogosFav.remove(linha)
                file = open("jogosFavoritos.txt", "w", encoding="utf-8")
                file.writelines(listaJogosFav)
                file.close()
                messagebox.showinfo("Success", "Game deleted from favorites successfully!")
                break
        else:
            messagebox.showerror("Error", "Game not found!")

def addComentario(nomeJogo, currentUser, comentario):
    """
    Função que adiciona um comentário a um jogo
    """
    if nomeJogo == "" or comentario == "":
        messagebox.showerror("Error", "Please fill in all fields!")
    else:
        file = open("comentarios.txt", "a", encoding="utf-8")
        file.write(f"{nomeJogo};{currentUser};{comentario}\n")
        file.close()
        messagebox.showinfo("Success", "Comment added successfully!")
