# ---------------BIBLIOTECAS ---------------------
#-----------------------------------------------------------------
import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox, ttk, Canvas
import os
import datetime
from PIL import Image, ImageDraw
import readFiles 
import shutil

#Retorna o caminho absoluto do ficheiro Python atualmente em execução.
root_dir = os.path.dirname(os.path.abspath(__file__))
#Altera o diretório atual para o diretório do ficheiro python
os.chdir(root_dir)

#cria a pasta files se não existir
if not os.path.exists(".\\files"):
    os.makedirs(".\\files")


# ---------------VARIAVEIS GLOBAIS---------------------
#-----------------------------------------------------------------
currentUser = ""
profile_circle = None

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
    app.resizable(True, True)

app = ctk.CTk()
app.configure(fg_color="black")  
app.iconbitmap("Images/1-f8c98aa8.ico")
renderWindow(1180, 732, "GameON!")
# ---------------FUNCOES ---------------------
# -----------------------------------------------------------------

#função que adiciona uma notificação ao ficheiro notificacoes.txt
def addNotification(nomeJogo, genero):
    """
    Função que adiciona uma notificação ao ficheiro notificacoes.txt
    """
    dataCriacao = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    file = open("files/notificacoes.txt", "a", encoding="utf-8")
    file.write(f"{nomeJogo};{genero};{dataCriacao}\n")
    file.close()

#função que verifica se o jogo adicionado à lista de jogos é do mesmo genero que um dos jogos favoritos do utilizador
def verificarGeneroJogosFavoritos(genero):
    """
    Função que verifica se o jogo adicionado à lista de jogos é do mesmo genero que um dos jogos favoritos do utilizador
    """
    listaJogosFavoritos = readFiles.lerFicheiroJogosFavoritos()
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
    listaUsers = readFiles.lerFicheiroUsers()
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
    listaNotificacoes = readFiles.lerFicheiroNotificacoes()
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
    listaNotificacoes = readFiles.lerFicheiroNotificacoes()
    for linha in listaNotificacoes:
        notificacao = linha.split(";")
        if verificarGeneroJogosFavoritos(notificacao[1]) and verificarDataUltimoLogout(notificacao[2]):
            scrollNotificacoes.insert("end", f"Game: {notificacao[0]}\nGenre: {notificacao[1]}\nDate: {notificacao[2]}\n\n")

#função que apaga uma notificação do ficheiro notificacoes.txt
def deleteNotification(nomeJogo):
    """
    Função que apaga uma notificação do ficheiro notificacoes.txt
    """
    listaNotificacoes = readFiles.lerFicheiroNotificacoes()
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
            comment_frame = ctk.CTkFrame(app, width=948, height=128, corner_radius=0, bg_color="#101010")
            comment_frame.pack(side=ctk.TOP, fill=ctk.X)
            comment_label = ctk.CTkLabel(comment_frame, text=f"User: {comentario[2]}\nRating: {comentario[3]}\nComment: {comentario[1]}", text_color="white", font=("Arial", 12))
            comment_label.pack(side=ctk.LEFT, padx=35, pady=50)
    return comment_frame

#FUNCOES DOS JOGOS
# ADMINISTRADOR:

def addGame(entryNomeJogo, entryGenero, entryDescricao, imagePath):
    """
    Função que adiciona um jogo à lista de jogos
    """
    nomeJogo = entryNomeJogo
    genero = entryGenero
    descricao = entryDescricao
    if nomeJogo == "" or genero == "" or descricao == ""  or imagePath == "":
        messagebox.showerror("Error", "Please fill in all fields!")
    else:
        #chamar função de notificações
        addNotification(nomeJogo,genero)
        file = open("files/jogos.txt", "a", encoding="utf-8")
        file.write(f"{nomeJogo};{genero};{descricao};{imagePath}\n")
        file.close()
        messagebox.showinfo("Success", "Game added successfully!")
        entryNomeJogo.delete(0, "end")
        entryGenero.delete(0, "end")
        entryDescricao.delete("1.0", "end")

def deleteGame():
    """
    Função que apaga um jogo da lista de jogos
    """
    if nomeJogo == "":
        messagebox.showerror("Error", "Please fill in all fields!")
    else:
        deleteNotification(nomeJogo)
        listaJogos = users.lerFicheiroJogos()
        for linha in listaJogos:
            jogo = linha.split(";")
            if jogo[0] == nomeJogo:
                listaJogos.remove(linha)
                file = open("jogos.txt", "w", encoding="utf-8")
                file.writelines(listaJogos)
                file.close()
                messagebox.showinfo("Success", "Game deleted successfully!")
                break
        else:
            messagebox.showerror("Error", "Game not found!")

# UTILIZADOR:

def addGameFav():
    """
    Função que adiciona um jogo aos favoritos do utilizador quando este clica num botão
    """

"""
def deleteGameFav(treeview):
    
    #Função que apaga um jogo dos favoritos do utilizador
    
    if treeview.selection() == "":
        messagebox.showerror("Error", "Please select a game!")
    else:
        gameName = treeview.item(treeview.selection())["values"][0]
        lfavGames = users.lerFicheiroJogosFavoritos()
        for line in lfavGames:
            game = line.split(";")
            if game[0] == gameName and game[1] == currentUser:
                lfavGames.remove(line)
                file = open("jogosFavoritos.txt", "w", encoding="utf-8")
                file.writelines(lfavGames)
                file.close()
                messagebox.showinfo("Success", "Game deleted from favorites successfully!")
                break
        else:
            messagebox.showerror("Error", "Game not found!")"""

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

def showFavGames(currentUser):
    """
    Função que apresenta os jogos favoritos do utilizador
    """
    listaJogosFav = readFiles.lerFicheiroJogosFavoritos()
    for linha in listaJogosFav:
        jogo = linha.split(";")
        if jogo[0] == currentUser:
            scrollFavGames.insert("end", f"Game: {jogo[1]}\nGenre: {jogo[2]}\n\n")

def showGames():
    """
    Função que apresenta 
    """
    listaJogos = users.lerFicheiroJogos()
    for linha in listaJogos:
        jogo = linha.split(";")
        scrollGames.insert("end", f"Game: {jogo[0]}\nGenre: {jogo[1]}\nPrice: {jogo[2]}\nDescription: {jogo[3]}\nRelease Date: {jogo[4]}\nRating: {jogo[5]}\nPlatform: {jogo[6]}\n\n")

#Funções dos users
# ADMINISTRADOR:

def addUser( entryUsername, entryPassword, entryPermLevel):
    """
    Função que adiciona um utilizador à lista de utilizadores
    """
    username = entryUsername.get()
    password = entryPassword.get()
    permLevel = entryPermLevel.get()
    if username == ""  or password == "" or permLevel == "":
        messagebox.showerror("Error", "Please fill in all fields!")
    else:
        listaUsers = readFiles.lerFicheiroUsers()
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

def deleteUser(treeview):
    """
    Função que apaga um utilizador da lista de utilizadores
    """
    username = treeview.item(treeview.selection())["values"][0]
    if username == "":
        messagebox.showerror("Error", "Please fill in all fields!")
    else:
        listaUsers = readFiles.lerFicheiroUsers()
        for linha in listaUsers:
            user = linha.split(";")
            if user[0] == username:
                listaUsers.remove(linha)
                file = open("users.txt", "w", encoding="utf-8")
                file.writelines(listaUsers)
                file.close()
                messagebox.showinfo("Success", "User deleted successfully!")
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
        uList = readFiles.lerFicheiroUsers()
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
                    file = open(".\\files\\users.txt", "a", encoding="utf-8")
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
    listaUsers = readFiles.lerFicheiroUsers()
    if userInput == "" or password == "":
        messagebox.showerror("Error", "Please fill in all fields!")
        return 
    for user in listaUsers:
        userData = user.split(";")
        print(userData[0], userInput, userData[1], password)
        if userData[0] == userInput and userData[1] == password:
            global currentUser
            currentUser = userInput
            welcomeUI()
            return currentUser
    messagebox.showerror("Error", "Invalid username or password!")
    return currentUser

