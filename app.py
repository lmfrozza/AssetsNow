import customtkinter as ctk
from instalation import Config_Folder_Appdata, Verify_Folder, Verify_Folder_userdb
from database import Read_API_Database, Patch_DB
import webbrowser
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue") 


app = ctk.CTk()
app.geometry("1200x600")
app.title("AssetsNow | Facilite suas aplicações financeiras! ")

#INICIALIZA O BANCO DE DADOS
if(Verify_Folder_userdb()):
    print("Inicializando o Banco de dados...")
    db = Read_API_Database()
    print(db)
else:
    print("Falha ao iniciar o banco de dados")
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
        Patch_Forms(0)
        api_frame.place(relx=1.0, rely=0.08, anchor='ne')  # Posiciona o frame na tela
    else:
        api_frame.place(relx=1.5, rely=0, anchor='ne')


api_frame = ctk.CTkFrame(app, width=300, height=600,fg_color="#303030")
api_frame.place(relx=1.5, rely=0, anchor='ne')  
api_frame_header = ctk.CTkFrame(api_frame, width=300, height=30, fg_color="#1b74c1")
api_frame_header.place(relx=1.0, rely=0.0001, anchor='ne')

api_frame_header_title = ctk.CTkLabel(api_frame_header, text="Chaves de API", font=("Arial", 16))
api_frame_header_title.place(relx=0.5, rely=0.5, anchor='center')





#/----------------/PATCH MENU API KEYS\----------------\
def Patch_Forms(row):
    # Remove botões antigos, se existirem
    for widget in api_frame.winfo_children():
        if isinstance(widget, ctk.CTkButton) and widget not in [api_frame]:
            widget.destroy()
        if isinstance(widget, ctk.CTkLabel) and widget not in [api_frame]:
            widget.destroy()

    pages = [0, 1, 2,]
    if row in pages:
        #⬅️
        #➡️
        if row != 0:
            api_frame_Back_Button = ctk.CTkButton(api_frame, text="←", width=50, command=lambda: toggle_Forms_API(row - 1), fg_color="#1b74c1", text_color="white", hover_color="#3b74c9")
            api_frame_Back_Button.place(relx=0.2, rely=0.07, anchor="ne")
        if row != 2:
            api_frame_Next_Button = ctk.CTkButton(api_frame, text="→", width=50, command=lambda: toggle_Forms_API(row + 1), fg_color="#1b74c1", text_color="white", hover_color="#3b74c9")
            api_frame_Next_Button.place(relx=0.8, rely=0.07, anchor="nw")
        if(Verify_Folder_userdb):
            API = Read_API_Database().loc[row, "API"]
            USER = Read_API_Database().loc[row, "User"]
            SENHA = Read_API_Database().loc[row, "Senha"]
            CHAVE = Read_API_Database().loc[row, "Chave"]
            api_frame_Api_Name = ctk.CTkLabel(api_frame, text=API, font=("Arial", 16))
            api_frame_Api_Name.place(relx=0.5, rely=0.09, anchor='center')

            entry_user_label= (ctk.CTkLabel(api_frame, text="Usuário:", font=("Arial", 16))).place(relx=0.36, rely=0.2, anchor='e')
            entry_user = ctk.CTkEntry(api_frame, width=200, placeholder_text=USER)
            entry_user.place(relx=0.5, rely=0.25, anchor='center')

            entry_pword_label= (ctk.CTkLabel(api_frame, text="Senha:", font=("Arial", 16))).place(relx=0.32, rely=0.40, anchor='e')
            entry_pword = ctk.CTkEntry(api_frame, width=200, placeholder_text=SENHA)
            entry_pword.place(relx=0.5, rely=0.45, anchor='center')

            entry_key_label= (ctk.CTkLabel(api_frame, text="Chave:", font=("Arial", 16))).place(relx=0.32, rely=0.60, anchor='e')
            entry_key = ctk.CTkEntry(api_frame, width=200, placeholder_text=CHAVE)
            entry_key.place(relx=0.5, rely=0.65, anchor='center')
            
        api_frame_Patch_Button = ctk.CTkButton(api_frame, text="Alterar", command=lambda: Patch_Row(), fg_color="#1b74c1", text_color="white", hover_color="#3b74c9")
        api_frame_Patch_Button.place(relx=0.5, rely=0.9,anchor="s")
        def Patch_Row():
            Patch_User = str(entry_user.get())
            Patch_Senha = str(entry_pword.get())
            Patch_Chave = str(entry_key.get())
            print(Patch_DB(
                Read_API_Database(), 
                row,
                Patch_User, 
                Patch_Senha, 
                Patch_Chave
            ))
    else:
        api_frame_error = ctk.CTkLabel(api_frame, text="Ocorreu um erro ao carregar o banco!", font=("Arial", 16))
        api_frame_error.place(relx=0.5, rely=0.5, anchor='center')

def toggle_Forms_API(row):
    # Remove outros toggles
    install_frame.place(relx=1.5, rely=0, anchor='ne')
    menu_frame.place(relx=1.5, rely=0, anchor='ne')

    # Reposiciona o api_frame para fora da tela antes de chamar Patch_Forms
    api_frame.place(relx=1.5, rely=0, anchor='ne')
    
    Patch_Forms(row)
        
    # Posiciona o frame na tela
    api_frame.place(relx=1.0, rely=0.08, anchor='ne')


    

    

#/-----------------/Interactive Menu\-----------------\
interactive_frame = ctk.CTkFrame(app, width=300, height=600,fg_color="#303030")
interactive_frame.pack(side="left")


app.mainloop()
