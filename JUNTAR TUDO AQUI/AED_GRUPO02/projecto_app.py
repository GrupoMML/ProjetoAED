# ---------------BIBLIOTECAS ---------------------
#-----------------------------------------------------------------
import customtkinter as ctk
from tkinter import messagebox, Toplevel
from PIL import Image, ImageTk
import os
import base64
from tkinter import *

# ---------------CRIAÇÃO DA PASTA USERS E CODIFICAÇÃO DA INFORMAÇÃO ---------------------
#-----------------------------------------------------------------
if not os.path.exists("users"):
    os.makedirs("users")

def encodeBinary(data):
    return base64.b64encode(data.encode()).decode()

def decodeBinary(data):
    return base64.b64decode(data.encode()).decode()

# ---------------VARIAVEIS GLOBAIS---------------------
#-----------------------------------------------------------------
currentUser = ""
userLibrary = []

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
app.iconbitmap(".\\Images\\1-f8c98aa8.ico")
renderWindow(1280, 832, "GameON!")

# ---------------FRAMES ---------------------
#-----------------------------------------------------------------
def showFrame(frame):
    frame.tkraise()

app.rowconfigure(0, weight=1)
app.columnconfigure(0, weight=1)

loginFrame = ctk.CTkFrame(app)
adminFrame = ctk.CTkFrame(app)
userFrame = ctk.CTkFrame(app)
signinFrame = ctk.CTkFrame(app)
loginFrame.pack(expand=True)

for frame in (loginFrame, adminFrame, userFrame, signinFrame):
    frame.grid(row=0, column=0, sticky="nsew")

# ---------------CARREGAR JOGOS ---------------------
#-----------------------------------------------------------------
def loadGames():
    games = []
    if os.path.exists("games.txt"):
        file = open("games.txt", "r")
        for line in file:
            name, description, image = line.strip().split("|")
            games.append({"name": name, "description": description, "image": image})
        file.close()
    return games

# ---------------GUARDAR JOGOS ---------------------
#-----------------------------------------------------------------
def saveGame(name, description, image):
    file = open("games.txt", "a")
    file.write(f"{name}|{description}|{image}\n")
    file.close()

# ---------------CARREGAR BIBLIOTECA---------------------
#-----------------------------------------------------------------
def loadUserLibrary(username):
    library = []
    userFile = os.path.join("users", f"{username}_library.txt")
    if os.path.exists(userFile):
        file = open(userFile, "r")
        for line in file:
            decodedLine = decodeBinary(line.strip())
            name, description, image = decodedLine.split("|")
            library.append({"name": name, "description": description, "image": image})
        file.close()
    return library

# ---------------GUARDAR BIBLIOTECA ---------------------
#-----------------------------------------------------------------
def saveToUserLibrary(username, game):
    userFile = os.path.join("users", f"{username}_library.txt")
    file = open(userFile, "a")
    encodedLine = encodeBinary(f"{game['name']}|{game['description']}|{game['image']}")
    file.write(f"{encodedLine}\n")
    file.close()

# ---------------ADICIONAR NOS FAVORITOS ---------------------
#-----------------------------------------------------------------
def addToFavorites(game):
    if game not in userLibrary:
        userLibrary.append(game)
        saveToUserLibrary(currentUser, game)
        refreshUserLibrary()

# ---------------XXXXXXXX ---------------------
#-----------------------------------------------------------------
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
#--------------------------------------------------------------------------------------------------------------------------

# ---------------PÁGINA PRINCIPAL (É NECESSÁRIO ARRANJAR - FALTA A IMAGEM E COLOCAR AS CARDS)---------------------
#-----------------------------------------------------------------
def homePage():
    for widget in app.winfo_children():
        widget.destroy()
        
    sidebar = ctk.CTkFrame(app, width=330, height=830, corner_radius=0, bg_color="#101010")
    sidebar.pack(side=ctk.LEFT, fill=ctk.Y)

    logo = ctk.CTkLabel(sidebar, text="GameON!", text_color="#ffa500", font=("Arial", 16, "bold"))
    logo.pack(pady=20)

    button_frame = ctk.CTkFrame(sidebar)
    button_frame.pack(expand=True)

    buttons = ["LIBRARY", "STORE", "WISHLIST", "DISCOVER"]
    for btn in buttons:
        button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                            font=("Arial", 12), hover_color="#5A5A5A", command=lambda btn=btn: print(f"{btn}"),
                            width=247, height=44)
        button.pack(pady=5, padx=42)

    profile_button_frame = ctk.CTkFrame(sidebar)
    profile_button_frame.pack(side=ctk.BOTTOM, pady=15)  

    profile_settingsBtn = ctk.CTkButton(profile_button_frame, text="PROFILE SETTINGS", text_color="white", fg_color="#ff4500",
                                        font=("Arial", 12), hover_color="#FF5900", command=app, width=247, height=44)
    profile_settingsBtn.pack(pady=5, padx=42)  

    topbar = ctk.CTkFrame(app, width=948, height=128, corner_radius=0, bg_color="#101010")
    topbar.pack(side=ctk.TOP, fill=ctk.X)
    
    home_label = ctk.CTkLabel(topbar, text="HOME", text_color="white", font=("Arial", 18))
    home_label.pack(side=ctk.LEFT, padx=35)

    circle_button = ctk.CTkButton(topbar, width=120, height=50, corner_radius=25, fg_color="#FF4500", hover_color="#FF5900",
                              command="")
    circle_button.pack(side=ctk.RIGHT, padx=30, pady=50)

    search_entry = ctk.CTkEntry(topbar, placeholder_text="Search...", font=("Arial", 16))
    search_entry.pack(side=ctk.RIGHT, padx=20, pady=50)