def userLogout(application):
    """
    Função que faz logout do utilizador
    """
    listaUsers = readFiles.lerFicheiroUsers()
    for linha in listaUsers:
        user = linha.split(";")
        if user[0] == user:
            user[3] = str(datetime.datetime.now())
            listaUsers.remove(linha)
            file = open(".\\files\\users.txt", "w", encoding="utf-8")
            file.writelines(listaUsers)
            file.close()
            messagebox.showinfo("Success", "Logged out successfully!")
            app.destroy()
            return
            
def checkPermLevel(user):
    """
    Função que verifica o nível de permissão do utilizador
    """
    listaUsers = readFiles.lerFicheiroUsers()
    for linha in listaUsers:
        user = linha.split(";")
        if user[0] == currentUser:
            return user[2]

# ---------------FRAMES ---------------------
#-----------------------------------------------------------------
def showFrame(frame):
    """
    Oculta todos os frames e exibe apenas o especificado.
    """
    for widget in app.winfo_children():
        widget.destroy()
    frame.pack(fill="both", expand=True)

# ---------------SELECIONAR IMAGEM ---------------------
#-----------------------------------------------------------------
def selectProfileImage():
    file_path = filedialog.askopenfilename(initialdir="./Images", title="Select Image",
                                           filetypes=(("PNG Images", "*.png"), ("JPG Images", "*.jpg")))
    if file_path:
        img = Image.open(file_path).resize((100, 100), Image.Resampling.LANCZOS)
        mask = Image.new("L", (100, 100), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, 100, 100), fill=255)
        img.putalpha(mask)
        
        save_path = f"Images/pfp/{currentUser}.png" 
        os.makedirs(os.path.dirname(save_path), exist_ok=True) 
        img.save(save_path)

        profile_img = ctk.CTkImage(img, size=(100, 100))
        # Atualizar a imagem no botão globalmente
        profile_circle.configure(image=profile_img, fg_color="transparent")
        profile_circle.image = profile_img

def loginUI():
    # --------------DESIGN LOGIN ---------------------
    #-----------------------------------------------------------------
    login_frame = ctk.CTkFrame(app, width=800, height=500, fg_color="#2E2B2B", corner_radius=15)
    login_frame.place(relx=0.5, rely=0.5, anchor="center")

    imgIcon = ctk.CTkImage(Image.open("Images/Logo.png"), size=(290, 100))
    imgIcon_label = ctk.CTkLabel(login_frame, image=imgIcon, text="", fg_color="#2E2B2B")
    imgIcon_label.place(relx=0.5, rely=0.2, anchor="center")

    input_frame = ctk.CTkFrame(login_frame, width=550, height=350, fg_color="#2E2B2B")
    input_frame.place(relx=0.5, rely=0.6, anchor="center")  

    username_entry = ctk.CTkEntry(input_frame, fg_color="white", width=290, height=37, border_color="#2E2B2B", corner_radius=5, 
                                placeholder_text="USERNAME", placeholder_text_color="black", text_color="black",
                                font=("Arial", 12, "bold"))
    username_entry.pack(pady=5, anchor="center")

    password_entry = ctk.CTkEntry(input_frame, fg_color="white", show="*", width=290, height=37, border_color="#2E2B2B", corner_radius=5, 
                                placeholder_text="PASSWORD", placeholder_text_color="black", text_color="black",
                                font=("Arial", 12, "bold"))
    password_entry.pack(pady=5, anchor="center")

    login_button_frame = ctk.CTkFrame(input_frame, fg_color="#2E2B2B")
    login_button_frame.pack(pady=(20, 20), anchor="center")

    loginBtn = ctk.CTkButton(login_button_frame, text="LOGIN", fg_color="#FFA500", hover_color="#FF5900", width=140, height=37, 
                                border_color="#2E2B2B", text_color="black", font=ctk.CTkFont(size=20, weight="bold"), command=lambda:userLogin(username_entry.get(),password_entry.get()))
    loginBtn.pack(side="left", padx=5, anchor="center")

    signinBtn = ctk.CTkButton(login_button_frame, text="SIGN IN", fg_color="#FFA500", hover_color="#FF5900", width=140, height=37, 
                                border_color="#2E2B2B", text_color="black", font=ctk.CTkFont(size=20, weight="bold"), command=lambda: signinUI())
    signinBtn.pack(side="left", padx=5, anchor="center")

    qrcode_frame = ctk.CTkFrame(input_frame, fg_color="#2E2B2B")
    qrcode_frame.pack(pady=(5, 20), anchor="center")

    qrcodeBtn = ctk.CTkButton(qrcode_frame, text="QR CODE", fg_color="#FFA500", hover_color="#FF5900", 
                                width=292, height=37, border_color="#2E2B2B", text_color="black", 
                                font=ctk.CTkFont(size=20, weight="bold"), command=lambda: qrcodeFunction())
    qrcodeBtn.pack(padx=5, anchor="center")
    
def signinUI():
    # --------------DESIGN SIGN IN ---------------------
    #-----------------------------------------------------------------
    signin_frame = ctk.CTkFrame(app, width=800, height=500, fg_color="#2E2B2B", corner_radius=15)
    signin_frame.place(relx=0.5, rely=0.5, anchor="center")

    imgIcon = ctk.CTkImage(Image.open("Images/Logo.png"), size=(290, 100))
    imgIcon_label = ctk.CTkLabel(signin_frame, image=imgIcon, text="", fg_color="#2E2B2B")
    imgIcon_label.place(relx=0.5, rely=0.2, anchor="center")

    input_frame = ctk.CTkFrame(signin_frame, width=550, height=350, fg_color="#2E2B2B")
    input_frame.place(relx=0.5, rely=0.6, anchor="center")  

    username_entry = ctk.CTkEntry(input_frame, fg_color="white", width=290, height=37, border_color="#2E2B2B", corner_radius=5, 
                                placeholder_text="USERNAME", placeholder_text_color="black", text_color="black",
                                font=("Arial", 12, "bold"))
    username_entry.pack(pady=5, anchor="center")

    password_entry = ctk.CTkEntry(input_frame, fg_color="white", show="*", width=290, height=37, border_color="#2E2B2B", corner_radius=5, 
                                placeholder_text="PASSWORD", placeholder_text_color="black", text_color="black",
                                font=("Arial", 12, "bold"))
    password_entry.pack(pady=5, anchor="center")

    button_frame = ctk.CTkFrame(input_frame, fg_color="#2E2B2B")
    button_frame.pack(pady=(20, 20), anchor="center")

    signinBtn = ctk.CTkButton(button_frame, text="SIGN IN", fg_color="#FFA500", hover_color="#FF5900", width=140, height=37, 
                                border_color="#2E2B2B", text_color="black", font=ctk.CTkFont(size=20, weight="bold"), command=lambda: signinFunction(username_entry, password_entry))
    signinBtn.pack(side="left", padx=5, anchor="center")

    backBtn = ctk.CTkButton(button_frame, text="BACK", fg_color="#FFA500", hover_color="#FF5900", width=140, height=37, 
                                border_color="#2E2B2B", text_color="black", font=ctk.CTkFont(size=20, weight="bold"), command=lambda:loginUI())
    backBtn.pack(side="left", padx=5, anchor="center")

