import os
import csv

import pandas as pd

def Read_Database(db):
    user_profile = os.environ['USERPROFILE']


    caminho_arquivo = os.path.join(user_profile, "AppData", "Roaming", "AssetsNow", f"{db}.csv")
    #print(caminho_arquivo)
    try:
        # Lê o arquivo CSV
        df = pd.read_csv(caminho_arquivo)
        return df
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
        return None

def Patch_DB(db_name,db, ln, user, pword, key):
    user_profile = os.environ['USERPROFILE']
    caminho_arquivo = os.path.join(user_profile, "AppData", "Roaming", "AssetsNow", f"{db_name}.csv")
    
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

def Patch_pConfig(db, theme, cottype):
    user_profile = os.environ['USERPROFILE']
    caminho_arquivo = os.path.join(user_profile, "AppData", "Roaming", "AssetsNow", "pconfig.csv")
    db['theme'] = db['theme'].astype(object)
    db['cottype'] = db['cottype'].astype(object)
    
    if(theme):
        db.loc[0,"theme"] = theme
    if(cottype):
        db.loc[0, "cottype"] = cottype

    db.to_csv(caminho_arquivo, index=False)
    return db


if __name__ == "__main__":
    print(Read_Database("pconfig"))
    print(Patch_pConfig(
        Read_Database("pconfig"),
        "dark",
        "None"
    ))