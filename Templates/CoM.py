import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import customtkinter as ctk
from Services.database import Database

class CM_Screen():
    @staticmethod
    def Main(frame):
        
        for widget in frame.winfo_children():
            widget_class = widget.winfo_class() 
            widget.destroy()
            #print(f"{widget_class} removido")

        
        header_frame = ctk.CTkFrame(frame, fg_color="#1b74c1", width=895, height=50)
        header_frame.place(relx=0.5, rely=0.05, anchor='center')

        
        header_label = ctk.CTkLabel(header_frame, text="Busca Avançada de cotações", font=("Arial", 16), text_color="#fff")
        header_label.place(relx=0.5, rely=0.5, anchor='center')

        #//------------- Changeble Container -------------------\\
        main_frame = ctk.CTkFrame(frame, fg_color=None, width=895, height=490)
        main_frame.place(relx=0.5, rely=0.545, anchor='center')

        if(Database.Read_Database("pconfig").loc[0,'cottype'] == "Mapeadas"):
            print("Abrindo com Mapeamento")
        elif(Database.Read_Database("pconfig").loc[0,'cottype'] == "Código de moeda"):
            print("abrindo por código de moeda")
        else:
            print("erro")
if __name__ == "__main__":
    import app