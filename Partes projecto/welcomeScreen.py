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
    canvas.create_oval(10, 10, 102, 102, width=10, outline="black") 
    canvas.create_arc(10, 10, 102, 102, start=angle, extent=270, width=10, outline="orange") 

def update_loading_circle(canvas, angle):
    angle += -5  
    if angle >= 360:
        angle = 0  
    draw_loading_circle(canvas, angle)
    canvas.after(50, update_loading_circle, canvas, angle) 

def pressBtn():

    descriptionLabel.destroy()
    msg_welcome_label.destroy()
    previewBtn.destroy()
    imgIcon_label.destroy()

    update_loading_circle(loading_canvas, 0)
    # O background do círculo deve ser cor #000000

    msg_loading_label = ctk.CTkLabel(main_frame, text="LOADING...", font=ctk.CTkFont(size=10, weight="bold"), text_color="white")
    msg_loading_label.pack(pady=10)

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

# ---------------BEM VINDO ---------------------
#-----------------------------------------------------------------

main_frame = ctk.CTkFrame(app, width=1280, height=832, fg_color="#000000", corner_radius=0)
main_frame.pack(expand=True)

box = ctk.CTkFrame(main_frame, height=500, width=600, fg_color="#2E2B2B", corner_radius=10)
box.pack(padx=5, pady=10)

imgIcon = ctk.CTkImage(Image.open("Images/Logo.png"), size=(200, 74))
imgIcon_label = ctk.CTkLabel(box, image=imgIcon, text="")
imgIcon_label.pack(pady=20)

msg_welcome_label = ctk.CTkLabel(box, text="Very welcome to Game ON!", font=ctk.CTkFont(size=24, weight="bold"), text_color="white")
msg_welcome_label.pack(pady=10)

descriptionLabel = ctk.CTkLabel(box, font=ctk.CTkFont(size=15, weight="bold"), text_color="white",  
                                text="Here you'll gonna find your favorite games,\nyou can liked, save in your Wish List,\nbuy your favorite ones and download your\nmoment game! You can still find a great\ndiscounts that fit in your budget!")
descriptionLabel.pack(padx=20)

previewBtn = ctk.CTkButton(box, text="So, let the Game ON!", font=ctk.CTkFont(size=24, weight="bold"), text_color="white", command=pressBtn)
previewBtn.pack(pady=10)

loading_canvas = tk.Canvas(box, width=120, height=120, bg="#2E2B2B", bd=0, highlightthickness=0)
loading_canvas.pack()

app.mainloop()
