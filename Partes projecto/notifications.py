#ficheiro com as funções relacionadas com as notificações

#estrutura da linha do ficheiro notificacoes.txt: nomeJogo; genero; dataCriacao\n

"""
As notificações sao guardadas num ficheiro TXT quando um jogo é adicionado à lista de jogos da aplicação.
O ficheiro notificacoes.txt é composto por uma lista de notificações, onde cada notificação é composta por:

- nome do jogo
- genero do jogo
- data de criação da notificação

Ao apagar o jogo criado da lista de jogos, a notificação é apagada do ficheiro notificacoes.txt para que o user não
continue a receber notificações de um jogo que já não existe. As notificações sao apresentadas numa scrollbox na pagina
do perfil do utilizador. Estas apenas aparecem para o utilizador caso o jogo que tenha sido adicionado à lista de jogos
seja do mesmo genero que um dos jogos favoritos do utilizador e tambem so sao apresentadas caso a data do ultimo logout seja inferior a data
de criação da notificação. Alem disto tudo o user tambem vai ter um botao chamado clear notifications que ao clicar vai limpar as notificações
que estao na scrollBar das notificações mas não apaga as notificações do ficheiro notificacoes.txt
"""

# ---------------BIBLIOTECAS ---------------------
# -----------------------------------------------------------------

import customtkinter as ctk
from tkinter import messagebox
import os
import datetime
import readFiles as rf

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
def verificarGeneroJogosFavoritos(genre, currentUser):
    """
    Função que verifica se o jogo adicionado à lista de jogos é do mesmo genero que um dos jogos favoritos do utilizador
    """
    listFavGames = rf.lerFicheiroJogosFavoritos()
    for line in listFavGames:
        game = line.split(";")
        if game[1] == currentUser and game[2] == genre:
            return True
    return False

#função que verifica se a data do ultimo logout é inferior à data de criação da notificação
def verificarDataUltimoLogout(creationDate, currentUser):
    """
    Função que verifica se a data do ultimo logout é inferior à data de criação da notificação
    """
    usersList = rf.lerFicheiroUsers()
    for line in usersList:
        user = line.split(";")
        if user[0] == currentUser:
            lastLogoutDate = user[4]
            lastLogoutDate = datetime.datetime.strptime(lastLogoutDate, "%d-%m-%Y %H:%M:%S")
            creationDate = datetime.datetime.strptime(creationDate, "%d-%m-%Y %H:%M:%S")
            if lastLogoutDate < creationDate:
                return True
    return False

#função que verifica se o utilizador tem notificações para apresentar
def verificarNotificacoes():
    """
    Função que verifica se o utilizador tem notificações para apresentar
    """
    notificationList = rf.lerFicheiroNotificacoes()
    for line in notificationList:
        notification = line.split(";")
        if verificarGeneroJogosFavoritos(notification[1]) and verificarDataUltimoLogout(notification[2]):
            return True
    return False

#função que apresenta as notificações na scrollbox
def mostrarNotificacoes():
    """
    Função que apresenta as notificações na scrollbox
    """
    notificationList = rf.lerFicheiroNotificacoes()
    for line in notificationList:
        notification = line.split(";")
        if verificarGeneroJogosFavoritos(notification[1]) and verificarDataUltimoLogout(notification[2]):
            notificationsFrame.insert("end", f"Game: {notification[0]}\nGenre: {notification[1]}\nDate: {notification[2]}\n\n")



#função que apaga uma notificação do ficheiro notificacoes.txt
def deleteNotification(gameName):
    """
    Função que apaga uma notificação do ficheiro notificacoes.txt
    """
    notificationList = rf.lerFicheiroNotificacoes()
    for line in notificationList:
        notificacao = line.split(";")
        if notificacao[0] == gameName:
            notificationList.remove(line)
    file = open("notifications.txt", "w", encoding="utf-8")
    file.writelines(notificationList)
    file.close()

def clearNotifications():
    """
    Função que limpa as notificações da scrollbox
    """
    notificationsFrame.delete(1.0, "end")