"""
def qrcodeFunction():
    # --------------FUNCIONALIDADES E DESIGN QR CODE ---------------------
    #-----------------------------------------------------------------
    qrcode_frame = ctk.CTkFrame(app, width=800, height=500, fg_color="#2E2B2B", corner_radius=15)
    qrcode_frame.place(relx=0.5, rely=0.5, anchor="center")

    imgIcon = ctk.CTkImage(Image.open("Images/Logo.png"), size=(290, 100))
    imgIcon_label = ctk.CTkLabel(qrcode_frame, image=imgIcon, text="", fg_color="#2E2B2B")
    imgIcon_label.place(relx=0.5, rely=0.2, anchor="center")

    input_frame = ctk.CTkFrame(qrcode_frame, width=550, height=350, fg_color="#2E2B2B")
    input_frame.place(relx=0.5, rely=0.9, anchor="center")  

    msg_qrcode_label = ctk.CTkLabel(qrcode_frame, text="SCAN & GO!", font=ctk.CTkFont(size=24, weight="bold"), text_color="white")
    msg_qrcode_label.place(relx=0.5, rely=0.3, anchor="center")

    imgQR = ctk.CTkImage(Image.open("Images/frame.png"), size=(239, 239))
    imgQR_label = ctk.CTkLabel(qrcode_frame, image=imgQR, text="", fg_color="#2E2B2B")
    imgQR_label.place(relx=0.5, rely=0.6, anchor="center") 

    button_frame = ctk.CTkFrame(input_frame, fg_color="#2E2B2B")
    button_frame.pack(pady=(20, 20), anchor="center")

    backBtn = ctk.CTkButton(button_frame, text="BACK", fg_color="#FFA500", hover_color="#FF5900", width=140, height=37, 
                                border_color="#2E2B2B", text_color="black", font=ctk.CTkFont(size=20, weight="bold"), command=lambda:loginUI())
    backBtn.pack(side="left", padx=5, anchor="center")

    app.after(5000, welcomeUI)
"""
def draw_loading_circle(canvas, angle):
    # ---------------CANVAS PARA O LOADING ---------------------
    #-----------------------------------------------------------------
    canvas.delete("all")  
    canvas.create_oval(10, 10, 102, 102, width=10, outline="gray") 
    canvas.create_arc(10, 10, 102, 102, start=angle, extent=270, width=10, outline="orange") 

def update_loading_circle(canvas, angle):
    # ---------------CANVAS PARA O LOADING ---------------------
    #-----------------------------------------------------------------
    angle += 10  
    if angle >= 360:
        angle = 0  
    draw_loading_circle(canvas, angle)
    canvas.after(50, update_loading_circle, canvas, angle) 

def welcomeUI():
    # --------------DESIGN BEM VINDO ---------------------
    #-----------------------------------------------------------------
    
    welcome_frame = ctk.CTkFrame(app, width=1180, height=732, fg_color="black")
    welcome_frame.place(relx=0.5, rely=0.5, anchor="center")

    imgIcon = ctk.CTkImage(Image.open("Images/Logo.png"), size=(450, 150))
    imgIcon_label = ctk.CTkLabel(app, image=imgIcon, text="")
    imgIcon_label.place(relx=0.5, rely=0.35, anchor="center")

    msg_welcome_label = ctk.CTkLabel(app, text="WELCOME!", font=ctk.CTkFont(size=24, weight="bold"), text_color="white")
    msg_welcome_label.place(relx=0.5, rely=0.50, anchor="center")

    loading_canvas = tk.Canvas(app, width=120, height=120, bg="black", bd=0, highlightthickness=0)
    loading_canvas.place(relx=0.5, rely=0.65, anchor="center")

    update_loading_circle(loading_canvas, 0)

    msg_loading_label = ctk.CTkLabel(app, text="LOADING...", font=ctk.CTkFont(size=24, weight="bold"), text_color="white")
    msg_loading_label.place(relx=0.5, rely=0.80, anchor="center")

    app.after(5000, storePageUI)

def storePageUI():
    # --------------DESIGN PÁGINA STORE ---------------------
    #-----------------------------------------------------------------
    for widget in app.winfo_children():
        widget.destroy()

    sidebar = ctk.CTkFrame(app, width=330, height=830, corner_radius=0, bg_color="#101010")
    sidebar.pack(side=ctk.LEFT, fill=ctk.Y)

    imgIcon = ctk.CTkImage(Image.open("Images/Logo.png"), size=(200, 75))
    imgIcon_label = ctk.CTkLabel(sidebar, image=imgIcon, text="", fg_color="#2E2B2B")
    imgIcon_label.place(x=61, y=26)

    button_frame = ctk.CTkFrame(sidebar)
    button_frame.pack(expand=True)

    buttons = ["STORE", "LIBRARY", "ADMIN"]
    for btn in buttons:
        if btn == "STORE":
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:storePageUI(),
                                width=247, height=44)
        elif btn == "LIBRARY":
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:libraryPageUI(),
                                width=247, height=44)
        elif btn == "ADMIN" and checkPermLevel(currentUser) == "2":
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:adminPageUI(),
                                width=247, height=44)
        button.pack(pady=5, padx=42)

    global profile_circle

    profile_button_frame = ctk.CTkFrame(sidebar)
    profile_button_frame.pack(side=ctk.BOTTOM, pady=15)  

    profile_settingsBtn = ctk.CTkButton(profile_button_frame, text="PROFILE SETTINGS", text_color="white", fg_color="#FF5900",
                                        font=("Arial", 12), hover_color="#FF4500", command=lambda:settingsPageUI(), width=247, height=44)
    profile_settingsBtn.pack(pady=5, padx=42)  

    topbar = ctk.CTkFrame(app, width=948, height=128, corner_radius=0, bg_color="#101010")
    topbar.pack(side=ctk.TOP, fill=ctk.X)
    
    store_label = ctk.CTkLabel(topbar, text="STORE", text_color="white", font=("Arial", 18))
    store_label.pack(side=ctk.LEFT, padx=35)

    profile_circle = ctk.CTkButton(topbar, width=50, height=50, corner_radius=25,  fg_color="#FFA500",
                                   text="", hover_color="#FF5900", command=lambda:settingsPageUI())
    profile_circle.pack(side=ctk.RIGHT, padx=(0, 15), pady=30)

    search_entry = ctk.CTkEntry(topbar, placeholder_text="Search...", font=("Arial", 16), width=300)
    search_entry.pack(side=ctk.RIGHT, padx=20, pady=50) 

    game_frame = ctk.CTkFrame(app, fg_color="#101010", width=800, height=400)
    game_frame.pack(pady=100)

    gamesList = readFiles.lerFicheiroJogos()
    for line in gamesList:
        game = line.split(";")
        game_image = ctk.CTkImage(Image.open(game[3]), size=(200, 300))
        game_button = ctk.CTkButton(game_frame, image=game_image, text="", fg_color="#101010", width=200, height=300,
                                    command=lambda: gameAspect(game[0],game[1],game[2],game[3]))
        game_button.place(x=30, y=26)
        gameTxt = ctk.CTkLabel(game_frame, text=game[0], text_color="white", font=("Arial", 18))
        gameTxt.place(x=100, y=340)

