# ---------------BIBLIOTECAS ---------------------
#-----------------------------------------------------------------
import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox, ttk, Canvas
import os
import datetime
from PIL import Image, ImageDraw
import readFiles 
import re

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
    app.resizable(False, False)

app = ctk.CTk()
app.configure(fg_color="black")  
app.iconbitmap("Images/1-f8c98aa8.ico")
renderWindow(1180, 732, "GameON!")

# ---------------FUNCOES ---------------------
# -----------------------------------------------------------------

def filterGames(search_text):
    """
    Função que filtra os jogos com base no texto de pesquisa.
    """
    # Limpa todos os widgets antes de adicionar os resultados
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
    
    store_label = ctk.CTkLabel(topbar, text="SEARCH", text_color="white", font=("Arial", 18))
    store_label.pack(side=ctk.LEFT, padx=35)

    profile_circle = ctk.CTkButton(topbar, width=50, height=50, corner_radius=25,  fg_color="#FFA500",
                                   text="", hover_color="#FF5900", command=lambda:settingsPageUI())
    profile_circle.pack(side=ctk.RIGHT, padx=(0, 15), pady=30)

    search_entry = ctk.CTkEntry(topbar, placeholder_text="Search...", font=("Arial", 16), width=300)
    search_entry.pack(side=ctk.RIGHT, padx=20, pady=50) 

    search_btn = ctk.CTkButton(topbar, text="\u2315", text_color="white", fg_color="#FF5900", font=("Arial", 16), hover_color="#FF4500", width=30, height=30, command=lambda: filterGames(search_entry.get()))
    search_btn.pack(side=ctk.RIGHT, pady=30)

    game_frame = ctk.CTkScrollableFrame(app, fg_color="#101010")
    game_frame.pack(fill="both", expand=True, pady=100)

    # Cria a expressão regular para pesquisa
    search_pattern = re.compile(search_text, re.IGNORECASE)  # Ignora maiúsculas/minúsculas

    # Recarrega a lista de jogos
    gamesList = readFiles.lerFicheiroJogos()

    max_games_per_row = 3 
    current_row = 0
    current_column = 0
    row_frame = None

    for i, line in enumerate(gamesList):
        game = line.split(";")
        
        # Verifica se o nome ou o gênero do jogo corresponde ao texto de pesquisa
        if search_pattern.search(game[0]) or search_pattern.search(game[1]):
            game_image = ctk.CTkImage(Image.open(game[3].strip()), size=(200, 300))

            if current_column == 0:
                row_frame = ctk.CTkFrame(game_frame, fg_color="#101010")
                row_frame.pack(side="top", fill="x", padx=10, pady=10)

            game_item_frame = ctk.CTkFrame(row_frame, fg_color="#101010", width=200, height=340)
            game_item_frame.pack(side="left", padx=10, pady=20)

            game_button = ctk.CTkButton(
                game_item_frame,
                image=game_image,
                text="",
                fg_color="#101010",
                width=200,
                height=300,
                command=lambda g=game: gameAspect(g[0], g[1], g[2], g[3].strip())
            )
            game_button.pack()

            gameTxt = ctk.CTkLabel(
                game_item_frame,
                text=game[0],
                text_color="white",
                font=("Arial", 18)
            )
            gameTxt.pack(pady=5)

            current_column += 1
            if current_column >= max_games_per_row:
                current_column = 0

def refreshTreeviewGame(treeview):
    """
    Função que atualiza a Treeview com os jogos restantes após a exclusão
    """
    # Limpa todos os itens da Treeview
    for item in treeview.get_children():
        treeview.delete(item)
    
    # Recarrega os jogos restantes
    listaJogos = readFiles.lerFicheiroJogos()  # Função para ler o arquivo de jogos
    for linha in listaJogos:
        jogo = linha.split(";")
        treeview.insert("", "end", values=(jogo[0], jogo[1], jogo[2]))  # Adiciona novamente os jogos na Treeview

def addNotification(nomeJogo, genero):
    """
    Função que adiciona uma notificação ao ficheiro notificacoes.txt
    """
    dataCriacao = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    file = open("files/notificacoes.txt", "a", encoding="utf-8")
    file.write(f"{nomeJogo};{genero};{dataCriacao}\n")
    file.close()

