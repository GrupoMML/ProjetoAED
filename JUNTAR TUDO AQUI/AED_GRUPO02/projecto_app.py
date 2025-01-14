# ---------------BIBLIOTECAS ---------------------
#-----------------------------------------------------------------
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
import os
import base64
from PIL import Image

# ---------------CRIAÇÃO DA PASTA USERS E CODIFICAÇÃO DA INFORMAÇÃO ---------------------
#-----------------------------------------------------------------
if not os.path.exists("users"):
    os.makedirs("users")

def encodeBinary(data):
    return base64.b64encode(data.encode()).decode()

def decodeBinary(data):
    return base64.b64decode(data.encode()).decode()

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
renderWindow(1280, 832, "GameON!")

# Função para trocar entre os frames
def showFrame(frame):
    """
    Oculta todos os frames e exibe apenas o especificado.
    """
    initital_frame.pack_forget()
    login_frame.pack_forget()
    frame.pack(fill="both", expand=True)

# --------------ECRÃ INICIAL ---------------------
#-----------------------------------------------------------------
initital_frame = ctk.CTkFrame(app, width=1280, height=832, fg_color="#2E2B2B", corner_radius=0)
initital_frame.pack(fill="both", expand=True)

imgIcon = ctk.CTkImage(Image.open("Images/Logo.png"), size=(450, 150))
imgIcon_label = ctk.CTkLabel(initital_frame, image=imgIcon, text="")
imgIcon_label.place(relx=0.5, rely=0.35, anchor="center")

initial_msg_label = ctk.CTkLabel(initital_frame, text="WELCOME TO YOUR FAVORITE PLACE TO PLAY GAMES!",
                                  font=ctk.CTkFont(size=24, weight="bold"), text_color="white")
initial_msg_label.place(relx=0.5, rely=0.5, anchor="center")

button_frame = ctk.CTkFrame(initital_frame, width=480, height=85, fg_color="#202020", corner_radius=15)
button_frame.place(relx=0.5, rely=0.6, anchor="center")  

initialBtn = ctk.CTkButton(button_frame, text="CLICK HERE IF YOU’RE ON!", text_color="black", fg_color="#FFA500",
                           font=ctk.CTkFont(size=20, weight="bold"), hover_color="#FF5900",
                           command=lambda: showFrame(login_frame), width=480, height=85)
initialBtn.place(relx=0.5, rely=0.5, anchor="center") 

# ---------------AREA UTILIZADOR (LOGIN) ---------------------
#-----------------------------------------------------------------
login_frame = ctk.CTkFrame(app, width=1280, height=832, fg_color="#2E2B2B", corner_radius=0)

imgIcon = ctk.CTkImage(Image.open("Images/Logo.png"), size=(290, 100))
imgIcon_label = ctk.CTkLabel(login_frame, image=imgIcon, text="", fg_color="#2E2B2B")
imgIcon_label.place(relx=0.5, rely=0.2, anchor="center")

input_frame = ctk.CTkFrame(login_frame, width=550, height=350, fg_color="#2E2B2B")
input_frame.place(relx=0.5, rely=0.6, anchor="center")  

username_entry = ctk.CTkEntry(input_frame, fg_color="white", width=290, height=37, border_color="#2E2B2B", corner_radius=5, 
                               placeholder_text="USERNAME / EMAIL", placeholder_text_color="black", text_color="black",
                               font=("Arial", 12, "bold"))
username_entry.pack(pady=5, anchor="center")

password_entry = ctk.CTkEntry(input_frame, fg_color="white", show="*", width=290, height=37, border_color="#2E2B2B", corner_radius=5, 
                               placeholder_text="PASSWORD", placeholder_text_color="black", text_color="black",
                               font=("Arial", 12, "bold"))
password_entry.pack(pady=5, anchor="center")

button_frame = ctk.CTkFrame(input_frame, fg_color="#2E2B2B")
button_frame.pack(pady=(20, 20), anchor="center")

loginBtn = ctk.CTkButton(button_frame, text="LOGIN", fg_color="#FFA500", hover_color="#FF5900", width=140, height=37, 
                             border_color="#2E2B2B", text_color="black", font=ctk.CTkFont(size=20, weight="bold"), command="")
loginBtn.pack(side="left", padx=5, anchor="center")

signinBtn = ctk.CTkButton(button_frame, text="SIGN IN", fg_color="#FFA500", hover_color="#FF5900", width=140, height=37, 
                              border_color="#2E2B2B", text_color="black", font=ctk.CTkFont(size=20, weight="bold"), command="")
signinBtn.pack(side="left", padx=5, anchor="center")

qrcode_frame = ctk.CTkFrame(input_frame, fg_color="#2E2B2B")
qrcode_frame.pack(pady=(5, 20), anchor="center")

qrcodeBtn = ctk.CTkButton(qrcode_frame, text="QR CODE", fg_color="#FFA500", hover_color="#FF5900", 
                              width=292, height=37, border_color="#2E2B2B", text_color="black", 
                              font=ctk.CTkFont(size=20, weight="bold"), command="")
qrcodeBtn.pack(padx=5, anchor="center")

# ---------------FIM DA FUNÇÃO DA APP ---------------------
#-----------------------------------------------------------------
app.mainloop()