def libraryPageUI():
    # --------------DESIGN PÁGINA BIBLIOTECA ---------------------
    #-----------------------------------------------------------------
    for widget in app.winfo_children():
        widget.destroy()
    
    sidebar = ctk.CTkFrame(app, width=330, height=830, corner_radius=0, bg_color="#101010")
    sidebar.pack(side=ctk.LEFT, fill=ctk.Y)

    imgIcon = ctk.CTkImage(Image.open("Images/Logo.png"), size=(200, 75))
    imgIcon_label = ctk.CTkLabel(sidebar, image=imgIcon, text="", fg_color="#2E2B2B")
    imgIcon_label.place(x=61, y=26)

    button_frame = ctk.CTkFrame(sidebar)
    button_frame.pack(expand=True)

    buttons = ["STORE", "LIBRARY", "ADMIN"]
    for btn in buttons:
        if btn == "STORE":
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:storePageUI(),
                                width=247, height=44)
        elif btn == "LIBRARY":
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:libraryPageUI(),
                                width=247, height=44)
        elif btn == "ADMIN" and checkPermLevel(currentUser) == "2":
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:adminPageUI(),
                                width=247, height=44)
        button.pack(pady=5, padx=42)

    profile_button_frame = ctk.CTkFrame(sidebar)
    profile_button_frame.pack(side=ctk.BOTTOM, pady=15)  

    profile_settingsBtn = ctk.CTkButton(profile_button_frame, text="PROFILE SETTINGS", text_color="white", fg_color="#FF5900",
                                        font=("Arial", 12), hover_color="#FF4500", command=lambda:settingsPageUI(), width=247, height=44)
    profile_settingsBtn.pack(pady=5, padx=42)  

    topbar = ctk.CTkFrame(app, width=948, height=128, corner_radius=0, bg_color="#101010")
    topbar.pack(side=ctk.TOP, fill=ctk.X)
    
    discover_label = ctk.CTkLabel(topbar, text="MY LIBRARY", text_color="white", font=("Arial", 18))
    discover_label.pack(side=ctk.LEFT, padx=35)

    profile_circle = ctk.CTkButton(topbar, width=50, height=50, corner_radius=25,  fg_color="#FFA500",
                                   text="", hover_color="#FF5900", command=lambda:settingsPageUI())
    profile_circle.pack(side=ctk.RIGHT, padx=(0, 15), pady=30)

    search_entry = ctk.CTkEntry(topbar, placeholder_text="Search...", font=("Arial", 16), width=300)
    search_entry.pack(side=ctk.RIGHT, padx=20, pady=50) 

    game_frame = ctk.CTkFrame(app, fg_color="#101010", width=800, height=400)
    game_frame.pack(pady=100)

    game1_image = ctk.CTkImage(Image.open("Images/game.png"), size=(200, 300))
    game1_button = ctk.CTkButton(game_frame, image=game1_image, text="", fg_color="#101010", width=200, height=300,
                                 command=lambda: gameAspect())
    game1_button.place(x=30, y=26)
    game1Txt = ctk.CTkLabel(game_frame, text="GAME 1", text_color="white", font=("Arial", 18))
    game1Txt.place(x=100, y=340)

    game2_image = ctk.CTkImage(Image.open("Images/game.png"), size=(200, 300))
    game2_button = ctk.CTkButton(game_frame, image=game2_image, text="", fg_color="#101010", width=200, height=300,
                                 command=lambda: gameAspect())
    game2_button.place(x=310, y=26)
    game2Txt = ctk.CTkLabel(game_frame, text="GAME 2", text_color="white", font=("Arial", 18))
    game2Txt.place(x=380, y=340)

    game3_image = ctk.CTkImage(Image.open("Images/game.png"), size=(200, 300))
    game3_button = ctk.CTkButton(game_frame, image=game3_image, text="", fg_color="#101010", width=200, height=300,
                                 command=lambda: gameAspect())
    game3_button.place(x=580, y=26)
    game3Txt = ctk.CTkLabel(game_frame, text="GAME 3", text_color="white", font=("Arial", 18))
    game3Txt.place(x=650, y=340)

def adminPageUI():
    # ---------------PÁGINA ADMIN---------------------
    #-----------------------------------------------------------------
    for widget in app.winfo_children():
        widget.destroy()
        
    sidebar = ctk.CTkFrame(app, width=330, height=830, corner_radius=0, bg_color="#101010")
    sidebar.pack(side=ctk.LEFT, fill=ctk.Y)

    imgIcon = ctk.CTkImage(Image.open("Images/Logo.png"), size=(200, 75))
    imgIcon_label = ctk.CTkLabel(sidebar, image=imgIcon, text="", fg_color="#2E2B2B")
    imgIcon_label.place(x=61, y=26)

    button_frame = ctk.CTkFrame(sidebar)
    button_frame.pack(expand=True)

    buttons = ["STORE", "LIBRARY", "ADMIN"]
    for btn in buttons:
        if btn == "STORE":
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:storePageUI(),
                                width=247, height=44)
        elif btn == "LIBRARY":
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:libraryPageUI(),
                                width=247, height=44)
        elif btn == "ADMIN" and checkPermLevel(currentUser) == "2":
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:adminPageUI(),
                                width=247, height=44)
        button.pack(pady=5, padx=42)

    profile_button_frame = ctk.CTkFrame(sidebar)
    profile_button_frame.pack(side=ctk.BOTTOM, pady=15)  

    profile_settingsBtn = ctk.CTkButton(profile_button_frame, text="PROFILE SETTINGS", text_color="white", fg_color="#FF5900",
                                        font=("Arial", 12), hover_color="#FF4500", command=lambda:settingsPageUI(), width=247, height=44)
    profile_settingsBtn.pack(pady=5, padx=42)  

    topbar = ctk.CTkFrame(app, width=948, height=128, corner_radius=0, bg_color="#101010")
    topbar.pack(side=ctk.TOP, fill=ctk.X)
    
    admin_label = ctk.CTkLabel(topbar, text="ADMIN", text_color="white", font=("Arial", 18))
    admin_label.pack(side=ctk.LEFT, padx=35, pady=50)

    button_frame = ctk.CTkFrame(app, fg_color="black")
    button_frame.pack(pady=(80, 0), anchor="center")

    userManagerBtn = ctk.CTkButton(button_frame, text="USER MANAGER", fg_color="#FFA500", hover_color="#FF5900", width=140, height=37, 
                                border_color="#2E2B2B", text_color="black", font=ctk.CTkFont(size=20, weight="bold"), command=lambda: usersManagerUI())
    userManagerBtn.pack(side="left", padx=50, anchor="center")

    gamesManagerBtn = ctk.CTkButton(button_frame, text="GAME MANAGER", fg_color="#FFA500", hover_color="#FF5900", width=140, height=37, 
                                border_color="#2E2B2B", text_color="black", font=ctk.CTkFont(size=20, weight="bold"), command=lambda: gamesManagerUI())
    gamesManagerBtn.pack(side="left", padx=50, anchor="center")

    label_frame = ctk.CTkFrame(app, fg_color="black")
    label_frame.pack(pady=(50, 0), anchor="center")

    totalUsers_label = ctk.CTkLabel(label_frame, text="TOTAL USERS:", text_color="white", font=("Arial", 18))
    totalUsers_label.pack(side="left", padx=50, anchor="center")

    totalGames_label = ctk.CTkLabel(label_frame, text="TOTAL GAMES:", text_color="white", font=("Arial", 18))
    totalGames_label.pack(side="left", padx=50, anchor="center")

    def graphFunc():
        data = [10, 20, 30, 40, 50]  
        labels = ['A', 'B', 'C', 'D', 'E'] 
        
        canvas.delete("all")  

        bar_width = 40  
        spacing = 30  

        for i, value in enumerate(data):
            x1 = i * (bar_width + spacing) + 50 
            y1 = 300 
            x2 = x1 + bar_width  
            y2 = y1 - value  

            canvas.create_rectangle(x1, y1, x2, y2, fill="orange")
            
            canvas.create_text(x1 + bar_width / 2, y1 + 20, text=labels[i], fill="white")
        
        for i, value in enumerate(data):
            canvas.create_text(i * (bar_width + spacing) + 50 + bar_width / 2, y1 - value - 10, 
                            text=str(value), fill="black")
            
    canvas = ctk.CTkCanvas(app, width=500, height=300, bg="black")
    canvas.pack(pady=20)

    draw_button = ctk.CTkButton(app, text="DRAW GRAPH", fg_color="#FFA500", hover_color="#FF5900", width=140, height=37, 
                                border_color="#2E2B2B", text_color="black", font=ctk.CTkFont(size=20, weight="bold"), command=lambda:graphFunc())
    draw_button.pack()

