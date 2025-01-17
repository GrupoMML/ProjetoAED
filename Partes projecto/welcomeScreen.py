# ---------------BIBLIOTECAS ---------------------
#-----------------------------------------------------------------
import customtkinter as ctk
import tkinter as tk  
from tkinter import messagebox
import os
import base64
from tkinter import *
from PIL import Image

# ---------------CANVAS PARA O LOADING ---------------------
#-----------------------------------------------------------------
def draw_loading_circle(canvas, angle):
    canvas.delete("all")  
    canvas.create_oval(10, 10, 102, 102, width=10, outline="gray") 
    canvas.create_arc(10, 10, 102, 102, start=angle, extent=270, width=10, outline="orange") 

def update_loading_circle(canvas, angle):
    angle += 10  
    if angle >= 360:
        angle = 0  
    draw_loading_circle(canvas, angle)
    canvas.after(50, update_loading_circle, canvas, angle) 

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

# ---------------BEM VINDO ---------------------
#-----------------------------------------------------------------

main_frame = ctk.CTkFrame(app, width=1280, height=832, fg_color="#2E2B2B", corner_radius=0)
main_frame.pack(fill="both", expand=True)

imgIcon = ctk.CTkImage(Image.open(".\\Images\\Logo.png"), size=(450, 150))
imgIcon_label = ctk.CTkLabel(main_frame, image=imgIcon, text="")
imgIcon_label.place(relx=0.5, rely=0.35, anchor="center")

msg_welcome_label = ctk.CTkLabel(main_frame, text="WELCOME!", font=ctk.CTkFont(size=24, weight="bold"), text_color="white")
msg_welcome_label.place(relx=0.5, rely=0.50, anchor="center")

loading_canvas = tk.Canvas(main_frame, width=120, height=120, bg="#2E2B2B", bd=0, highlightthickness=0)
loading_canvas.place(relx=0.5, rely=0.65, anchor="center")

update_loading_circle(loading_canvas, 0)

msg_loading_label = ctk.CTkLabel(main_frame, text="LOADING...", font=ctk.CTkFont(size=24, weight="bold"), text_color="white")
msg_loading_label.place(relx=0.5, rely=0.80, anchor="center")

app.mainloop()