def verificarGeneroJogosFavoritos(genero):
    """
    Função que verifica se o jogo adicionado à lista de jogos é do mesmo gênero que um dos jogos favoritos do utilizador.
    """
    listaJogosFavoritos = readFiles.lerFicheiroJogosFavoritos()
    for linha in listaJogosFavoritos:
        jogo = linha.strip().split(";")
        if len(jogo) >= 3 and jogo[0] == currentUser and jogo[2] == genero:
            return True
    return False

def verificarDataUltimoLogout(dataCriacao):
    """
    Função que verifica se a data do último logout é inferior à data de criação da notificação.
    """
    listaUsers = readFiles.lerFicheiroUsers()
    for linha in listaUsers:
        user = linha.strip().split(";")
        if len(user) >= 4 and user[0] == currentUser:
            dataUltimoLogout = user[3]
            try:
                dataUltimoLogout = datetime.datetime.strptime(dataUltimoLogout, "%Y-%m-%d %H:%M:%S")
                dataCriacao = datetime.datetime.strptime(dataCriacao, "%Y-%m-%d %H:%M:%S")
                return dataUltimoLogout < dataCriacao
            except ValueError:
                print(f"Erro ao converter datas: {dataUltimoLogout} ou {dataCriacao}")
                return False
    return False

def deleteNotification(nomeJogo):
    """
    Função que apaga uma notificação do ficheiro notificacoes.txt
    """
    listaNotificacoes = readFiles.lerFicheiroNotificacoes()
    for linha in listaNotificacoes:
        notificacao = linha.split(";")
        if notificacao[0] == nomeJogo:
            listaNotificacoes.remove(linha)
    file = open("files/notificacoes.txt", "w", encoding="utf-8")
    file.writelines(listaNotificacoes)
    file.close()

def addComment(game,comment,user,rating):
    """
    Função que adiciona um comentário ao ficheiro comentarios.txt
    """
    file = open("files/comentarios.txt", "a", encoding="utf-8")
    file.write(f"{game};{user};{rating};{comment}\n")
    file.close()

def showComments(game):
    """
    Função que mostra os comentários de um jogo dentro de uma frame na interface gráfica
    """
    listaComentarios = readFiles.lerFicheiroComentarios()
    for linha in listaComentarios:
        comentario = linha.split(";")
        if comentario[0] == game:
            comment_frame = ctk.CTkFrame(app, width=948, height=128, corner_radius=0, bg_color="#101010")
            comment_frame.pack(side=ctk.TOP, fill=ctk.X)
            comment_label = ctk.CTkLabel(comment_frame, text=f"User: {comentario[2]}\nRating: {comentario[3]}\nComment: {comentario[1]}", text_color="white", font=("Arial", 12))
            comment_label.pack(side=ctk.LEFT, padx=35, pady=50)
    return comment_frame

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
        file.write(f"{nomeJogo};{genero};{descricao.strip("\n")};{imagePath}\n")
        file.close()
        messagebox.showinfo("Success", "Game added successfully!")
        
def deleteGame(treeview):
    """
    Função que apaga um jogo da lista de jogos
    """
    selected_item = treeview.selection()  # Pega o item selecionado na Treeview
    if not selected_item:  # Verifica se há algum item selecionado
        messagebox.showerror("Error", "Please select a game to delete!")
        return
    
    # Obtém o nome do jogo da primeira coluna do item selecionado
    nomeJogo = treeview.item(selected_item)["values"][0]
    
    if nomeJogo == "":  # Verifica se o nome do jogo está vazio
        messagebox.showerror("Error", "Please fill in all fields!")
    else:
        deleteNotification(nomeJogo)  # Supondo que você tenha essa função definida
        listaJogos = readFiles.lerFicheiroJogos()  # Função para ler o arquivo de jogos
        for linha in listaJogos:
            jogo = linha.split(";")
            if jogo[0] == nomeJogo:
                listaJogos.remove(linha)  # Remove o jogo da lista

                # Apaga a imagem do jogo
                image_path = jogo[3].strip()  # Supondo que a imagem esteja na 4ª coluna
                if os.path.exists(image_path):
                    os.remove(image_path)  # Apaga o arquivo de imagem
                else:
                    print(f"Imagem não encontrada: {image_path}")

                # Reabre o arquivo e escreve a lista de jogos atualizada
                file = open("files/jogos.txt", "w", encoding="utf-8")
                file.writelines(listaJogos)
                file.close()
                messagebox.showinfo("Success", "Game deleted successfully!")
                break
        else:
            messagebox.showerror("Error", "Game not found!")
    refreshTreeviewGame(treeview)