def gameAspect(gameName):
    # ---------------ASPECTO JOGOS---------------------
    #-----------------------------------------------------------------
    for widget in app.winfo_children():
        widget.destroy()

    sidebar = ctk.CTkFrame(app, width=330, height=830, corner_radius=0, bg_color="#101010")
    sidebar.pack(side=ctk.LEFT, fill=ctk.Y)

    imgIcon = ctk.CTkImage(Image.open("Images/Logo.png"), size=(200, 75))
    imgIcon_label = ctk.CTkLabel(sidebar, image=imgIcon, text="", fg_color="#2E2B2B")
    imgIcon_label.place(x=61, y=26)

    button_frame = ctk.CTkFrame(sidebar)
    button_frame.pack(expand=True)

    buttons = ["STORE", "LIBRARY", "ADMIN"]
    for btn in buttons:
        if btn == "STORE":
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:storePageUI(),
                                width=247, height=44)
        elif btn == "LIBRARY":
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:libraryPageUI(),
                                width=247, height=44)
        elif btn == "ADMIN" and checkPermLevel(currentUser) == "2":
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:adminPageUI(),
                                width=247, height=44)
        button.pack(pady=5, padx=42)

    profile_button_frame = ctk.CTkFrame(sidebar)
    profile_button_frame.pack(side=ctk.BOTTOM, pady=15)  

    profile_settingsBtn = ctk.CTkButton(profile_button_frame, text="PROFILE SETTINGS", text_color="white", fg_color="#FF5900",
                                        font=("Arial", 12), hover_color="#FF4500", command=lambda:settingsPageUI(), width=247, height=44)
    profile_settingsBtn.pack(pady=5, padx=42)  

    topbar = ctk.CTkFrame(app, width=948, height=128, corner_radius=0, bg_color="#101010")
    topbar.pack(side=ctk.TOP, fill=ctk.X)
    
    game_label = ctk.CTkLabel(topbar, text="GAME NAME", text_color="white", font=("Arial", 18))
    game_label.pack(side=ctk.LEFT, padx=35)

    profile_circle = ctk.CTkButton(topbar, width=50, height=50, corner_radius=25,  fg_color="#FFA500",
                                   text="", hover_color="#FF5900", command=lambda:settingsPageUI())
    profile_circle.pack(side=ctk.RIGHT, padx=(0, 15), pady=30)

    search_entry = ctk.CTkEntry(topbar, placeholder_text="Search...", font=("Arial", 16), width=300)
    search_entry.pack(side=ctk.RIGHT, padx=20, pady=50) 

    imgGame = ctk.CTkImage(Image.open("Images/game.png"), size=(200, 300))
    imgGame_label = ctk.CTkLabel(app, image=imgGame, text="", fg_color="#2E2B2B")
    imgGame_label.place(x=350, y=200)

    nameGame_label = ctk.CTkLabel(app, text=gameName, text_color="white", font=("Arial", 18))
    nameGame_label.place(x=580, y=220)

    gameDescription=ctk.CTkTextbox(app, width=480, height=180, fg_color="white", font=("Arial", 12), text_color="black")
    gameDescription.place(x=350, y=520)

    saveBtn = ctk.CTkButton(app, text="SAVE", fg_color="#FFA500", hover_color="#FF5900", width=140, height=37,
                            border_color="black", text_color="black",font=ctk.CTkFont(size=20, weight="bold"), command=lambda: addGameFav())
    saveBtn.place(x=580, y=260) 

    backBtn = ctk.CTkButton(app, text="BACK", fg_color="#FFA500", hover_color="#FF5900",
                            width=292, height=37, border_color="#2E2B2B", text_color="black", 
                            font=ctk.CTkFont(size=20, weight="bold"), command=lambda:storePageUI())
    backBtn.place(x=350, y=150)

    comment_frame=ctk.CTkFrame(app, fg_color="#101010", width=300, height=520, corner_radius=10)
    comment_frame.place(x=860, y=150)

    commentZone=ctk.CTkTextbox(comment_frame, width=280, height=100, fg_color="white", font=("Arial", 12), text_color="black")
    commentZone.place(x=10, y=20)

    commentZone2=ctk.CTkTextbox(comment_frame, width=280, height=100, fg_color="white", font=("Arial", 12), text_color="black")
    commentZone2.place(x=10, y=150)

    commentZone3=ctk.CTkTextbox(comment_frame, width=280, height=100, fg_color="white", font=("Arial", 12), text_color="black")
    commentZone3.place(x=10, y=280)

    commentZone3=ctk.CTkTextbox(comment_frame, width=280, height=100, fg_color="white", font=("Arial", 12), text_color="black")
    commentZone3.place(x=10, y=410)

    createCommentBtn = ctk.CTkButton(app, text="CRATE A COMMENT", fg_color="#FFA500", hover_color="#FF5900",
                            width=300, height=37, border_color="#2E2B2B", text_color="black", 
                            font=ctk.CTkFont(size=20, weight="bold"), command=lambda:commentsPage())
    createCommentBtn.place(x=860, y=680)

def commentsPage():
    # ---------------PÁGINA COMENTÁRIOS---------------------
    #-----------------------------------------------------------------
    for widget in app.winfo_children():
        widget.destroy()

    sidebar = ctk.CTkFrame(app, width=330, height=830, corner_radius=0, bg_color="#101010")
    sidebar.pack(side=ctk.LEFT, fill=ctk.Y)

    imgIcon = ctk.CTkImage(Image.open("Images/Logo.png"), size=(200, 75))
    imgIcon_label = ctk.CTkLabel(sidebar, image=imgIcon, text="", fg_color="#2E2B2B")
    imgIcon_label.place(x=61, y=26)

    button_frame = ctk.CTkFrame(sidebar)
    button_frame.pack(expand=True)

    buttons = ["STORE", "LIBRARY", "ADMIN"]
    for btn in buttons:
        if btn == "STORE":
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:storePageUI(),
                                width=247, height=44)
        elif btn == "LIBRARY":
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:libraryPageUI(),
                                width=247, height=44)
        elif btn == "ADMIN" and checkPermLevel(currentUser) == "2":
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:adminPageUI(),
                                width=247, height=44)
        button.pack(pady=5, padx=42)

    profile_button_frame = ctk.CTkFrame(sidebar)
    profile_button_frame.pack(side=ctk.BOTTOM, pady=15)  

    profile_settingsBtn = ctk.CTkButton(profile_button_frame, text="PROFILE SETTINGS", text_color="white", fg_color="#FF5900",
                                        font=("Arial", 12), hover_color="#FF4500", command=lambda:settingsPageUI(), width=247, height=44)
    profile_settingsBtn.pack(pady=5, padx=42)  

    topbar = ctk.CTkFrame(app, width=948, height=128, corner_radius=0, bg_color="#101010")
    topbar.pack(side=ctk.TOP, fill=ctk.X)
    
    commentsZone_label = ctk.CTkLabel(topbar, text="COMMENTS ZONE", text_color="white", font=("Arial", 18))
    commentsZone_label.pack(side=ctk.LEFT, padx=35)

    profile_circle = ctk.CTkButton(topbar, width=50, height=50, corner_radius=25,  fg_color="#FFA500",
                                   text="", hover_color="#FF5900", command=lambda:settingsPageUI())
    profile_circle.pack(side=ctk.RIGHT, padx=(0, 15), pady=30)

    search_entry = ctk.CTkEntry(topbar, placeholder_text="Search...", font=("Arial", 16), width=300)
    search_entry.pack(side=ctk.RIGHT, padx=20, pady=50) 

    ratingList = ["Select..." ,"1", "2", "3", "4", "5"]

    rating_label= ctk.CTkLabel(app, text="Rating", text_color="white", font=("Arial", 18))
    rating_label.place(x=540, y=200)

    rating=ctk.CTkComboBox(app, width=300, height=37, fg_color="white", values= ratingList, font=("Arial", 12), text_color="black", state="readonly")
    rating.place(x=640, y=200)
    rating.set("Select...")

    commentTxt=ctk.CTkTextbox(app, width=500, height=300, fg_color="white", font=("Arial", 12), text_color="black")
    commentTxt.place(x=480, y=260)

    commentBtn = ctk.CTkButton(app, text="COMMENT HERE", fg_color="#FFA500", hover_color="#FF5900",
                            width=292, height=37, border_color="#2E2B2B", text_color="black", 
                            font=ctk.CTkFont(size=20, weight="bold"), command=lambda:"")
    commentBtn.place(x=580, y=600)

    backBtn = ctk.CTkButton(app, text="BACK", fg_color="#FFA500", hover_color="#FF5900",
                            width=292, height=37, border_color="#2E2B2B", text_color="black", 
                            font=ctk.CTkFont(size=20, weight="bold"), command=lambda:gameAspect())
    backBtn.place(x=580, y=650)

