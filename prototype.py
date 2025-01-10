# ---------------BIBLIOTECAS ---------------------
import customtkinter 
from tkinter import messagebox
import os
import base64
from PIL import Image
from tkinter.font import Font

# ---------------PARTE DAS PASTAS ---------------------
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

app = customtkinter.CTk()
app.configure(fg_color="grey")  
app.iconbitmap(".\\Images\\1-f8c98aa8.ico")
renderWindow(1080, 695, "GameON!")

# ---------------FRAMES ---------------------
#-----------------------------------------------------------------
def showFrame(frame):
    """
    Levanta o frame especificado.
    """
    frame.tkraise()

app.rowconfigure(0, weight=1)
app.columnconfigure(0, weight=1)

main_frame = customtkinter.CTkFrame(app, width=550, height=350, fg_color="white")
main_frame.grid(row=0, column=0, sticky="nsew")
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_columnconfigure(0, weight=1)

login_frame = customtkinter.CTkFrame(main_frame, fg_color="grey")
user_frame = customtkinter.CTkFrame(main_frame, fg_color="grey")
signIn_frame = customtkinter.CTkFrame(main_frame, fg_color="grey")

for frame in (login_frame, user_frame, signIn_frame):
    frame.grid(row=0, column=0, sticky="nsew")


# ---------------VARIAVEIS ---------------------
#-----------------------------------------------------------------
currentUser = ""

# ---------------FONTES TEXTO ---------------------
#-----------------------------------------------------------------
bold_font = ("Arial", 14, "bold")

# ---------------FUNÇÃO LOGIN UTILIZADOR ---------------------
#-----------------------------------------------------------------
def loginAsUser():
    global currentUser
    login_input = username_entry.get().strip()  
    password = password_entry.get().strip() 

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
                            showFrame(user_frame)  
                            userFound = True
                        else:
                            messagebox.showerror("Error", "Wrong username or password.")
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
                    showFrame(user_frame)  
                else:
                    messagebox.showerror("Error", "Wrong username or password.")
            else:
                messagebox.showerror("Error", "User not found.")
    else:
        messagebox.showwarning("Warning", "Fill all the fields.")



# ---------------FUNÇÃO SIGN IN ---------------------
#----------------------------------------------------
def goToRegister():
    showFrame(signIn_frame)

def registerUser():
    newUsername = newUsernameEntry.get().strip()
    newEmail = newEmailEntry.get().strip()
    newPassword = newPasswordEntry.get().strip()
    confirmPassword = confirmPasswordEntry.get().strip()
    
    if newUsername and newEmail and newPassword:
        if '@' not in newEmail:
            messagebox.showwarning("Warning", "Please enter a valid email address with '@'.")
            return
        
        userFile = os.path.join("users", f"{newUsername}.txt")
        if not os.path.exists(userFile):
            file = open(userFile, "w")
            file.write(f"{encodeBinary(newUsername)}\n {encodeBinary(newPassword)}\n {encodeBinary(newEmail)}")
            file.close()
            messagebox.showinfo("Success", "Your account was created.")
            showFrame(login_frame)  
        else:
            messagebox.showwarning("Warning", "You already have an account.")
    else:
        messagebox.showwarning("Warning", "Fill all the fields.")

# --------------- FRAME CINZENTO ---------------------
#-----------------------------------------------------



# --------------- LOGO APP ---------------------
#-----------------------------------------------
imgIcon = customtkinter.CTkImage(Image.open(".\\Images\\Logo.png"), size=(145, 50))
imgIcon_label = customtkinter.CTkLabel(app, image=imgIcon, text="", fg_color="grey")
imgIcon_label.place(x=470, y=200)


# --------------- AREA UTILIZADOR (LOGIN) --------------------
#-------------------------------------------------------------
input_frame = customtkinter.CTkFrame(login_frame, fg_color="grey")
input_frame.place(relx=0.5, rely=0.5, anchor="center")  

username_entry = customtkinter.CTkEntry(input_frame, fg_color="white", width=200, height=25, border_color="black", corner_radius=5, placeholder_text="Username", placeholder_text_color="grey", text_color="black")
username_entry.pack(pady=5, anchor="center")

password_entry = customtkinter.CTkEntry(input_frame, fg_color="white", show="*", width=200, height=25, border_color="black", corner_radius=5, placeholder_text="Password", placeholder_text_color="grey", text_color="black")
password_entry.pack(pady=5, anchor="center")

button_frame = customtkinter.CTkFrame(input_frame, fg_color="gray")
button_frame.pack(pady=(20, 20), anchor="center")

login_button = customtkinter.CTkButton(button_frame, text="LOGIN", fg_color="orange", width=95, height=25, border_color="black", text_color="black", font=("Arial", 14, "bold"), command=loginAsUser)
login_button.pack(side="left", padx=5, anchor="center")

signIn_button = customtkinter.CTkButton(button_frame, text="SIGN IN", fg_color="orange", width=95, height=25, border_color="black", text_color="black", font=("Arial", 14, "bold"), command=goToRegister)
signIn_button.pack(side="left", padx=5, anchor="center")

# --------------- AREA UTILIZADOR (SIGN IN) ----------------------
#-----------------------------------------------------------------

signIn_input_frame = customtkinter.CTkFrame(signIn_frame, fg_color="gray")
signIn_input_frame.place(relx=0.5, rely=0.5, anchor="center") 

newUsernameEntry = customtkinter.CTkEntry(signIn_input_frame, fg_color="white", width=200, height=25, border_color="black", corner_radius=5, placeholder_text="Username", placeholder_text_color="gray", text_color="black")
newUsernameEntry.pack(pady=5, anchor="center")

newEmailEntry = customtkinter.CTkEntry(signIn_input_frame, fg_color="white", width=200, height=25, border_color="black", corner_radius=5, placeholder_text="Email", placeholder_text_color="gray", text_color="black")
newEmailEntry.pack(pady=5, anchor="center")

newPasswordEntry = customtkinter.CTkEntry(signIn_input_frame, fg_color="white", show="*", width=200, height=25, border_color="black", corner_radius=5, placeholder_text="Password", placeholder_text_color="gray", text_color="black")
newPasswordEntry.pack(pady=5, anchor="center")

confirmPasswordEntry = customtkinter.CTkEntry(signIn_input_frame,fg_color="white", show="*", width=200, height=25, border_color="black", corner_radius=5, placeholder_text="Password", placeholder_text_color="gray", text_color="black")
confirmPasswordEntry.pack(pady=5, anchor="center")

signIn_button_frame = customtkinter.CTkFrame(signIn_input_frame, fg_color="gray")
signIn_button_frame.pack(pady=(40, 20), anchor="center")

register_button = customtkinter.CTkButton(signIn_button_frame, text="SIGN IN", fg_color="orange", width=95, height=25, border_color="black", text_color="black", font=bold_font, command = registerUser)
register_button.pack(side="left", padx=5, anchor="center")

login_button_signIn = customtkinter.CTkButton(signIn_button_frame, text="BACK", fg_color="orange", width=95, height=25, border_color="black", text_color="black", font=bold_font, command = lambda: showFrame(login_frame))
login_button_signIn.pack(side="right", padx=5, anchor="center")

#-------------------------------------------------------------
showFrame(login_frame) 

app.mainloop()
