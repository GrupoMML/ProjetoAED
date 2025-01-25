# ---------------BIBLIOTECAS ---------------------
#-----------------------------------------------------------------
import customtkinter as ctk
from tkinter import messagebox
import os
import base64
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import Image

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

# ---------------PÁGINA ADMIN---------------------
#-----------------------------------------------------------------
def adminPage():
    for widget in app.winfo_children():
        widget.destroy()
        
    sidebar = ctk.CTkFrame(app, width=330, height=830, corner_radius=0, bg_color="#101010")
    sidebar.pack(side=ctk.LEFT, fill=ctk.Y)

    imgIcon = ctk.CTkImage(Image.open("Images/Logo.png"), size=(200, 75))
    imgIcon_label = ctk.CTkLabel(sidebar, image=imgIcon, text="", fg_color="#2E2B2B")
    imgIcon_label.place(x=61, y=26)

    button_frame = ctk.CTkFrame(sidebar)
    button_frame.pack(expand=True)

    buttons = ["LIBRARY", "STORE", "DISCOVER"]
    for btn in buttons:
        if btn == "LIBRARY":
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:"",
                                width=247, height=44)
        elif btn == "STORE":
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:"",
                                width=247, height=44)
        else:  
            button = ctk.CTkButton(button_frame, text=btn, text_color="white", fg_color="#383838",
                                font=("Arial", 12), hover_color="#5A5A5A", command=lambda:"",
                                width=247, height=44)
        button.pack(pady=5, padx=42)

    topbar = ctk.CTkFrame(app, width=948, height=128, corner_radius=0, bg_color="#101010")
    topbar.pack(side=ctk.TOP, fill=ctk.X)
    
    admin_label = ctk.CTkLabel(topbar, text="ADMIN", text_color="white", font=("Arial", 18))
    admin_label.pack(side=ctk.LEFT, padx=35, pady=50)

    button_frame = ctk.CTkFrame(app, fg_color="black")
    button_frame.pack(pady=(80, 0), anchor="center")

    userManagerBtn = ctk.CTkButton(button_frame, text="USER MANAGER", fg_color="#FFA500", hover_color="#FF5900", width=140, height=37, 
                                border_color="#2E2B2B", text_color="black", font=ctk.CTkFont(size=20, weight="bold"), command="")
    userManagerBtn.pack(side="left", padx=50, anchor="center")

    gameManagerBtn = ctk.CTkButton(button_frame, text="GAME MANAGER", fg_color="#FFA500", hover_color="#FF5900", width=140, height=37, 
                                border_color="#2E2B2B", text_color="black", font=ctk.CTkFont(size=20, weight="bold"), command="")
    gameManagerBtn.pack(side="left", padx=50, anchor="center")

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

adminPage()
app.mainloop()
