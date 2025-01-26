import customtkinter as ctk
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageDraw
import os

if not os.path.exists("profileImages"):
    os.makedirs("profileImages")

def renderWindow(appWidth, appHeight, appTitle):
    app.title(appTitle)
    screenWidth = app.winfo_screenwidth()
    screenHeight = app.winfo_screenheight()
    x = (screenWidth / 2) - (appWidth / 2)
    y = (screenHeight / 2) - (appHeight / 2)
    app.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
    app.resizable(False, False)

app = ctk.CTk()
app.configure(fg_color="black")
renderWindow(800, 600, "Profile Image Demo")

profile_img = None
profile_circle = None

def loadProfileImage():
    global profile_img
    profile_image_folder = "profileImages"
    if os.listdir(profile_image_folder):
        first_image_path = os.path.join(profile_image_folder, os.listdir(profile_image_folder)[0]) 
        img = Image.open(first_image_path).resize((100, 100), Image.Resampling.LANCZOS)
        mask = Image.new("L", (100, 100), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, 100, 100), fill=255)
        img.putalpha(mask)
        profile_img = ctk.CTkImage(img, size=(100, 100))

def selectProfileImage():
    global profile_img
    file_path = filedialog.askopenfilename(initialdir="./Images", title="Select Image",
                                           filetypes=(("PNG Images", "*.png"), ("JPG Images", "*.jpg")))

    if file_path:
        new_file_path = os.path.join("profileImages", os.path.basename(file_path))
        
        img = Image.open(file_path).resize((100, 100), Image.Resampling.LANCZOS)
        mask = Image.new("L", (100, 100), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, 100, 100), fill=255)
        img.putalpha(mask)
        profile_img = ctk.CTkImage(img, size=(100, 100))
        
        img.save(new_file_path)

        profile_circle.configure(image=profile_img, fg_color="transparent")
        profile_circle.image = profile_img

def mainPage():
    for widget in app.winfo_children():
        widget.destroy()

    global profile_circle

    user_info_frame = ctk.CTkFrame(app, width=300, height=200, fg_color="#2E2B2B")
    user_info_frame.place(relx=0.5, rely=0.5, anchor="center")  

    profile_circle = ctk.CTkButton(user_info_frame, width=100, height=100, corner_radius=77, fg_color="#FFA500",
                                   text="", hover_color="#FF5900", command=selectProfileImage)
    profile_circle.place(relx=0.5, rely=0.3, anchor="center")  

    if profile_img:
        profile_circle.configure(image=profile_img, fg_color="transparent")
        profile_circle.image = profile_img

    switch_button = ctk.CTkButton(app, text="Go to Page 2", command=pageTwo)
    switch_button.place(relx=0.5, rely=0.7, anchor="center")  

def pageTwo():
    for widget in app.winfo_children():
        widget.destroy()

    global profile_circle

    user_info_frame = ctk.CTkFrame(app, width=300, height=200, fg_color="#2E2B2B")
    user_info_frame.place(relx=0.5, rely=0.5, anchor="center")  

    profile_circle = ctk.CTkButton(user_info_frame, width=100, height=100, corner_radius=77, fg_color="#FFA500",
                                   text="", hover_color="#FF5900", command=selectProfileImage)
    profile_circle.place(relx=0.5, rely=0.3, anchor="center")  

    if profile_img:
        profile_circle.configure(image=profile_img, fg_color="transparent")
        profile_circle.image = profile_img

    switch_button = ctk.CTkButton(app, text="Go to Page 1", command=mainPage)
    switch_button.place(relx=0.5, rely=0.7, anchor="center")  

loadProfileImage()
mainPage()
app.mainloop()