def removeGameFav(gameName):
    """
    Função que remove um jogo dos favoritos do utilizador
    """
    lFavGames = readFiles.lerFicheiroJogosFavoritos()
    updated_fav_games = []

    # Procura o jogo nos favoritos e remove-o
    game_found = False
    for line in lFavGames:
        favGame = line.strip().split(";")
        if len(favGame) >= 2 and favGame[1] == gameName and favGame[0] == currentUser:
            game_found = True  # Marca que o jogo foi encontrado
        else:
            updated_fav_games.append(line)  # Mantém o jogo na lista se não for o jogo a ser removido

    if not game_found:
        messagebox.showerror("Error", "Game not found in your favorites")
        return

    # Reescreve o arquivo com a lista atualizada de favoritos
    file = open("files/jogosFavoritos.txt", "w", encoding="utf-8")
    file.writelines(updated_fav_games)
    file.close()

    messagebox.showinfo("Success", "Game removed from your library successfully!")

def addGameFav(gameName, gameGenre):
    """
    Função que adiciona um jogo aos favoritos do utilizador
    """
    lFavGames = readFiles.lerFicheiroJogosFavoritos()
    
    for line in lFavGames:
        favGame = line.strip().split(";") 
        if len(favGame) >= 2 and favGame[1] == gameName and favGame[0] == currentUser:
            messagebox.showerror("Error", "You already have this game in your library")
            return

    # Se o jogo não estiver nos favoritos, adiciona-o
    file = open("files/jogosFavoritos.txt", "a", encoding="utf-8")
    file.write(f"{currentUser};{gameName};{gameGenre}\n")
    file.close()
    
    messagebox.showinfo("Success", "Game added to your library successfully!")

def addComentario(nomeJogo, rating, comentario):
    """
    Função que adiciona um comentário a um jogo
    """
    if nomeJogo == "" or comentario == "":
        messagebox.showerror("Error", "Please fill in all fields!")
    else:
        file = open("files/comentarios.txt", "a", encoding="utf-8")
        file.write(f"{nomeJogo};{currentUser};{rating};{comentario.strip()}\n")
        file.close()
        messagebox.showinfo("Success", "Comment added successfully!")

def addUser( username, password, permLevel):
    """
    Função que adiciona um utilizador à lista de utilizadores
    """

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
                file = open("files/users.txt", "a", encoding="utf-8")
                file.write(f"{username};{password};{permLevel};a;\n")
                file.close()
                messagebox.showinfo("Success", "User added successfully!")
                return

def deleteUser(treeview):
    """
    Função que apaga um utilizador da lista de utilizadores e sua imagem
    e faz refresh na Treeview
    """
    username = treeview.item(treeview.selection())["values"][0]
    
    if username == "":
        messagebox.showerror("Error", "Please select a user to delete!")
        return
    
    listaUsers = readFiles.lerFicheiroUsers() 
    for linha in listaUsers:
        user = linha.split(";")
        
        if user[0] == username:
            if len(user) == 5:
                listaUsers.remove(linha) 
                image_path = user[4].strip()
                file = open("files/users.txt", "w", encoding="utf-8")
                file.writelines(listaUsers)
                file.close()
                if os.path.exists(image_path):
                    os.remove(image_path)  
                else:
                    print(f"Imagem não encontrada: {image_path}")
            else:
                listaUsers.remove(linha)
                file = open("files/users.txt", "w", encoding="utf-8")
                file.writelines(listaUsers)
                file.close()
            
            
            
            # Atualiza a Treeview para refletir a remoção
            refreshTreeviewUser(treeview)
            
            messagebox.showinfo("Success", "User deleted successfully!")
            return
    
    messagebox.showerror("Error", "User not found!")  # Caso o utilizador não seja encontrado