"""  profile_settingsBtn = ctk.CTkButton(sidebar, text="PROFILE SETTINGS", text_color="white", fg_color="#ff4500",
                             font=("Arial", 12), hover_color="#FF5900", command=app)
    profile_settingsBtn.pack(side=ctk.BOTTOM, fill=ctk.X, pady=10, padx=10)
 
    main_content = ctk.CTkFrame(app, bg_color="#000000")
    main_content.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True)

    top_bar = ctk.CTkFrame(main_content, height=50, fg_color="#1a1a1a")
    top_bar.pack(side=ctk.TOP, fill=ctk.X)

    home_label = ctk.CTkLabel(top_bar, text="HOME", text_color="white", font=("Arial", 14))
    home_label.pack(side=ctk.LEFT, padx=20)

    search_entry = ctk.CTkEntry(top_bar, placeholder_text="SEARCH...", font=("Arial", 12))
    search_entry.pack(side=ctk.RIGHT, padx=20, pady=10)

    discount_frame = ctk.CTkFrame(main_content, fg_color="#ffa500", height=150)
    discount_frame.pack(fill=ctk.X, pady=10, padx=20)

    discount_label = ctk.CTkLabel(discount_frame, text="DISCOUNT", text_color="#000000",
                                  font=("Arial", 16, "bold"))
    discount_label.pack(pady=20)

    game_frame = ctk.CTkFrame(main_content, bg_color="#000000")
    game_frame.pack(fill=ctk.BOTH, expand=True, padx=20, pady=10)

    for i in range(3):  
        game_card = ctk.CTkFrame(game_frame, fg_color="#cccccc", width=200, height=250)
        game_card.pack(side=ctk.LEFT, padx=20, pady=10)

        game_label = ctk.CTkLabel(game_card, text=f"GAME {i + 1}", text_color="#000000", font=("Arial", 12, "bold"))
        game_label.pack(pady=40)

        game_info = ctk.CTkLabel(game_card, text="Name game\nPrice", text_color="#000000", font=("Arial", 10))
        game_info.pack(side=ctk.BOTTOM, pady=10)

        favorite_icon = ctk.CTkLabel(game_card, text="\u2764", text_color="#000000", font=("Arial", 14))
        favorite_icon.pack(side=ctk.BOTTOM)
  """
#---------------------------------------------------------------------------------------------------------------------------------

# ---------------FUNÇÃO LOGIN UTILIZADOR ---------------------
#-----------------------------------------------------------------
def loginAsUser():
    global currentUser
    login_input = usernameEntry.get().strip()  
    password = passwordEntry.get().strip() 

    if login_input and password:
        if '@' in login_input:
            userFound = False
            for file_name in os.listdir("users"):
                if file_name.endswith(".txt"):
                    userFile = os.path.join("users", file_name)
                    file = open(userFile, "r")
                    savedUsername = decodeBinary(file.readline().strip())
                    savedPassword = decodeBinary(file.readline().strip())
                    savedEmail = decodeBinary(file.readline().strip())
                    file.close()

                    if savedEmail == login_input: 
                        if savedPassword == password:  
                            currentUser = savedUsername
                            showFrame(userFrame)  
                            userFound = True
                        else:
                            messagebox.showerror("Error", "Wrong password.")
                            userFound = True
                        break
            if not userFound:
                messagebox.showerror("Error", "Email not found.")
        else:
            userFile = os.path.join("users", f"{login_input}.txt")
            if os.path.exists(userFile):
                file = open(userFile, "r")
                savedPassword = decodeBinary(file.readline().strip())
                file.close()

                if savedPassword == password:  
                    currentUser = login_input
                    showFrame(userFrame)  
                else:
                    messagebox.showerror("Error", "Wrong password.")
            else:
                messagebox.showerror("Error", "User not found.")
    else:
        messagebox.showwarning("Warning", "Fill all the fields.")


def goToRegister():
    showFrame(signinFrame)


box = LabelFrame(loginFrame, padx=150, pady=50, bg="#2E2B2B", borderwidth=0)
box.pack(expand=True)

logo = ctk.CTkLabel(box, text="GameON!", text_color="#ffa500", font=("Arial", 16, "bold"))
logo.grid(pady=10)        

usernameEntry = ctk.CTkEntry(box, placeholder_text="USERNAME/EMAIL", width=250)
usernameEntry.grid(padx=(10, 10), pady=(50, 10))

passwordEntry = ctk.CTkEntry(box, placeholder_text="PASSWORD", show="*", width=250)
passwordEntry.grid(pady=10)

userButton = ctk.CTkButton(box, text="LOGIN", command=loginAsUser, width=250, height=30, fg_color="#ffa500", text_color="#000000")
userButton.grid(pady=5)

registerButton = ctk.CTkButton(box, text="SIGN IN", command=goToRegister, width=250, height=30, fg_color="#ffa500", text_color="#000000")
registerButton.grid(pady=5)

previewBtn = ctk.CTkButton(box, text="Previsualização", command=homePage, width=250, height=30, fg_color="#ffa500", text_color="#000000")
previewBtn.grid(pady=5) 

registerLabel = ctk.CTkLabel(signinFrame, text="New user", font=("Arial", 24))
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

newUsernameEntry = ctk.CTkEntry(signinFrame, placeholder_text="Novo Nome de utilizador")
newUsernameEntry.pack(pady=10)

newPasswordEntry = ctk.CTkEntry(signinFrame, placeholder_text="Senha", show="*")
newPasswordEntry.pack(pady=10)

registerConfirmButton = ctk.CTkButton(signinFrame, text="Registrar", command=registerUser, width=250, height=50)
registerConfirmButton.pack(pady=20)

registerBackButton = ctk.CTkButton(signinFrame, text="Voltar", command=lambda: showFrame(loginFrame), width=250, height=50)
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