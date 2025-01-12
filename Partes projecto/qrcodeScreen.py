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
app.iconbitmap(".\\Images\\1-f8c98aa8.ico")
renderWindow(1280, 832, "GameON!")


# ---------------AREA UTILIZADOR (QR CODE) ---------------------
#-----------------------------------------------------------------
main_frame = ctk.CTkFrame(app, width=800, height=510, fg_color="#2E2B2B")
main_frame.place(relx=0.5, rely=0.5, anchor="center")

imgIcon = ctk.CTkImage(Image.open(".\\Images\\Logo.png"), size=(290, 100))
imgIcon_label = ctk.CTkLabel(app, image=imgIcon, text="", fg_color="#2E2B2B")
imgIcon_label.place(x=500, y=200)

input_frame = ctk.CTkFrame(main_frame, width=550, height=350, fg_color="#2E2B2B")
input_frame.place(relx=0.5, rely=0.9, anchor="center")  

msg_qrcode_label = ctk.CTkLabel(main_frame, text="SCAN & GO!", font=ctk.CTkFont(size=24, weight="bold"), text_color="white")
msg_qrcode_label.place(relx=0.5, rely=0.3, anchor="center")

imgQR = ctk.CTkImage(Image.open(".\\Images\\frame.png"), size=(239, 239))
imgQR_label = ctk.CTkLabel(main_frame, image=imgQR, text="", fg_color="#2E2B2B")
imgQR_label.place(relx=0.5, rely=0.6, anchor="center") 

button_frame = ctk.CTkFrame(input_frame, fg_color="#2E2B2B")
button_frame.pack(pady=(20, 20), anchor="center")

scanBtn = ctk.CTkButton(button_frame, text="SCAN IT", fg_color="#FFA500", hover_color="#FF5900", width=140, height=37, 
                              border_color="#2E2B2B", text_color="black", font=ctk.CTkFont(size=20, weight="bold"), command="")
scanBtn.pack(side="left", padx=5, anchor="center")

backBtn = ctk.CTkButton(button_frame, text="BACK", fg_color="#FFA500", hover_color="#FF5900", width=140, height=37, 
                             border_color="#2E2B2B", text_color="black", font=ctk.CTkFont(size=20, weight="bold"), command="")
backBtn.pack(side="left", padx=5, anchor="center")

app.mainloop()
