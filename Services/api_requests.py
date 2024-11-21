import sys
import os

# Adiciona o diretório pai ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import requests
from Services.database import Database

class ExancheRate_ApiCall():
    @staticmethod
    def ExchangeRateApi_latest_all(moeda):
        CHAVE = Database.Read_Database("apikeys").loc[0, "Chave"]

        response = requests.get(f"https://v6.exchangerate-api.com/v6/{CHAVE}/latest/{moeda}")
        
        # Verifica se a requisição foi bem-sucedida
        if response.status_code == 200:
            data = response.json()  # Converte a resposta para JSON
            return data['conversion_rates']  # Acessa o valor desejado
        else:
            print("Erro ao acessar a API:", response.status_code)
            return None
    @staticmethod
    def ExchangeRateApi_latest_Conversion(moeda1, moeda2):
        CHAVE = Database.Read_Database("apikeys").loc[0, "Chave"]

        response = requests.get(f"https://v6.exchangerate-api.com/v6/{CHAVE}/latest/{moeda1}")
        
        # Verifica se a requisição foi bem-sucedida
        if response.status_code == 200:
            data = response.json()  # Converte a resposta para JSON
            return data['conversion_rates'][moeda2]  # Acessa o valor desejado
        else:
            print("Erro ao acessar a API:", response.status_code)
            return None

if __name__ == "__main__":
    print(ExancheRate_ApiCall.ExchangeRateApi_latest_all("USD"))
    print(ExancheRate_ApiCall.ExchangeRateApi_latest_Conversion("USD","BRL"))