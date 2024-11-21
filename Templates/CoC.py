import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import customtkinter as ctk
from Services.database import Database

class CC_Screen():
    @staticmethod
    def Main(frame):
        # Remove todos os widgets do frame
        for widget in frame.winfo_children():
            widget_class = widget.winfo_class() 
            widget.destroy()
            #print(f"{widget_class} removido")

        # Cria o header_frame
        header_frame = ctk.CTkFrame(frame, fg_color="#1b74c1", width=895, height=50)
        header_frame.place(relx=0.5, rely=0.05, anchor='center')

        # Cria o header_label
        header_label = ctk.CTkLabel(header_frame, text="Busca Avançada de Criptomoedas", font=("Arial", 16), text_color="#fff")
        header_label.place(relx=0.5, rely=0.5, anchor='center')  # Posiciona o label no centro do header_frame

        #//------------- Changeble Container -------------------\\
        main_frame = ctk.CTkFrame(frame, fg_color="#fff", width=895, height=490)
        main_frame.place(relx=0.5, rely=0.545, anchor='center')
if __name__ == "__main__":
    import app