import customtkinter as ctk
from tkinter import messagebox, Toplevel
from PIL import Image, ImageTk
import os
import CTkMessagebox
import base64

# Configuração inicial de estilo
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Criar pasta de utilizadores, se não existir
if not os.path.exists("users"):
    os.makedirs("users")

def encodeBinary(data):
    return base64.b64encode(data.encode()).decode()

def decodeBinary(data):
    return base64.b64decode(data.encode()).decode()

# Função para alternar entre interfaces
def showFrame(frame):
    frame.tkraise()

# Função para carregar dados da "base de dados" (arquivo .txt)
def loadGames():
    games = []
    if os.path.exists("games.txt"):
        with open("games.txt", "r") as file:
            for line in file:
                name, description, image = line.strip().split("|")
                games.append({"name": name, "description": description, "image": image})
    return games

# Função para salvar dados da "base de dados" (arquivo .txt)
def saveGame(name, description, image):
    with open("games.txt", "a") as file:
        file.write(f"{name}|{description}|{image}\n")

# Função para carregar biblioteca do utilizador
def loadUserLibrary(username):
    library = []
    userFile = os.path.join("users", f"{username}_library.txt")
    if os.path.exists(userFile):
        with open(userFile, "r") as file:
            for line in file:
                decodedLine = decodeBinary(line.strip())
                name, description, image = decodedLine.split("|")
                library.append({"name": name, "description": description, "image": image})
    return library

# Função para salvar biblioteca do utilizador
def saveToUserLibrary(username, game):
    userFile = os.path.join("users", f"{username}_library.txt")
    with open(userFile, "a") as file:
        encodedLine = encodeBinary(f"{game['name']}|{game['description']}|{game['image']}")
        file.write(f"{encodedLine}\n")

# Função para adicionar jogo à biblioteca e salvar no arquivo do utilizador
def addToFavorites(game):
    if game not in userLibrary:
        userLibrary.append(game)
        saveToUserLibrary(currentUser, game)
        refreshUserLibrary()

# Função para exibir detalhes do jogo em uma janela modal
def showGameDetails(game):
    modal = Toplevel(app)
    modal.title(game["name"])
    modal.geometry("400x500")

    # Exibir imagem do jogo
    img = Image.open(game["image"])
    img = img.resize((200, 200))
    imgTk = ImageTk.PhotoImage(img)
    imgLabel = ctk.CTkLabel(modal, image=imgTk, text="")
    imgLabel.image = imgTk
    imgLabel.pack(pady=10)

    # Exibir nome e descrição
    nameLabel = ctk.CTkLabel(modal, text=game["name"], font=("Arial", 18))
    nameLabel.pack(pady=10)
    descriptionLabel = ctk.CTkLabel(modal, text=game["description"], wraplength=300, justify="left")
    descriptionLabel.pack(pady=10)

    # Botão para adicionar aos favoritos
    addFavoriteButton = ctk.CTkButton(modal, text="Adicionar à Biblioteca", command=lambda: [addToFavorites(game), modal.destroy()])
    addFavoriteButton.pack(pady=20)

# Inicializar janela principal
app = ctk.CTk()
app.title("Gestão de Jogos - Loja")
app.geometry("800x600")

# Configurar grid para múltiplos frames
app.rowconfigure(0, weight=1)
app.columnconfigure(0, weight=1)

# Frames principais
loginFrame = ctk.CTkFrame(app)
adminFrame = ctk.CTkFrame(app)
userFrame = ctk.CTkFrame(app)
registerFrame = ctk.CTkFrame(app)

for frame in (loginFrame, adminFrame, userFrame, registerFrame):
    frame.grid(row=0, column=0, sticky="nsew")

# Variáveis globais
currentUser = ""
userLibrary = []

# --- Frame de Login ---
loginLabel = ctk.CTkLabel(loginFrame, text="Bem-vindo! Escolha seu perfil:", font=("Arial", 24))
loginLabel.pack(pady=40)

def loginAsUser():
    global currentUser, userLibrary
    username = usernameEntry.get().strip()
    password = passwordEntry.get().strip()
    if username and password:
        userFile = os.path.join("users", f"{username}.txt")
        if os.path.exists(userFile):
            with open(userFile, "r") as file:
                savedPassword = decodeBinary(file.readline().strip())
                if savedPassword == password:
                    currentUser = username
                    userLibrary = loadUserLibrary(username)
                    refreshUserLibrary()
                    showFrame(userFrame)
                else:
                    messagebox.showerror("Erro", "Senha incorreta!")
        else:
            messagebox.showerror("Erro", "utilizador não encontrado!")
    else:
        messagebox.showwarning("Aviso", "Preencha todos os campos!")

def goToRegister():
    showFrame(registerFrame)

usernameEntry = ctk.CTkEntry(loginFrame, placeholder_text="Nome de utilizador")
usernameEntry.pack(pady=10)

passwordEntry = ctk.CTkEntry(loginFrame, placeholder_text="Senha", show="*")
passwordEntry.pack(pady=10)

userButton = ctk.CTkButton(loginFrame, text="Login", command=loginAsUser, width=250, height=50)
userButton.pack(pady=20)

