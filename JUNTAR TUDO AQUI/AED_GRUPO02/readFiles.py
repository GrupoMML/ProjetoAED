#ficheiro que contem as funcoes para ler ficheiros

#Users.txt
def lerFicheiroUsers():
    """
    Função que lê o ficheiro users.txt e retorna a lista de utilizadores
    """
    fileUsers = open(".\\files\\users.txt", "r",encoding="utf-8")
    listUsers = fileUsers.readlines()
    fileUsers.close()
    return listUsers

#Jogos.txt
def lerFicheiroJogos():
    """
    Função que lê o ficheiro jogos.txt e retorna a lista de jogos
    """
    fileJogos = open(".\\files\\jogos.txt", "r",encoding="utf-8")
    listJogos = fileJogos.readlines()
    fileJogos.close()
    return listJogos

#comentarios.txt
def lerFicheiroComentarios():
    """
    Função que lê o ficheiro comentarios.txt e retorna a lista de comentários
    """
    fileComentarios = open(".\\files\\comentarios.txt", "r",encoding="utf-8")
    listComentarios = fileComentarios.readlines()
    fileComentarios.close()
    return listComentarios

#notificacoes.txt
def lerFicheiroNotificacoes():
    """
    Função que lê o ficheiro notificacoes.txt e retorna a lista de notificações
    """
    fileNotificacoes = open(".\\files\\notificacoes.txt", "r",encoding="utf-8")
    listNotificacoes = fileNotificacoes.readlines()
    fileNotificacoes.close()
    return listNotificacoes

#jogosFavoritos.txt
def lerFicheiroJogosFavoritos():
    """
    Função que lê o ficheiro jogosFavoritos.txt e retorna a lista de jogos favoritos
    """
    fileJogosFavoritos = open(".\\files\\jogosFavoritos.txt", "r",encoding="utf-8")
    listJogosFavoritos = fileJogosFavoritos.readlines()
    fileJogosFavoritos.close()
    return listJogosFavoritos