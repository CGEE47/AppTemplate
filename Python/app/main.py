# Welcome to Lyf Mentor
import customtkinter as ctk

appColourMode = "Light"

def mainLoginWindow():
    global appColourMode
    # Window
    loginWindow = ctk.CTk()
    loginWindow.title("Lyf Mentor")
    loginWindow.geometry("400x500")
    loginWindow.resizable(False, False)
    ctk.set_appearance_mode(appColourMode)

    # Login Label
    loginLabel = ctk.CTkLabel(loginWindow,
        text = "Login",
        text_color = ("#6F686D","#E0D3D3"),
        font = ('Humanist', 40))
    loginLabel.place(relx=0.5, rely=0.3, anchor = "center")

    # Username Textbox
    userTextbox = ctk.CTkTextbox(loginWindow,
        text_color = ("#E0D3D3","#6F686D"),
        fg_color = ("#6F686D","#E0D3D3"),
        activate_scrollbars = False,
        height = 1,
        width = 220,
        font = ('Humanist', 13))
    userTextbox.place(relx=0.5, rely=0.46, anchor = "center")

    # Password Textbox
    passTextbox = ctk.CTkTextbox(loginWindow,
        text_color = ("#E0D3D3","#6F686D"),
        fg_color = ("#6F686D","#E0D3D3"),
        activate_scrollbars = False,
        height = 1,
        width = 220,
        font = ('Humanist', 13))
    passTextbox.place(relx=0.5, rely=0.54, anchor = "center")

    # Login Button
    appLoginButton = ctk.CTkButton(loginWindow,
        text = ("Login"),
        fg_color = ("#6F686D","#E0D3D3"),
        text_color = ("#E0D3D3","#6F686D"))
    appLoginButton.place(relx=0.5, rely=0.65, anchor = "center")

    # Colour Mode Button
    appColourModeButton = ctk.CTkButton(loginWindow,
        text = ("Colour Mode"),
        fg_color = ("#6F686D","#E0D3D3"),
        text_color = ("#E0D3D3","#6F686D"),
        command = lambda: switchAppColourMode())
    appColourModeButton.place(relx=0.97, rely=0.03, relwidth=0.22, anchor = "ne")

    loginWindow.mainloop()

def switchAppColourMode():
    global appColourMode
    if appColourMode == "Light":
        appColourMode = "Dark"
        ctk.set_appearance_mode(appColourMode)
    else:
        appColourMode = "Light"
        ctk.set_appearance_mode(appColourMode)

mainLoginWindow()

'''
Colour Palette

E0D3D3 - Pale
D8D0C1 - Bone
CBB8A9 - Dun
B3B492 - Sage
6F686D - Dim gray
