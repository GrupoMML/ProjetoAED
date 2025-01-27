import re
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image


def filterGames(search_text):
    """
    Função que filtra os jogos com base no texto de pesquisa.
    """
    # Limpa todos os widgets da game_frame antes de adicionar os resultados
    for widget in game_frame.winfo_children():
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

# Chama a função de pesquisa inicial
filterGames(search_entry.get())

