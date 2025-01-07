import customtkinter
from tkinter import messagebox
import os
import base64

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

app = customtkinter.CTk()
app.configure(fg_color="black")  
renderWindow(550, 350, "GameON!")

# ---------------FRAMES ---------------------
#-----------------------------------------------------------------
def showFrame(frame):
    frame.tkraise()

app.rowconfigure(0, weight=1)
app.columnconfigure(0, weight=1)

main_frame = customtkinter.CTkFrame(app, fg_color="black")
main_frame.grid(row=0, column=0, sticky="nsew")

login_frame = customtkinter.CTkFrame(main_frame, fg_color="black")
admin_frame = customtkinter.CTkFrame(main_frame, fg_color="black")
user_frame = customtkinter.CTkFrame(main_frame, fg_color="black")
signIn_frame = customtkinter.CTkFrame(main_frame, fg_color="black")

for frame in (login_frame, admin_frame, user_frame, signIn_frame):
    frame.grid(row=0, column=0, sticky="nsew")

# ---------------VARIAVEIS ---------------------
#-----------------------------------------------------------------
currentUser = ""

# ---------------FRAME LOGIN ---------------------
#-----------------------------------------------------------------
def loginAsUser():
    global currentUser
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    
    if username and password:
        userFile = os.path.join("users", f"{username}.txt")
        
        if os.path.exists(userFile):
            file = open(userFile, "r")
            savedPassword = decodeBinary(file.readline().strip())
            file.close()
            
            if savedPassword == password:
                currentUser = username
                showFrame(user_frame)
            else:
                messagebox.showerror("Error", "Wrong password.")
        else:
            messagebox.showerror("Error", "User not found.")
    else:
        messagebox.showwarning("Warning", "Fill all the fields.")

# ---------------FRAMES SIGN IN ---------------------
#-----------------------------------------------------------------
def goToRegister():
    showFrame(signIn_frame)

def registerUser():
    newUsername = newUsernameEntry.get().strip()
    newEmail = newEmailEntry.get().strip()
    newPassword = newPasswordEntry.get().strip()
    
    if newUsername and newEmail and newPassword:
        userFile = os.path.join("users", f"{newUsername}.txt")
        if not os.path.exists(userFile):
            file = open(userFile, "w")
            file.write(f"{encodeBinary(newPassword)}\n")
            file.close()
            messagebox.showinfo("Sucesso", "Utilizador registrado com sucesso!")
            showFrame(login_frame)  
        else:
            messagebox.showwarning("Aviso", "Utilizador já existe!")
    else:
        messagebox.showwarning("Aviso", "Preencha todos os campos!")

# ---------------AREA UTILIZADOR (LOGIN) ---------------------
#-----------------------------------------------------------------
input_frame = customtkinter.CTkFrame(login_frame, fg_color="black")
input_frame.pack(padx=20, pady=(80, 20))

username_entry = customtkinter.CTkEntry(input_frame, fg_color="purple", width=200, height=25, border_color="black", corner_radius=5, placeholder_text="Username", text_color="white")
username_entry.pack(pady=5, anchor="center")

password_entry = customtkinter.CTkEntry(input_frame, fg_color="purple", show="*", width=200, height=25, border_color="black", corner_radius=5, placeholder_text="Password", text_color="white")
password_entry.pack(pady=5, anchor="center")

button_frame = customtkinter.CTkFrame(input_frame, fg_color="black")
button_frame.pack(pady=(40, 20), anchor="center")

login_button = customtkinter.CTkButton(button_frame, text="Login", fg_color="purple", width=95, height=25, border_color="black", command=loginAsUser)
login_button.pack(side="left", padx=5, anchor="center")

signIn_button = customtkinter.CTkButton(button_frame, text="Sign In", fg_color="purple", width=95, height=25, border_color="black", command=goToRegister)
signIn_button.pack(side="left", padx=5, anchor="center")

# ---------------AREA UTILIZADOR (SIGN IN)---------------------
#-----------------------------------------------------------------

signIn_input_frame = customtkinter.CTkFrame(signIn_frame, fg_color="black")
signIn_input_frame.pack(padx=20, pady=(80, 20))

newUsernameEntry = customtkinter.CTkEntry(signIn_input_frame, fg_color="purple", width=200, height=25, border_color="black", corner_radius=5, placeholder_text="New Username", text_color="white")
newUsernameEntry.pack(pady=5, anchor="center")

newEmailEntry = customtkinter.CTkEntry(signIn_input_frame, fg_color="purple", width=200, height=25, border_color="black", corner_radius=5, placeholder_text="Email", text_color="white")
newEmailEntry.pack(pady=5, anchor="center")

newPasswordEntry = customtkinter.CTkEntry(signIn_input_frame, fg_color="purple", show="*", width=200, height=25, border_color="black", corner_radius=5, placeholder_text="New Password", text_color="white")
newPasswordEntry.pack(pady=5, anchor="center")

signIn_button_frame = customtkinter.CTkFrame(signIn_input_frame, fg_color="black")
signIn_button_frame.pack(pady=(40, 20), anchor="center")

register_button = customtkinter.CTkButton(signIn_button_frame, text="Register", fg_color="purple", width=95, height=25, border_color="black", command=registerUser)
register_button.pack(side="left", padx=5, anchor="center")

login_button_signIn = customtkinter.CTkButton(signIn_button_frame, text="Back to Login", fg_color="purple", width=95, height=25, border_color="black", command=lambda: showFrame(login_frame))
login_button_signIn.pack(side="left", padx=5, anchor="center")

showFrame(login_frame)

app.mainloop()
