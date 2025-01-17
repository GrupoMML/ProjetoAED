# ---------------BIBLIOTECAS ---------------------
#-----------------------------------------------------------------
import customtkinter as ctk
from tkinter import messagebox
import os
import base64
from tkinter import *
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
    app.resizable(False, False)

app = ctk.CTk()
app.configure(fg_color="black")  
app.iconbitmap("Images/1-f8c98aa8.ico")
renderWindow(1280, 832, "GameON!")


# ---------------AREA UTILIZADOR (LOGIN) ---------------------
#-----------------------------------------------------------------
main_frame = ctk.CTkFrame(app, width=800, height=510, fg_color="#2E2B2B", corner_radius=15)
main_frame.place(relx=0.5, rely=0.5, anchor="center")

imgIcon = ctk.CTkImage(Image.open("Images/Logo.png"), size=(290, 100))
imgIcon_label = ctk.CTkLabel(app, image=imgIcon, text="", fg_color="#2E2B2B")
imgIcon_label.place(x=500, y=200)

input_frame = ctk.CTkFrame(main_frame, width=550, height=350, fg_color="#2E2B2B")
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

app.mainloop()