def refreshTreeviewUser(treeview):
    """
    Função que atualiza a Treeview com a lista atualizada de utilizadores
    """
    # Limpa todos os itens da Treeview
    for item in treeview.get_children():
        treeview.delete(item)
    
    # Repopula a Treeview com a lista de utilizadores atualizada
    lUsers = readFiles.lerFicheiroUsers()
    for line in lUsers:
        user = line.split(";")
        if user[2] != "2":
            treeview.insert('', 'end', values=(user[0].strip(), "User"))
        else:
            continue

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
            file.write(f"{username};{password};1;a;\n")
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
                    file.write(f"{username};{password};1;a;\n")
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

def userLogout():
    """
    Função que faz logout do utilizador
    """
    listaUsers = readFiles.lerFicheiroUsers()
    for index, linha in enumerate(listaUsers):
        user = linha.split(";")
        if user[0] == currentUser:
            user[3] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            

            listaUsers[index] = ";".join(user) + "\n" 

            file = open(".\\files\\users.txt", "w", encoding="utf-8")
            file.writelines(listaUsers)
            file.close()

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
                                           filetypes=(("PNG Images", "*.png"), ("JPG Images", "*.jpg"),("JPEG Images","*.jpeg")))
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

    search_btn = ctk.CTkButton(topbar, text="\u2315", text_color="white", fg_color="#FF5900", font=("Arial", 16), hover_color="#FF4500", width=30, height=30, command=lambda: filterGames(search_entry.get()))
    search_btn.pack(side=ctk.RIGHT, pady=30)

    game_frame = ctk.CTkScrollableFrame(app, fg_color="#101010")
    game_frame.pack(fill="both", expand=True, pady=100)

    gamesList = readFiles.lerFicheiroJogos()

    max_games_per_row = 3 
    current_row = 0
    current_column = 0
    row_frame = None

    for i, line in enumerate(gamesList):
        game = line.split(";")
        game_image = ctk.CTkImage(Image.open(game[3].strip()), size=(200, 300))

        if current_column == 0:
            row_frame = ctk.CTkFrame(game_frame, fg_color="#101010")
            row_frame.pack(side="top", fill="x", padx=10, pady=10)

        game_item_frame = ctk.CTkFrame(row_frame, fg_color="#101010", width=200, height=340)
        game_item_frame.pack(side="left", padx=10, pady=20)

        game_button = ctk.CTkButton(
            game_item_frame,
            image=game_image,
            text="",
            fg_color="#101010",
            width=200,
            height=300,
            command=lambda g=game: gameAspect(g[0], g[1], g[2], g[3].strip())
        )
        game_button.pack()

        gameTxt = ctk.CTkLabel(
            game_item_frame,
            text=game[0],
            text_color="white",
            font=("Arial", 18)
        )
        gameTxt.pack(pady=5)

        current_column += 1
        if current_column >= max_games_per_row:
            current_column = 0

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

    search_btn = ctk.CTkButton(topbar, text="\u2315", text_color="white", fg_color="#FF5900", font=("Arial", 16), hover_color="#FF4500", width=30, height=30, command=lambda: filterGames(search_entry.get()))
    search_btn.pack(side=ctk.RIGHT, pady=30)
    
    game_frame = ctk.CTkScrollableFrame(app, fg_color="#101010")
    game_frame.pack(fill="both", expand=True, pady=100)

    lFavGames = readFiles.lerFicheiroJogosFavoritos()

    max_games_per_row = 4  

    current_row = 0
    current_column = 0

    row_frame = None

    for line in lFavGames:
        gameFav = line.split(";")
        if currentUser == gameFav[0]:
            lGames = readFiles.lerFicheiroJogos()
            for line2 in lGames:
                game = line2.split(";")
                if game[0] == gameFav[1]:

                    game_image = ctk.CTkImage(Image.open(game[3].strip()), size=(200, 300))

                    if current_column == 0:
                        row_frame = ctk.CTkFrame(game_frame, fg_color="#101010")
                        row_frame.pack(side="top", fill="x", padx=10, pady=10)

                    game_item_frame = ctk.CTkFrame(row_frame, fg_color="#101010", width=200, height=340)
                    game_item_frame.pack(side="left", padx=10, pady=20)

                    game_button = ctk.CTkButton(
                        game_item_frame,
                        image=game_image,
                        text="",
                        fg_color="#101010",
                        width=200,
                        height=300,
                        command=lambda g=game: gameAspect(g[0], g[1], g[2], g[3].strip())
                    )
                    game_button.pack()

                    gameTxt = ctk.CTkLabel(
                        game_item_frame,
                        text=game[0],
                        text_color="white",
                        font=("Arial", 18)
                    )
                    gameTxt.pack(pady=5)

                    current_column += 1

                    if current_column >= max_games_per_row:
                        current_column = 0

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

    # Ler dados dos ficheiros
    total_users = len(readFiles.lerFicheiroUsers())  # Quantidade total de usuários
    total_games = len(readFiles.lerFicheiroJogos())  # Quantidade total de jogos
    jogos_fav_data = readFiles.lerFicheiroJogosFavoritos()  # Dados dos jogos favoritados

    # Criar lista de jogos mais favoritados
    jogos_fav_count = {}
    for jogo in jogos_fav_data:
        if jogo in jogos_fav_count:
            jogos_fav_count[jogo] += 1
        else:
            jogos_fav_count[jogo] = 1

    # Ordenar jogos pelo número de favoritos (maior para menor) e pegar o top 5
    top_games = sorted(jogos_fav_count.items(), key=lambda x: x[1], reverse=True)[:5]

    label_frame = ctk.CTkFrame(app, fg_color="black")
    label_frame.pack(pady=(50, 0), anchor="center")

    totalUsers_label = ctk.CTkLabel(label_frame, text=f"TOTAL USERS: {total_users}", text_color="white", font=("Arial", 18))
    totalUsers_label.pack(side="left", padx=(0,50), anchor="center")

    totalGames_label = ctk.CTkLabel(label_frame, text=f"TOTAL GAMES: {total_games}", text_color="white", font=("Arial", 18))
    totalGames_label.pack(side="left", padx=50, anchor="center")

    def graphFunc():
        canvas.delete("all")  

        bar_width = 80  
        spacing = 50  
        max_value = max([value for _, value in top_games]) if top_games else 1  

        for i, (game, favorites) in enumerate(top_games):
            x1 = i * (bar_width + spacing) + 50  
            y1 = 300  
            x2 = x1 + bar_width  
            y2 = y1 - int((favorites / max_value) * 250)  

            # Desenhar barra
            canvas.create_rectangle(x1, y1, x2, y2, fill="orange")
            
            # Nome do jogo DENTRO da barra (ou ajustar se necessário)
            canvas.create_text(
                x1 + bar_width / 2,  # Posição X (centro da barra)
                (y1 + y2) / 2,      # Posição Y (meio da barra)
                text=game,           # Nome do jogo
                fill="black",        # Cor do texto (muda para preto para melhor contraste)
                font=("Arial", 10, "bold")
            )
            
            # Quantidade de favoritos acima da barra
            canvas.create_text(
                x1 + bar_width / 2,  # Posição X (centro da barra)
                y2 - 10,             # Posição Y (acima da barra)
                text=str(favorites), # Texto com o número de favoritos
                fill="white", 
                font=("Arial", 10, "bold")
            )

          

    canvas = tk.Canvas(app, width=600, height=300, bg="black", highlightthickness=0)
    canvas.pack(pady=20)

    draw_button = ctk.CTkButton(app, text="DRAW GRAPH", fg_color="#FFA500", hover_color="#FF5900", width=140, height=37, 
                                border_color="#2E2B2B", text_color="black", font=ctk.CTkFont(size=20, weight="bold"), command=lambda:graphFunc())
    draw_button.pack()

