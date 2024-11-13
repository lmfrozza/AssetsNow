import customtkinter as ctk
import webbrowser
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue") 


def on_link_click(url):
    print(f"Abrindo: {url}")

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

link2 = ctk.CTkButton(header_nav_frame, text="Chaves APIs", command=lambda: on_link_click("https://www.exemplo1.com"), fg_color="transparent", text_color="white", hover_color="#3b74c9")
link2.pack(side="left",pady=1)


link3 = ctk.CTkButton(header_nav_frame, text="Instalação", command=lambda: on_link_click("https://www.exemplo1.com"), fg_color="transparent", text_color="white", hover_color="#3b74c9")
link3.pack(side="left",pady=1)


link4 = ctk.CTkButton(header_nav_frame, text="GitHub", command=lambda: webbrowser.open("https://github.com/lmfrozza/AssetsNow"), fg_color="transparent", text_color="white", hover_color="#3b74c9")
link4.pack(side="left",pady=1)

#CONFIG TOOGLE

def toggle_menu_config():
    print(f"Header:{header_frame.winfo_height()}")
    if menu_frame.winfo_x() > app.winfo_width():  # Se o menu estiver fora da tela
        menu_frame.place(relx=1, rely=0, anchor='ne')  # Move para dentro da tela
        menu_frame.pack(side="right",pady=18)
    else:
        menu_frame.place(relx=1.2, rely=0, anchor='ne')  # Move para fora da tela


menu_frame = ctk.CTkFrame(app, width=200, height=app.winfo_height(), fg_color="#FFF")
menu_frame.place(relx=1.2, rely=0, anchor='ne')  # Inicialmente fora da tela


app.mainloop()