import customtkinter as ctk
from tkinter import messagebox, Toplevel
from PIL import Image, ImageTk
import PIL
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

# Inicializar janela principal
app = ctk.CTk()
app.title("GameON!")
app.geometry("1024x600")
app.configure(bg="#000000")

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

# Previsualização da aplicação

def previewPage():
    # Remover conteúdo atual do app
    for widget in app.winfo_children():
        widget.destroy()

    # Sidebar à esquerda
    sidebar = ctk.CTkFrame(app, width=300, height=600, corner_radius=0, fg_color="#1a1a1a")
    sidebar.pack(side=ctk.LEFT, fill=ctk.Y)

    imglogo = ctk.CTkImage(Image.open("Images/Logo.png"), size=(120, 44))
    imglogo_label = ctk.CTkLabel(sidebar, image=imglogo, text="", fg_color="#1a1a1a")
    imglogo_label.pack(padx=10, pady=20)

    registerBtn = ctk.CTkButton(sidebar, text="Registe Agora!", text_color="#ffffff", fg_color="#ff4500",
                               font=("Arial", 14), hover_color="#FF5900")
    registerBtn.pack(fill=ctk.X, pady=15, padx=10)

    storeBtn = ctk.CTkButton(sidebar, text="LOJA", text_color="#ffffff", fg_color="#383838",
                               font=("Arial", 12), hover_color="#505050", command=lambda: print("Loja"))
    storeBtn.pack(fill=ctk.X, pady=5, padx=10)

    discoverBtn = ctk.CTkButton(sidebar, text="DESCUBRA", text_color="#ffffff", fg_color="#383838",
                               font=("Arial", 12), hover_color="#505050", command=lambda: print("Descubra"))
    discoverBtn.pack(fill=ctk.X, pady=5, padx=10)

    loginBtn = ctk.CTkButton(sidebar, text="Entrar", text_color="white", fg_color="#ff4500",
                                     font=("Arial", 12), hover_color="#FF5900", command=lambda: print("entrar"))
    loginBtn.pack(side=ctk.BOTTOM, fill=ctk.X, pady=10, padx=10)

    # Main content
    main_content = ctk.CTkFrame(app, fg_color="#000000")
    main_content.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True)

    # Top bar
    top_bar = ctk.CTkFrame(main_content, height=100, fg_color="#1a1a1a", corner_radius=0)
    top_bar.pack(side=ctk.TOP, fill=ctk.X)

    discover_label = ctk.CTkLabel(top_bar, text="DISCOVER", text_color="white", font=("Arial", 14))
    discover_label.pack(side=ctk.LEFT, padx=20, pady=25)

    search_entry = ctk.CTkEntry(top_bar, placeholder_text="SEARCH...", font=("Arial", 12))
    search_entry.pack(side=ctk.RIGHT, padx=20, pady=10)

    # Discount Section

    imglogo = ctk.CTkImage(Image.open("Images/discount.png"), size=(885, 212))

    discount_frame = ctk.CTkButton(main_content, image=imglogo, text="", fg_color="#000000",
                                   hover_color="#000000", height=150, corner_radius=0)
    discount_frame.pack(fill=ctk.X, pady=20, padx=20)

    # Game Cards Section
    game_frame = ctk.CTkFrame(main_content, fg_color="#000000")
    game_frame.pack(fill=ctk.BOTH, expand=True, padx=20, pady=10)

    game_card = ctk.CTkButton(game_frame, fg_color="#cccccc", width=250, height=300)
    game_card.pack(side=ctk.LEFT)

    game_label = ctk.CTkLabel(game_card, text=f"GAME", text_color="#000000", font=("Arial", 12, "bold"))
    game_label.pack(pady=40)

    game_info = ctk.CTkLabel(game_card, text="Name game\nPrice", text_color="#000000", font=("Arial", 10))
    game_info.pack(side=ctk.BOTTOM, pady=10)

    favorite_icon = ctk.CTkLabel(game_card, text="\u2764", text_color="#000000", font=("Arial", 14))
    favorite_icon.pack(side=ctk.BOTTOM)


# Configurar grid para múltiplos frames
app.rowconfigure(0, weight=1)
app.columnconfigure(0, weight=1)

# Frames principais
loginFrame = ctk.CTkFrame(app, fg_color="#000000")
adminFrame = ctk.CTkFrame(app)
userFrame = ctk.CTkFrame(app)
registerFrame = ctk.CTkFrame(app)
loginFrame.pack(expand=True)

for frame in (loginFrame, adminFrame, userFrame, registerFrame):
    frame.grid(row=0, column=0, sticky="nsew")

# Variáveis globais
currentUser = ""
userLibrary = []

# --- Frame de Login ---

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


# Box (LabelFrame) dentro do Frame
box = ctk.CTkFrame(loginFrame, width=150, height=50, fg_color="#2e2b2b", corner_radius=5)
box.pack(expand=True, pady=50)

imglogo = ctk.CTkImage(Image.open("Images/Logo.png"), size=(200, 74))
imglogo_label = ctk.CTkLabel(box, image=imglogo, text="", fg_color="#2e2b2b")
imglogo_label.grid(padx=150, pady=15)

usernameEntry = ctk.CTkEntry(box, placeholder_text="Nome de utilizador", width=250)
usernameEntry.grid(padx=10, pady=10)

passwordEntry = ctk.CTkEntry(box, placeholder_text="Senha", show="*", width=250)
passwordEntry.grid(pady=10)

btnFrame = ctk.CTkFrame(box, width=100, height=5, fg_color="#2e2b2b", corner_radius=5)
btnFrame.grid(pady=10)

userButton = ctk.CTkButton(btnFrame, text="Entrar", command=loginAsUser, width=120, height=30, fg_color="#ffa500", text_color="#000000", hover_color="#FFB100")
userButton.grid(row=0, column=0, pady=5, padx=5)

registerButton = ctk.CTkButton(btnFrame, text="Registrar", command=goToRegister, width=120, height=30, fg_color="#ffa500", text_color="#000000", hover_color="#FFB100")
registerButton.grid(row=0, column=1, pady=5, padx=5)

previewBtn = ctk.CTkButton(box, text="Previsualização", command=previewPage, width=250, height=30, fg_color="#ffa500", text_color="#000000", hover_color="#FFB100")
previewBtn.grid(pady=(5,20))

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
