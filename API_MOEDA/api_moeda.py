import json
import requests
import json


chamada = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")

chamada_conv = chamada.json()
cotacao_dolar = chamada_conv["USDBRL"]  # pegando apenas cotação do dolar

# print(cotacao_dolar)
print("O Dólar está custando: R${} ".format(cotacao_dolar["bid"]))