def settingsPageUI():
    # --------------DESIGN PÁGINA SETTINGS ---------------------
    #-----------------------------------------------------------------
    for widget in app.winfo_children():
        widget.destroy()

    sidebar = ctk.CTkFrame(app, width=330, height=830, corner_radius=0, bg_color="#101010")
    sidebar.pack(side=ctk.LEFT, fill=ctk.Y)

    imgIcon = ctk.CTkImage(Image.open("Images/Logo.png"), size=(200, 75))
    imgIcon_label = ctk.CTkLabel(sidebar, image=imgIcon, text="", fg_color="#2E2B2B")
    imgIcon_label.place(x=61, y=26)

    button_frame = ctk.CTkFrame(sidebar)
    button_frame.pack(expand=True)

    buttons = ["STORE", "LIBRARY", "ADMIN"]
    for btn in buttons:
        if btn == "STORE":
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:storePageUI(),
                                width=247, height=44)
        elif btn == "LIBRARY":
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:libraryPageUI(),
                                width=247, height=44)
        elif btn == "ADMIN" and checkPermLevel(currentUser) == "2":
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:adminPageUI(),
                                width=247, height=44)
        button.pack(pady=5, padx=42)

    profile_button_frame = ctk.CTkFrame(sidebar)
    profile_button_frame.pack(side=ctk.BOTTOM, pady=15)  

    profile_settingsBtn = ctk.CTkButton(profile_button_frame, text="PROFILE SETTINGS", text_color="white", fg_color="#FF5900",
                                        font=("Arial", 12), hover_color="#FF4500", command=lambda:settingsPageUI(), width=247, height=44)
    profile_settingsBtn.pack(pady=5, padx=42)  

    topbar = ctk.CTkFrame(app, width=948, height=128, corner_radius=0, bg_color="#101010")
    topbar.pack(side=ctk.TOP, fill=ctk.X)
    
    settings_label = ctk.CTkLabel(topbar, text="SETTINGS", text_color="white", font=("Arial", 18))
    settings_label.pack(side=ctk.LEFT, padx=35, pady=50)

    user_info_frame = ctk.CTkFrame(app, width=875, height=450, fg_color="black")
    user_info_frame.place(x=370, y=160) 

    global profile_circle
    profile_circle = ctk.CTkButton(user_info_frame, width=100, height=100, corner_radius=77, fg_color="#FFA500", text="", hover_color="#FF5900", command=lambda:selectProfileImage())
    profile_circle.place(x=5, y=5)

    username_label = ctk.CTkLabel(user_info_frame, text=currentUser , text_color="white", font=("Arial", 40, "bold"))
    username_label.place(x=120, y=15)

    notifications_frame= ctk.CTkFrame (app, width=800, height=51, corner_radius=10, fg_color="#FFA500")
    notifications_frame.place(x=370, y=300)

    notifications_label = ctk.CTkLabel(notifications_frame, text="NOTIFICATIONS", text_color="black", font=("Arial", 22, "bold"))
    notifications_label.place(x=10, rely=0.5, anchor="w") 

    notification_frame = ctk.CTkScrollableFrame(app, width=775, height=200, fg_color="white")
    notification_frame.place(x=370, y=360)

    msgSettings_frame= ctk.CTkFrame (app, width=600, height=52, corner_radius=10, fg_color="#FFA500")
    msgSettings_frame.place(x=370, y=580)

    msgSettings_label = ctk.CTkLabel(msgSettings_frame, text="YOU'RE A PRO PLAYER, DON'T GIVE UP", text_color="black", font=("Arial", 22, "bold"))
    msgSettings_label.place(relx=0.5, rely=0.5, anchor="center")

    logoutBtn = ctk.CTkButton(app, text="LOGOUT", text_color="white", fg_color="#FF5900", font=("Arial", 22, "bold"), hover_color="#FF4500", width=191, height=52, command=lambda:loginUI())
    logoutBtn.place(x=980, y=580)

    deleteAccountBtn= ctk.CTkButton(app, text="DELETE ACCOUNT", text_color="white", fg_color="#FF5900", font=("Arial", 22, "bold"), hover_color="#FF4500", width=800, height=55, command=lambda:deletePageUI())
    deleteAccountBtn.place(x=370, y=650)

def addGameUI():
    # Variável para armazenar o caminho da imagem selecionada
    selected_image_path = [None]  # Usar uma lista para permitir a modificação no escopo interno

    # ---------------PÁGINA ADICIONAR JOGO---------------------
    # -----------------------------------------------------------------
    for widget in app.winfo_children():
        widget.destroy()
        
    sidebar = ctk.CTkFrame(app, width=330, height=830, corner_radius=0, bg_color="#101010")
    sidebar.pack(side=ctk.LEFT, fill=ctk.Y)

    imgIcon = ctk.CTkImage(Image.open("Images/Logo.png"), size=(200, 75))
    imgIcon_label = ctk.CTkLabel(sidebar, image=imgIcon, text="", fg_color="#2E2B2B")
    imgIcon_label.place(x=61, y=26)

    button_frame = ctk.CTkFrame(sidebar)
    button_frame.pack(expand=True)

    buttons = ["STORE", "LIBRARY", "ADMIN"]
    for btn in buttons:
        if btn == "STORE":
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:storePageUI(),
                                width=247, height=44)
        elif btn == "LIBRARY":
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:libraryPageUI(),
                                width=247, height=44)
        else:  
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:adminPageUI(),
                                width=247, height=44)
        button.pack(pady=5, padx=42)

    topbar = ctk.CTkFrame(app, width=948, height=128, corner_radius=0, bg_color="#101010")
    topbar.pack(side=ctk.TOP, fill=ctk.X)
    
    addGame_label = ctk.CTkLabel(topbar, text="ADD GAME", text_color="white", font=("Arial", 18))
    addGame_label.pack(side=ctk.LEFT, padx=35, pady=50)

    addGameName_entry = ctk.CTkEntry(app, fg_color="white", width=290, height=37, border_color="black", corner_radius=5, 
                            placeholder_text="Game Name", placeholder_text_color="black", text_color="black",
                            font=("Arial", 12, "bold"))
    addGameName_entry.pack(padx=(50, 10), pady=(100, 10), anchor="w")

    genre_entry = ctk.CTkEntry(app, fg_color="white", width=290, height=37, border_color="black", corner_radius=5, 
                                placeholder_text="Genre", placeholder_text_color="black", text_color="black",
                                font=("Arial", 12, "bold"))
    genre_entry.pack(padx=(50, 10), anchor="w")

    description = ctk.CTkTextbox(app, width=300, height=180, fg_color="white", text_color="black", font=("Arial", 14))
    description.place(x=780, y=180)

    # ---------------SELECIONAR IMAGEM JOGO---------------------
    # -----------------------------------------------------------------
    def selectImage(gameName):  
        file_path = filedialog.askopenfilename(initialdir="./Images", title="Select Image",
                                filetypes=(("PNG Images", "*.png"), ("JPG Images", "*.jpg")))
        if file_path:
            # Atualizar o caminho da imagem na variável global
            selected_image_path[0] = f"Images/games/{gameName}.png"

            # Salvar a imagem com o nome do jogo
            os.makedirs(os.path.dirname(selected_image_path[0]), exist_ok=True)  # Criar a pasta se não existir
            Image.open(file_path).save(selected_image_path[0])  # Salvar a imagem original no local especificado
            print(f"Imagem salva como: {selected_image_path[0]}")

            # Atualizar a imagem exibida
            img = ctk.CTkImage(Image.open(file_path), size=(180, 180))
            img_label.configure(image=img)

    selectImageBtn = ctk.CTkButton(app, text="SELECT IMAGE", fg_color="#FFA500", hover_color="#FF5900",
                                width=160, height=37, border_color="black", text_color="black",
                                font=ctk.CTkFont(size=20, weight="bold"), command=lambda:selectImage(addGameName_entry.get()))
    selectImageBtn.pack(padx=260, pady=140, anchor="center")

    img_label = ctk.CTkLabel(app, text="", width=180, height=180, fg_color="white")
    img_label.place(x=900, y=380) 

    # Botão para adicionar o jogo, passando o caminho da imagem
    addGameBtn = ctk.CTkButton(app, text="ADD GAME", fg_color="#FFA500", hover_color="#FF5900", width=140, height=37, 
                             border_color="#2E2B2B", text_color="black", font=ctk.CTkFont(size=20, weight="bold"), 
                             command=lambda:addGame(addGameName_entry.get(), genre_entry.get(), description.get("1.0", "end"), selected_image_path[0]))
    addGameBtn.pack(side="left", padx=(250,5), pady=(0,0) ,anchor="center")

    backBtn = ctk.CTkButton(app, text="BACK", fg_color="#FFA500", hover_color="#FF5900", width=140, height=37, 
                                border_color="#2E2B2B", text_color="black", font=ctk.CTkFont(size=20, weight="bold"), command=lambda:gamesManagerUI())
    backBtn.pack(side="left", padx=5, pady=(0,0), anchor="center")


