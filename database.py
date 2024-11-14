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
