import os
import csv

#Cria o e configura o Folder
def Config_Folder_Appdata():
    user_profile = os.environ['USERPROFILE']


    appdata_folder = os.path.join(user_profile, "AppData", "Roaming", "AssetsNow")
    print(Verify_Folder())

    if(not Verify_Folder()):
        os.makedirs(appdata_folder)  
        print(f"Pasta '{appdata_folder}' criada com sucesso!")
    else:
        print(f"A pasta '{appdata_folder}' já existe.")

    if(Verify_Folder_userdb):
        dados = [
        ["API", "User", "Senha", "Chave"],
        ["ExchangeRate-API","","",""]
        ]   

        # Nome do arquivo CSV
        nome_arquivo = f"{appdata_folder}/apikeys.csv"

        # Abrindo o arquivo em modo de escrita ('w')
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)
            
            # Escrevendo os dados no arquivo CSV
            escritor_csv.writerows(dados)

        print(f"Arquivo '{nome_arquivo}' criado com sucesso!")
        


#Verifica se o Folder existe
def Verify_Folder():
    user_profile = os.environ['USERPROFILE']


    appdata_folder = os.path.join(user_profile, "AppData", "Roaming", "AssetsNow")


    if not os.path.exists(appdata_folder):
        return False
    else:
        return True
    
def Verify_Folder_userdb():
    user_profile = os.environ['USERPROFILE']


    appdata_folder = os.path.join(user_profile, "AppData", "Roaming", "AssetsNow", "apikeys.csv")


    if not os.path.exists(appdata_folder):
        return False
    else:
        return True
    


