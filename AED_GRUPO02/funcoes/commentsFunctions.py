#Ficheiro python com funcionalidades relacionadas com comentários
import datetime
import os
import AED_GRUPO02.funcoes.readFiles as rf
import customtkinter as ctk


def addComment(game,comment,user,rating):
    """
    Função que adiciona um comentário ao ficheiro comentarios.txt
    """
    dataCriacao = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    file = open("comentarios.txt", "a", encoding="utf-8")
    file.write(f"{game};{comment};{user};{rating};{dataCriacao}\n")
    file.close()

def showComments(game):
    """
    Função que mostra os comentários de um jogo dentro de uma frame na interface gráfica
    """
    listaComentarios = rf.lerFicheiroComentarios()
    for linha in listaComentarios:
        comentario = linha.split(";")
        if comentario[0] == game:
            comment_frame = ctk.CTkFrame(ctk.app, width=948, height=128, corner_radius=0, bg_color="#101010")
            comment_frame.pack(side=ctk.TOP, fill=ctk.X)
            comment_label = ctk.CTkLabel(comment_frame, text=f"User: {comentario[2]}\nRating: {comentario[3]}\nComment: {comentario[1]}", text_color="white", font=("Arial", 12))
            comment_label.pack(side=ctk.LEFT, padx=35, pady=50)
    return comment_frame


            