def gameAspect(gameName, gameGenre, gameDescription, gameImage):
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

    search_btn = ctk.CTkButton(topbar, text="\u2315", text_color="white", fg_color="#FF5900", font=("Arial", 16), hover_color="#FF4500", width=30, height=30, command=lambda: filterGames(search_entry.get()))
    search_btn.pack(side=ctk.RIGHT, pady=30)

    backBtn = ctk.CTkButton(app, text="BACK", fg_color="#FFA500", hover_color="#FF5900",
                                width=292, height=37, border_color="#2E2B2B", text_color="black", 
                                font=ctk.CTkFont(size=20, weight="bold"), command=lambda:storePageUI())
    backBtn.place(x=350, y=150)
    
    imgGame = ctk.CTkImage(Image.open(gameImage), size=(200, 300))
    imgGame_label = ctk.CTkLabel(app, image=imgGame, text="", fg_color="#2E2B2B")
    imgGame_label.place(x=350, y=200)

    nameGame_label = ctk.CTkLabel(app, text=gameName, text_color="white", font=("Arial", 18))
    nameGame_label.place(x=580, y=220)

    gameDescriptionBox = ctk.CTkTextbox(app, width=480, height=180, fg_color="white", font=("Arial", 12), text_color="black", state="normal")
    gameDescriptionBox.place(x=350, y=520)

    gameDescriptionBox.insert("1.0", gameDescription)
    gameDescriptionBox.configure(state="disabled")

    # Verifica se o jogo já está nos favoritos do utilizador
    lFavGames = readFiles.lerFicheiroJogosFavoritos()
    game_in_fav = False
    for line in lFavGames:
        favGame = line.strip().split(";")
        if favGame[0] == currentUser and favGame[1] == gameName:
            game_in_fav = True
            break

    # Se o jogo já está nos favoritos, mostra o botão "Remove", caso contrário, mostra o botão "Save"
    if game_in_fav:
        removeBtn = ctk.CTkButton(app, text="REMOVE", fg_color="#FF4500", hover_color="#FF5900", width=140, height=37,
                            border_color="black", text_color="black", font=ctk.CTkFont(size=20, weight="bold"), command=lambda: removeGameFav(gameName))
        removeBtn.place(x=580, y=260)
    else:
        saveBtn = ctk.CTkButton(app, text="SAVE", fg_color="#FFA500", hover_color="#FF5900", width=140, height=37,
                            border_color="black", text_color="black", font=ctk.CTkFont(size=20, weight="bold"), command=lambda: addGameFav(gameName, gameGenre))
        saveBtn.place(x=580, y=260)

    comment_frame = ctk.CTkFrame(app, fg_color="#101010", width=300, height=520, corner_radius=10)
    comment_frame.place(x=860, y=150)

    listaComentarios = readFiles.lerFicheiroComentarios()

    if listaComentarios:  # Apenas processa se a lista não estiver vazia
        for linha in listaComentarios:
            comentario = linha.strip().split(";")  # Remove espaços extras e quebra linhas
            if len(comentario) >= 4 and comentario[0] == gameName:  # Verifica se há campos suficientes e se o jogo corresponde
                comment_label = ctk.CTkLabel(
                    comment_frame, 
                    text=f"User: {comentario[1]}\t\tRating: {comentario[2]}/5\nComment: {comentario[3]}", 
                    text_color="white", 
                    font=("Arial", 12),
                    wraplength=280  # Limita o comprimento do texto
                )
                comment_label.pack(anchor="w", padx=10, pady=10)  # Alinha à esquerda e adiciona espaçamento
    else:
        # Mensagem padrão se não houver comentários
        empty_label = ctk.CTkLabel(
            comment_frame, 
            text="No comments available.", 
            text_color="white", 
            font=("Arial", 12)
        )
        empty_label.pack(anchor="center", pady=20)

    createCommentBtn = ctk.CTkButton(app, text="CREATE A COMMENT", fg_color="#FFA500", hover_color="#FF5900",
                            width=300, height=37, border_color="#2E2B2B", text_color="black", 
                            font=ctk.CTkFont(size=20, weight="bold"), command=lambda:commentsPage(gameName))
    createCommentBtn.place(x=860, y=680)