registerButton = ctk.CTkButton(loginFrame, text="Registrar-se", command=goToRegister, width=250, height=50)
registerButton.pack(pady=20)

# --- Frame de Registro ---
registerLabel = ctk.CTkLabel(registerFrame, text="Registrar Novo utilizador", font=("Arial", 24))
registerLabel.pack(pady=20)

def registerUser():
    newUsername = newUsernameEntry.get().strip()
    newPassword = newPasswordEntry.get().strip()
    if newUsername and newPassword:
        userFile = os.path.join("users", f"{newUsername}.txt")
        if not os.path.exists(userFile):
            with open(userFile, "w") as file:
                file.write(f"{encodeBinary(newPassword)}\n")
            messagebox.showinfo("Sucesso", "utilizador registrado com sucesso!")
            showFrame(loginFrame)
        else:
            messagebox.showwarning("Aviso", "utilizador já existe!")
    else:
        messagebox.showwarning("Aviso", "Preencha todos os campos!")

newUsernameEntry = ctk.CTkEntry(registerFrame, placeholder_text="Novo Nome de utilizador")
newUsernameEntry.pack(pady=10)

newPasswordEntry = ctk.CTkEntry(registerFrame, placeholder_text="Senha", show="*")
newPasswordEntry.pack(pady=10)

registerConfirmButton = ctk.CTkButton(registerFrame, text="Registrar", command=registerUser, width=250, height=50)
registerConfirmButton.pack(pady=20)

registerBackButton = ctk.CTkButton(registerFrame, text="Voltar", command=lambda: showFrame(loginFrame), width=250, height=50)
registerBackButton.pack(pady=20)

# --- Frame Admin ---
adminLabel = ctk.CTkLabel(adminFrame, text="Painel do Admin", font=("Arial", 24))
adminLabel.pack(pady=20)

# Menu lateral
adminSidebar = ctk.CTkFrame(adminFrame, width=200, height=600, corner_radius=0)
adminSidebar.pack(side="left", fill="y")
adminSidebarLabel = ctk.CTkLabel(adminSidebar, text="Menu Admin", font=("Arial", 18))
adminSidebarLabel.pack(pady=20)

# Adicionar novo jogo
adminContentFrame = ctk.CTkFrame(adminFrame, corner_radius=10)
adminContentFrame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

def addGame():
    name = nameEntry.get()
    description = descriptionText.get("1.0", "end").strip()
    image = imageEntry.get()
    if name and description and image:
        saveGame(name, description, image)
        nameEntry.delete(0, "end")
        descriptionText.delete("1.0", "end")
        imageEntry.delete(0, "end")
        messagebox.showinfo("Sucesso", "Jogo adicionado à Biblioteca!")
    else:
        messagebox.showwarning("Aviso", "Preencha todos os campos!")

nameEntry = ctk.CTkEntry(adminContentFrame, placeholder_text="Nome do jogo")
nameEntry.pack(pady=10)

descriptionText = ctk.CTkTextbox(adminContentFrame, height=100)
descriptionText.insert("1.0", "Descrição do jogo")
descriptionText.pack(pady=10)

imageEntry = ctk.CTkEntry(adminContentFrame, placeholder_text="Caminho da imagem")
imageEntry.pack(pady=10)

addGameButton = ctk.CTkButton(adminContentFrame, text="Adicionar Jogo", command=addGame)
addGameButton.pack(pady=20)

# Voltar ao login
adminBackButton = ctk.CTkButton(adminSidebar, text="Logout", command=lambda: showFrame(loginFrame))
adminBackButton.pack(side="bottom", pady=20)

# --- Frame User ---
userLabel = ctk.CTkLabel(userFrame, text="Loja de Jogos", font=("Arial", 24))
userLabel.pack(pady=20)

# Menu lateral do utilizador
userSidebar = ctk.CTkFrame(userFrame, width=200, height=600, corner_radius=0)
userSidebar.pack(side="left", fill="y")
userSidebarLabel = ctk.CTkLabel(userSidebar, text="Menu", font=("Arial", 18))
userSidebarLabel.pack(pady=20)

# Biblioteca de jogos
userContentFrame = ctk.CTkFrame(userFrame, corner_radius=10)
userContentFrame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

libraryLabel = ctk.CTkLabel(userContentFrame, text="Biblioteca", font=("Arial", 18))
libraryLabel.pack(pady=10)

libraryFrame = ctk.CTkFrame(userContentFrame)
libraryFrame.pack(pady=10, fill="both", expand=True)

def refreshUserLibrary():
    for widget in libraryFrame.winfo_children():
        widget.destroy()
    for game in userLibrary:
        gameButton = ctk.CTkButton(libraryFrame, text=game["name"], command=lambda g=game: showGameDetails(g))
        gameButton.pack(pady=5)

refreshUserLibrary()

# Voltar ao login
userBackButton = ctk.CTkButton(userSidebar, text="Logout", command=lambda: showFrame(loginFrame))
userBackButton.pack(side="bottom", pady=20)

# Mostrar o frame de login inicialmente
showFrame(loginFrame)

# Executar a aplicação
app.mainloop()