def addUserUI():
    # ---------------ADICIONAR UTILIZADOR---------------------
    #-----------------------------------------------------------------
    for widget in app.winfo_children():
        widget.destroy()
        
    sidebar = ctk.CTkFrame(app, width=330, height=830, corner_radius=0, bg_color="#101010")
    sidebar.pack(side=ctk.LEFT, fill=ctk.Y)

    imgIcon = ctk.CTkImage(Image.open("Images/Logo.png"), size=(200, 75))
    imgIcon_label = ctk.CTkLabel(sidebar, image=imgIcon, text="", fg_color="#2E2B2B")
    imgIcon_label.place(x=61, y=26)

    button_frame = ctk.CTkFrame(sidebar)
    button_frame.pack(expand=True)

    buttons = ["STORE", "LIBRARY", "ADMIN"]
    for btn in buttons:
        if btn == "STORE":
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:storePageUI(),
                                width=247, height=44)
        elif btn == "LIBRARY":
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:libraryPageUI(),
                                width=247, height=44)
        else:  
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:adminPageUI(),
                                width=247, height=44)
        button.pack(pady=5, padx=42)

    topbar = ctk.CTkFrame(app, width=948, height=128, corner_radius=0, bg_color="#101010")
    topbar.pack(side=ctk.TOP, fill=ctk.X)
    
    addUser_label = ctk.CTkLabel(topbar, text="ADD USER", text_color="white", font=("Arial", 18))
    addUser_label.pack(side=ctk.LEFT, padx=35, pady=50)

    addUsername_entry = ctk.CTkEntry(app, fg_color="white", width=290, height=37, border_color="black", corner_radius=5, 
                            placeholder_text="USERNAME", placeholder_text_color="black", text_color="black",
                            font=("Arial", 12, "bold"))
    addUsername_entry.pack(padx=250, pady=(200, 10), anchor="center")

    addPassword_entry = ctk.CTkEntry(app, fg_color="white", show="*", width=290, height=37, border_color="black", corner_radius=5, 
                                placeholder_text="PASSWORD", placeholder_text_color="black", text_color="black",
                                font=("Arial", 12, "bold"))
    addPassword_entry.pack(padx=250, anchor="center")

    radioBtn_frame = ctk.CTkFrame(app, fg_color="transparent")
    radioBtn_frame.pack(pady=20, anchor="center")

    radio_value = ctk.StringVar(value="1")

    radioBtn1 = ctk.CTkRadioButton(radioBtn_frame, text="ADMIN", fg_color="#FFA500", font=("Arial", 12), value="2", variable=radio_value)
    radioBtn1.pack(side=ctk.LEFT, padx=10)

    radioBtn2 = ctk.CTkRadioButton(radioBtn_frame, text="USER", fg_color="#FFA500", font=("Arial", 12), value="1", variable=radio_value)
    radioBtn2.pack(side=ctk.LEFT, padx=10)

    addUserBtn = ctk.CTkButton(app, text="ADD USER", fg_color="#FFA500", hover_color="#FF5900", width=292, height=37,
                                border_color="black", text_color="black",font=ctk.CTkFont(size=20, weight="bold"), command="")
    addUserBtn.pack(pady=20, anchor="center")

    backBtn = ctk.CTkButton(app, text="BACK", fg_color="#FFA500", hover_color="#FF5900", 
                              width=292, height=37, border_color="#2E2B2B", text_color="black", 
                              font=ctk.CTkFont(size=20, weight="bold"), command=lambda:usersManagerUI())
    backBtn.pack(padx=5, pady=0, anchor="center")

def usersManagerUI():
    # ---------------PÁGINA GESTOR UTILIZADORES---------------------
    #-----------------------------------------------------------------
    for widget in app.winfo_children():
        widget.destroy()
        
    sidebar = ctk.CTkFrame(app, width=330, height=830, corner_radius=0, bg_color="#101010")
    sidebar.pack(side=ctk.LEFT, fill=ctk.Y)

    imgIcon = ctk.CTkImage(Image.open("Images/Logo.png"), size=(200, 75))
    imgIcon_label = ctk.CTkLabel(sidebar, image=imgIcon, text="", fg_color="#2E2B2B")
    imgIcon_label.place(x=61, y=26)

    button_frame = ctk.CTkFrame(sidebar)
    button_frame.pack(expand=True)

    buttons = ["STORE", "LIBRARY", "ADMIN"]
    for btn in buttons:
        if btn == "STORE":
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:storePageUI(),
                                width=247, height=44)
        elif btn == "LIBRARY":
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:libraryPageUI(),
                                width=247, height=44)
        else:  
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:adminPageUI(),
                                width=247, height=44)
        button.pack(pady=5, padx=42)

    topbar = ctk.CTkFrame(app, width=948, height=128, corner_radius=0, bg_color="#101010")
    topbar.pack(side=ctk.TOP, fill=ctk.X)
    
    userManager_label = ctk.CTkLabel(topbar, text="USER MANAGER", text_color="white", font=("Arial", 18))
    userManager_label.pack(side=ctk.LEFT, padx=35, pady=50)

    tree_frame = ctk.CTkFrame(app, fg_color="black")
    tree_frame.pack(pady=(125, 0), padx=10, anchor="center")

    tree = ttk.Treeview(tree_frame, height=11, selectmode='browse', 
                        columns=('NAME', 'PERMISSIONS'), show='headings')
    
    tree.column('NAME', width=200, anchor='center')
    tree.column('PERMISSIONS', width=200, anchor='center')
    tree.heading('NAME', text='NAME')
    tree.heading('PERMISSIONS', text='PERMISSIONS')
    tree.pack(side="left")

    verticalScrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
    verticalScrollbar.pack(side="right", fill="y")
    tree.configure(yscrollcommand=verticalScrollbar.set)

    button_frame = ctk.CTkFrame(app, fg_color="black")
    button_frame.pack(pady=(20, 0), anchor="center")

    addBtn = ctk.CTkButton(button_frame, text="ADD", fg_color="#FFA500", hover_color="#FF5900", 
                           width=140, height=37, text_color="black", font=ctk.CTkFont(size=20, weight="bold"), command=lambda: addUserUI())
    addBtn.pack(side="left", padx=10)

    editBtn = ctk.CTkButton(button_frame, text="EDIT", fg_color="#FFA500", hover_color="#FF5900", 
                            width=140, height=37, text_color="black", font=ctk.CTkFont(size=20, weight="bold"), command="")
    editBtn.pack(side="left", padx=10)

    deleteBtn = ctk.CTkButton(button_frame, text="DELETE", fg_color="#FFA500", hover_color="#FF5900", 
                              width=140, height=37, text_color="black", font=ctk.CTkFont(size=20, weight="bold"), command="")
    deleteBtn.pack(side="left", padx=10)

    backBtn = ctk.CTkButton(app, text="BACK", fg_color="#FFA500", hover_color="#FF5900", 
                              width=292, height=37, border_color="#2E2B2B", text_color="black", 
                              font=ctk.CTkFont(size=20, weight="bold"), command=lambda:adminPageUI())
    backBtn.pack(padx=5, pady=20, anchor="center")

