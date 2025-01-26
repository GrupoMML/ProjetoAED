#ficheiro que contem as funcoes para ler ficheiros
import os
#Users.txt
def lerFicheiroUsers():
    """
    Função que lê o ficheiro users.txt e retorna a lista de utilizadores
    """
    if not os.path.exists(".\\files\\users.txt"):
        fileUsers = open(".\\files\\users.txt", "a",encoding="utf-8")
        fileUsers.close()
    else:
        fileUsers = open(".\\files\\users.txt", "r",encoding="utf-8")
        listUsers = fileUsers.readlines()
        fileUsers.close()
        return listUsers

#Jogos.txt
def lerFicheiroJogos():
    """
    Função que lê o ficheiro jogos.txt e retorna a lista de jogos
    """
    if not os.path.exists(".\\files\\jogos.txt"):
        fileJogos = open(".\\files\\jogos.txt", "a",encoding="utf-8")
        fileJogos.close()
    else:
        fileJogos = open(".\\files\\jogos.txt", "r",encoding="utf-8")
        listJogos = fileJogos.readlines()
        fileJogos.close()
        return listJogos

#comentarios.txt
def lerFicheiroComentarios():
    """
    Função que lê o ficheiro comentarios.txt e retorna a lista de comentários
    """
    if not os.path.exists(".\\files\\comentarios.txt"):
        fileComentarios = open(".\\files\\comentarios.txt", "a",encoding="utf-8")
        fileComentarios.close()
    else:
        fileComentarios = open(".\\files\\comentarios.txt", "r",encoding="utf-8")
        listComentarios = fileComentarios.readlines()
        fileComentarios.close()
        return listComentarios

#notificacoes.txt
def lerFicheiroNotificacoes():
    """
    Função que lê o ficheiro notificacoes.txt e retorna a lista de notificações
    """
    if not os.path.exists(".\\files\\notificacoes.txt"):
        fileNotificacoes = open(".\\files\\notificacoes.txt", "a",encoding="utf-8")
        fileNotificacoes.close()
    else:
        fileNotificacoes = open(".\\files\\notificacoes.txt", "r",encoding="utf-8")
        listNotificacoes = fileNotificacoes.readlines()
        fileNotificacoes.close()
        return listNotificacoes

#jogosFavoritos.txt
def lerFicheiroJogosFavoritos():
    """
    Função que lê o ficheiro jogosFavoritos.txt e retorna a lista de jogos favoritos
    """
    if not os.path.exists(".\\files\\jogosFavoritos.txt"):
        fileJogosFavoritos = open(".\\files\\jogosFavoritos.txt", "a",encoding="utf-8")
        fileJogosFavoritos.close()
    else:
        fileJogosFavoritos = open(".\\files\\jogosFavoritos.txt", "r",encoding="utf-8")
        listJogosFavoritos = fileJogosFavoritos.readlines()
        fileJogosFavoritos.close()
        return listJogosFavoritos