def commentsPage(gameName):
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

    search_btn = ctk.CTkButton(topbar, text="\u2315", text_color="white", fg_color="#FF5900", font=("Arial", 16), hover_color="#FF4500", width=30, height=30, command=lambda: filterGames(search_entry.get()))
    search_btn.pack(side=ctk.RIGHT, pady=30)

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
                            font=ctk.CTkFont(size=20, weight="bold"), command=lambda:addComentario(gameName,rating.get(),commentTxt.get("1.0", "end")))
    commentBtn.place(x=580, y=600)

    backBtn = ctk.CTkButton(app, text="BACK", fg_color="#FFA500", hover_color="#FF5900",
                            width=292, height=37, border_color="#2E2B2B", text_color="black", 
                            font=ctk.CTkFont(size=20, weight="bold"), command=lambda:storePageUI())
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

    listaNotificacoes = readFiles.lerFicheiroNotificacoes()
    for linha in listaNotificacoes:
        notificacao = linha.strip().split(";")
        if len(notificacao) >= 3:  # Verifica se há pelo menos 3 campos
            nome_jogo, genero, data_criacao = notificacao[0], notificacao[1], notificacao[2]
            print(verificarDataUltimoLogout(data_criacao))
            print(verificarGeneroJogosFavoritos(genero))
            if verificarGeneroJogosFavoritos(genero) and verificarDataUltimoLogout(data_criacao):
                notification_text = f"Game: {nome_jogo}\nGenre: {genero}"
                notifications_label = ctk.CTkLabel(
                    notification_frame,
                    text=notification_text,
                    text_color="black",
                    font=("Arial", 14),
                    fg_color="#101010",
                    width=300,
                    height=100,
                    anchor="w"
                )
                notifications_label.pack(pady=10, padx=20)
        else:
            print(f"Linha inválida ignorada: {linha}")

    msgSettings_frame= ctk.CTkFrame (app, width=600, height=52, corner_radius=10, fg_color="#FFA500")
    msgSettings_frame.place(x=370, y=580)

    msgSettings_label = ctk.CTkLabel(msgSettings_frame, text="YOU'RE A PRO PLAYER, DON'T GIVE UP", text_color="black", font=("Arial", 22, "bold"))
    msgSettings_label.place(relx=0.5, rely=0.5, anchor="center")

    logoutBtn = ctk.CTkButton(app, text="LOGOUT", text_color="white", fg_color="#FF5900", font=("Arial", 22, "bold"), hover_color="#FF4500", width=191, height=52, command=lambda:userLogout())
    logoutBtn.place(x=980, y=580)

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
                                filetypes=(("PNG Images", "*.png"),("JPG Images", "*.jpg"),("JPEG Images","*.jpeg")))
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
                                border_color="black", text_color="black",font=ctk.CTkFont(size=20, weight="bold"), command=lambda:addUser(addUsername_entry.get(),addPassword_entry.get(),radio_value.get()))
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

    lUsers = readFiles.lerFicheiroUsers()
    for line in lUsers:
        user = line.strip().split(";")
        if len(user) >= 4:
            if user[2] != "2":
                tree.insert('', 'end', values=(user[0].strip(), "User"))
        else:
            print(f"Linha inválida encontrada e ignorada: {line}")

    button_frame = ctk.CTkFrame(app, fg_color="black")
    button_frame.pack(pady=(20, 0), anchor="center")

    addBtn = ctk.CTkButton(button_frame, text="ADD", fg_color="#FFA500", hover_color="#FF5900", 
                           width=140, height=37, text_color="black", font=ctk.CTkFont(size=20, weight="bold"), command=lambda: addUserUI())
    addBtn.pack(side="left", padx=10)

    deleteBtn = ctk.CTkButton(button_frame, text="DELETE", fg_color="#FFA500", hover_color="#FF5900", 
                              width=140, height=37, text_color="black", font=ctk.CTkFont(size=20, weight="bold"), command=lambda: deleteUser(tree))
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

    lGames = readFiles.lerFicheiroJogos()
    for line in lGames:
        game = line.split(";")
        tree.insert('', 'end', values=(game[0].strip(), game[1].strip()))

    button_frame = ctk.CTkFrame(app, fg_color="black")
    button_frame.pack(pady=(20, 0), anchor="center")

    addBtn = ctk.CTkButton(button_frame, text="ADD", fg_color="#FFA500", hover_color="#FF5900", 
                           width=140, height=37, text_color="black", font=ctk.CTkFont(size=20, weight="bold"), command=lambda: addGameUI())
    addBtn.pack(side="left", padx=10)

    deleteBtn = ctk.CTkButton(button_frame, text="DELETE", fg_color="#FFA500", hover_color="#FF5900", 
                              width=140, height=37, text_color="black", font=ctk.CTkFont(size=20, weight="bold"), command=lambda:deleteGame(tree))
    deleteBtn.pack(side="left", padx=10)
    
    backBtn = ctk.CTkButton(app, text="BACK", fg_color="#FFA500", hover_color="#FF5900", 
                              width=292, height=37, border_color="#2E2B2B", text_color="black", 
                              font=ctk.CTkFont(size=20, weight="bold"), command=lambda:adminPageUI())
    backBtn.pack(padx=5, pady=20, anchor="center")

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
userLogout()