def gamesManagerUI():
    # ---------------PÁGINA GESTOR JOGOS---------------------
    #-----------------------------------------------------------------
    for widget in app.winfo_children():
        widget.destroy()
        
    sidebar = ctk.CTkFrame(app, width=330, height=830, corner_radius=0, bg_color="#101010")
    sidebar.pack(side=ctk.LEFT, fill=ctk.Y)

    imgIcon = ctk.CTkImage(Image.open("Images/Logo.png"), size=(200, 75))
    imgIcon_label = ctk.CTkLabel(sidebar, image=imgIcon, text="", fg_color="#2E2B2B")
    imgIcon_label.place(x=61, y=26)

    button_frame = ctk.CTkFrame(sidebar)
    button_frame.pack(expand=True)

    buttons = ["STORE", "LIBRARY", "ADMIN"]
    for btn in buttons:
        if btn == "STORE":
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:storePageUI(),
                                width=247, height=44)
        elif btn == "LIBRARY":
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:libraryPageUI(),
                                width=247, height=44)
        else:  
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:adminPageUI(),
                                width=247, height=44)
        button.pack(pady=5, padx=42)

    topbar = ctk.CTkFrame(app, width=948, height=128, corner_radius=0, bg_color="#101010")
    topbar.pack(side=ctk.TOP, fill=ctk.X)
    
    userManager_label = ctk.CTkLabel(topbar, text="GAME MANAGER", text_color="white", font=("Arial", 18))
    userManager_label.pack(side=ctk.LEFT, padx=35, pady=50)

    tree_frame = ctk.CTkFrame(app, fg_color="black")
    tree_frame.pack(pady=(125, 0), padx=10, anchor="center")

    tree = ttk.Treeview(tree_frame, height=11, selectmode='browse', 
                        columns=('NAME', 'GENRE'), show='headings')
    
    tree.column('NAME', width=200, anchor='center')
    tree.column('GENRE', width=200, anchor='center')
    tree.heading('NAME', text='NAME')
    tree.heading('GENRE', text='GENRE')
    tree.pack(side="left")

    verticalScrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
    verticalScrollbar.pack(side="right", fill="y")
    tree.configure(yscrollcommand=verticalScrollbar.set)

    button_frame = ctk.CTkFrame(app, fg_color="black")
    button_frame.pack(pady=(20, 0), anchor="center")

    addBtn = ctk.CTkButton(button_frame, text="ADD", fg_color="#FFA500", hover_color="#FF5900", 
                           width=140, height=37, text_color="black", font=ctk.CTkFont(size=20, weight="bold"), command=lambda: addGameUI())
    addBtn.pack(side="left", padx=10)

    editBtn = ctk.CTkButton(button_frame, text="EDIT", fg_color="#FFA500", hover_color="#FF5900", 
                            width=140, height=37, text_color="black", font=ctk.CTkFont(size=20, weight="bold"), command="")
    editBtn.pack(side="left", padx=10)

    deleteBtn = ctk.CTkButton(button_frame, text="DELETE", fg_color="#FFA500", hover_color="#FF5900", 
                              width=140, height=37, text_color="black", font=ctk.CTkFont(size=20, weight="bold"), command="")
    deleteBtn.pack(side="left", padx=10)
    
    backBtn = ctk.CTkButton(app, text="BACK", fg_color="#FFA500", hover_color="#FF5900", 
                              width=292, height=37, border_color="#2E2B2B", text_color="black", 
                              font=ctk.CTkFont(size=20, weight="bold"), command=lambda:adminPageUI())
    backBtn.pack(padx=5, pady=20, anchor="center")

def deletePageUI():
    # --------------DESIGN PÁGINA DELETE ---------------------
    #-----------------------------------------------------------------
    for widget in app.winfo_children():
        widget.destroy()

    main_frame = ctk.CTkFrame(app, width=1180, height=732, fg_color="#2E2B2B", corner_radius=0)
    main_frame.pack(fill="both", expand=True)

    dlt_msg_label1 = ctk.CTkLabel(main_frame, text="THIS ACTION WILL DELETE YOUR ACCOUNT", 
                              font=ctk.CTkFont(size=45, weight="bold"), text_color="#FFA500")
    dlt_msg_label1.place(relx=0.5, rely=0.3, anchor="center")

    dlt_msg_label2 = ctk.CTkLabel(main_frame, text="PERMANENTLY!", 
                                font=ctk.CTkFont(size=50, weight="bold"), text_color="#FF4500")
    dlt_msg_label2.place(relx=0.5, rely=0.4, anchor="center")

    dlt_msg_label3 = ctk.CTkLabel(main_frame, text="ARE YOU SURE?", 
                                font=ctk.CTkFont(size=70, weight="bold"), text_color="#FFA500")
    dlt_msg_label3.place(relx=0.5, rely=0.55, anchor="center")

    button_frame = ctk.CTkFrame(main_frame, fg_color="#2E2B2B")
    button_frame.place(relx=0.5, rely=0.75, anchor="center")

    noBtn = ctk.CTkButton(button_frame, text="NO, I STILL WANNA PLAY!", fg_color="#D9D9D9", hover_color="#5A5A5A", width=300, height=60, border_color="#2E2B2B", text_color="black", font=ctk.CTkFont(size=35, weight="bold"), command=lambda: settingsPageUI())
    noBtn.pack(side="left", padx=10)

    yesBtn = ctk.CTkButton(button_frame, text="YES, UNFORTUNATELY!", fg_color="#D9D9D9", hover_color="#5A5A5A", width=300, height=60, border_color="#2E2B2B", text_color="black", font=ctk.CTkFont(size=35, weight="bold"), command=lambda: goodbyeUI() )
    yesBtn.pack(side="left", padx=10)
    
def goodbyeUI():
    # --------------DESIGN GOODBYE ---------------------
    #-----------------------------------------------------------------
    
    for widget in app.winfo_children():
        widget.destroy()

    goodbye_frame = ctk.CTkFrame(app, width=1180, height=732, fg_color="black")
    goodbye_frame.place(relx=0.5, rely=0.5, anchor="center")

    imgIcon = ctk.CTkImage(Image.open("Images/Logo.png"), size=(450, 150))
    imgIcon_label = ctk.CTkLabel(app, image=imgIcon, text="")
    imgIcon_label.place(relx=0.5, rely=0.35, anchor="center")

    msg_welcome_label = ctk.CTkLabel(app, text="SEE YOU LATER!", font=ctk.CTkFont(size=24, weight="bold"), text_color="white")
    msg_welcome_label.place(relx=0.5, rely=0.50, anchor="center")

    loading_canvas = tk.Canvas(app, width=120, height=120, bg="black", bd=0, highlightthickness=0)
    loading_canvas.place(relx=0.5, rely=0.65, anchor="center")

    update_loading_circle(loading_canvas, 0)

    msg_loading_label = ctk.CTkLabel(app, text="LOADING...", font=ctk.CTkFont(size=24, weight="bold"), text_color="white")
    msg_loading_label.place(relx=0.5, rely=0.80, anchor="center")

    app.after(5000, loginUI)

# --------------ECRÃ INICIAL ---------------------
#-----------------------------------------------------------------
imgIcon = ctk.CTkImage(Image.open("Images/Logo.png"), size=(450, 150))
imgIcon_label = ctk.CTkLabel(app, image=imgIcon, text="")
imgIcon_label.place(relx=0.5, rely=0.35, anchor="center")

initial_msg_label = ctk.CTkLabel(app, text="WELCOME TO YOUR FAVORITE PLACE TO PLAY GAMES!",
                                  font=ctk.CTkFont(size=24, weight="bold"), text_color="white")
initial_msg_label.place(relx=0.5, rely=0.5, anchor="center")

button_frame = ctk.CTkFrame(app, width=480, height=85, fg_color="#202020", corner_radius=15)
button_frame.place(relx=0.5, rely=0.6, anchor="center")  

initialBtn = ctk.CTkButton(button_frame, text="CLICK HERE IF YOU’RE ON!", text_color="black", fg_color="#FFA500",
                           font=ctk.CTkFont(size=20, weight="bold"), hover_color="#FF5900",
                           command=lambda:loginUI(), width=480, height=85)
initialBtn.place(relx=0.5, rely=0.5, anchor="center") 

# ---------------FIM DA FUNÇÃO DA APP ---------------------
#-----------------------------------------------------------------
app.mainloop()