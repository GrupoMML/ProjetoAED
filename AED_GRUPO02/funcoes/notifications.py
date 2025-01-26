#ficheiro com as funções relacionadas com as notificações

# ---------------BIBLIOTECAS ---------------------
# -----------------------------------------------------------------

import customtkinter as ctk
from tkinter import messagebox
import os
import datetime

# ---------------FUNCOES ---------------------
# -----------------------------------------------------------------

#verifica se o ficheiro notificacoes.txt existe, caso nao exista cria um ficheiro vazio
def verificarFicheiroNotificacoes():
    """
    Função que verifica se o ficheiro notificacoes.txt existe dentro da pasta files. Caso
    não exista, cria um ficheiro vazio.
    """
    if not os.path.exists("notificacoes.txt"):
        file = open("notificacoes.txt", "w", encoding="utf-8")
        file.close()
    

#função que adiciona uma notificação ao ficheiro notificacoes.txt
def addNotification(nomeJogo, genero):
    """
    Função que adiciona uma notificação ao ficheiro notificacoes.txt
    """
    dataCriacao = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    file = open("notificacoes.txt", "a", encoding="utf-8")
    file.write(f"{nomeJogo};{genero};{dataCriacao}\n")
    file.close()

#função que verifica se o jogo adicionado à lista de jogos é do mesmo genero que um dos jogos favoritos do utilizador
def verificarGeneroJogosFavoritos(genero):
    """
    Função que verifica se o jogo adicionado à lista de jogos é do mesmo genero que um dos jogos favoritos do utilizador
    """
    listaJogosFavoritos = lerFicheiroJogosFavoritos()
    for linha in listaJogosFavoritos:
        jogo = linha.split(";")
        if jogo[1] == currentUser and jogo[2] == genero:
            return True
    return False

#função que verifica se a data do ultimo logout é inferior à data de criação da notificação
def verificarDataUltimoLogout(dataCriacao):
    """
    Função que verifica se a data do ultimo logout é inferior à data de criação da notificação
    """
    listaUsers = lerFicheiroUsers()
    for linha in listaUsers:
        user = linha.split(";")
        if user[0] == currentUser:
            dataUltimoLogout = user[4]
            if dataUltimoLogout < dataCriacao:
                return True
    return False

#função que verifica se o utilizador tem notificações para apresentar
def verificarNotificacoes():
    """
    Função que verifica se o utilizador tem notificações para apresentar
    """
    listaNotificacoes = lerFicheiroNotificacoes()
    for linha in listaNotificacoes:
        notificacao = linha.split(";")
        if verificarGeneroJogosFavoritos(notificacao[1]) and verificarDataUltimoLogout(notificacao[2]):
            return True
    return False

#função que apresenta as notificações na scrollbox
def mostrarNotificacoes():
    """
    Função que apresenta as notificações na scrollbox
    """
    listaNotificacoes = lerFicheiroNotificacoes()
    for linha in listaNotificacoes:
        notificacao = linha.split(";")
        if verificarGeneroJogosFavoritos(notificacao[1]) and verificarDataUltimoLogout(notificacao[2]):
            scrollNotificacoes.insert("end", f"Game: {notificacao[0]}\nGenre: {notificacao[1]}\nDate: {notificacao[2]}\n\n")



#função que apaga uma notificação do ficheiro notificacoes.txt
def deleteNotification(nomeJogo):
    """
    Função que apaga uma notificação do ficheiro notificacoes.txt
    """
    listaNotificacoes = lerFicheiroNotificacoes()
    for linha in listaNotificacoes:
        notificacao = linha.split(";")
        if notificacao[0] == nomeJogo:
            listaNotificacoes.remove(linha)
    file = open("notificacoes.txt", "w", encoding="utf-8")
    file.writelines(listaNotificacoes)
    file.close()

def clearNotifications():
    """
    Função que limpa as notificações da scrollbox
    """
    scrollNotificacoes.delete(1.0, "end")





