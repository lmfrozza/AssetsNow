import os
import csv

import pandas as pd

def Read_API_Database():
    user_profile = os.environ['USERPROFILE']


    caminho_arquivo = os.path.join(user_profile, "AppData", "Roaming", "AssetsNow", "apikeys.csv")
    try:
        # Lê o arquivo CSV
        df = pd.read_csv(caminho_arquivo)
        return df
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
        return None

def Patch_DB(db, ln, user, pword, key):
    user_profile = os.environ['USERPROFILE']
    caminho_arquivo = os.path.join(user_profile, "AppData", "Roaming", "AssetsNow", "apikeys.csv")
    
    db['User'] = db['User'].astype(object)
    db['Senha'] = db['Senha'].astype(object)
    db['Chave'] = db['Chave'].astype(object)

    if(user):
        print("user alterado")
        db.loc[ln, "User"] = user
    if(pword):
        print("Senha alterada")
        db.loc[ln , "Senha"] = pword
    if(key):
        print("Chave alterada")
        db.loc[ln, "Chave"] = key
    
    db.to_csv(caminho_arquivo, index=False)
    return db
    

if __name__ == "__main__":
    print(Read_API_Database())
    print(Patch_DB(
            Read_API_Database(), 
            2,
            "Nome do usuário3", 
            "Senha do usuário3", 
            "Chave de usuário3"
        ))
    #