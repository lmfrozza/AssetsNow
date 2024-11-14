import customtkinter as ctk
from instalation import Config_Folder_Appdata, Verify_Folder, Verify_Folder_userdb
import webbrowser
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue") 


app = ctk.CTk()
app.geometry("1200x600")
app.title("AssetsNow | Facilite suas aplicações financeiras! ")

#HEADER DIV
header_frame = ctk.CTkFrame(app, fg_color="#1b74c1")
header_frame.pack(side="top", fill="x")

#HEADER H2
header_label = ctk.CTkLabel(header_frame, text="AssetsNow", font=("Arial", 16))
header_label.pack(side="left", padx=40, pady=10) 



#HEADER "NAV"
header_nav_frame = ctk.CTkFrame(header_frame, fg_color="#1b74c1")
header_nav_frame.pack(side="right", padx=10)



link1 = ctk.CTkButton(header_nav_frame, text="Configurações", command=lambda: toggle_menu_config(), fg_color="transparent", text_color="white", hover_color="#3b74c9")
link1.pack(side="left",pady=1)

link2 = ctk.CTkButton(header_nav_frame, text="Chaves APIs", command=lambda: toggle_menu_APIs(), fg_color="transparent", text_color="white", hover_color="#3b74c9")
link2.pack(side="left",pady=1)


link3 = ctk.CTkButton(header_nav_frame, text="Instalação", command=lambda: toggle_menu_Install(), fg_color="transparent", text_color="white", hover_color="#3b74c9")
link3.pack(side="left",pady=1)


link4 = ctk.CTkButton(header_nav_frame, text="GitHub", command=lambda: webbrowser.open("https://github.com/lmfrozza/AssetsNow"), fg_color="transparent", text_color="white", hover_color="#3b74c9")
link4.pack(side="left",pady=1)

#CONFIG TOOGLE

def toggle_menu_config():
    #Remove outros toggles
    install_frame.place(relx=1.5, rely=0, anchor='ne')
    api_frame.place(relx=1.5, rely=0, anchor='ne')

    if menu_frame.winfo_x() > app.winfo_width(): 
        menu_frame.place(relx=1, rely=0.08, anchor='ne')  
        
    else:
        menu_frame.place(relx=1.5, rely=0, anchor='ne')  


menu_frame = ctk.CTkFrame(app, width=300, height=600,fg_color="#303030")
menu_frame.place(relx=1.5, rely=0, anchor='ne')
menu_frame_header = ctk.CTkFrame(menu_frame, width=300, height=30, fg_color="#1b74c1")
menu_frame_header.place(relx=1.0, rely=0.0001, anchor='ne')

menu_frame_header_title = ctk.CTkLabel(menu_frame_header, text="Configurações", font=("Arial", 16))
menu_frame_header_title.place(relx=0.5, rely=0.5, anchor='center')
#INSTALL TOOGLE

def toggle_menu_Install():
    #Remove outros toggles
    menu_frame.place(relx=1.5, rely=0, anchor='ne')
    api_frame.place(relx=1.5, rely=0, anchor='ne')

    if install_frame.winfo_x() > app.winfo_width():  
        CheckList()
        install_frame.place(relx=1.0, rely=0.08, anchor='ne')  # Posiciona o frame na tela

    else:
        install_frame.place(relx=1.5, rely=0, anchor='ne')


install_frame = ctk.CTkFrame(app, width=300, height=600,fg_color="#303030")
install_frame.place(relx=1.5, rely=0, anchor='ne')  
install_frame_header = ctk.CTkFrame(install_frame, width=300, height=30, fg_color="#1b74c1")
install_frame_header.place(relx=1.0, rely=0.0001, anchor='ne')

install_frame_header_title = ctk.CTkLabel(install_frame_header, text="Instalação", font=("Arial", 16))
install_frame_header_title.place(relx=0.5, rely=0.5, anchor='center')

install_frame_Env_Button = ctk.CTkButton(install_frame, text="Instalar", command=lambda: Config_Folder_Appdata(), fg_color="#1b74c1", text_color="white", hover_color="#3b74c9")
install_frame_Env_Button.place(relx=0.5, rely=0.9,anchor="s")

#/----------------/CHELIST FOLDER\----------------\
def CheckList():
    if(Verify_Folder()):
        emoji = "✅"
    else:
        emoji = "☒"
    install_frame_checklist_1 = ctk.CTkLabel(install_frame, text=f"Folder AppData {emoji}", font=("Arial", 16))
    install_frame_checklist_1.place(relx=0.5, rely=0.2, anchor='center')
    if(Verify_Folder_userdb()):
        emoji = "✅"
    else:
        emoji = "☒"
    install_frame_checklist_2 = ctk.CTkLabel(install_frame, text=f"CSV API Keys {emoji}", font=("Arial", 16))
    install_frame_checklist_2.place(relx=0.5, rely=0.35, anchor='center')


#API KEYS TOOGLE
def toggle_menu_APIs():
    #Remove outros toggles
    install_frame.place(relx=1.5, rely=0, anchor='ne')
    menu_frame.place(relx=1.5, rely=0, anchor='ne')

    if api_frame.winfo_x() > app.winfo_width():  
        api_frame.place(relx=1.0, rely=0.08, anchor='ne')  # Posiciona o frame na tela
    else:
        api_frame.place(relx=1.5, rely=0, anchor='ne')


api_frame = ctk.CTkFrame(app, width=300, height=600,fg_color="#303030")
api_frame.place(relx=1.5, rely=0, anchor='ne')  
api_frame_header = ctk.CTkFrame(api_frame, width=300, height=30, fg_color="#1b74c1")
api_frame_header.place(relx=1.0, rely=0.0001, anchor='ne')

api_frame_header_title = ctk.CTkLabel(api_frame_header, text="Chaves de API", font=("Arial", 16))
api_frame_header_title.place(relx=0.5, rely=0.5, anchor='center')

    

#/-----------------/Interactive Menu\-----------------\
interactive_frame = ctk.CTkFrame(app, width=300, height=600,fg_color="#303030")
interactive_frame.pack(side="left")


app.mainloop()
