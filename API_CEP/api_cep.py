import requests

opcao = ""


while opcao != "nao":
    entrada = input("digite o CEP: ")
    chamada = requests.get("https://viacep.com.br/ws/{}/json/".format(entrada))
    resultado = chamada.json()
    print("CEP: {}".format(resultado["cep"]))
    print("Logradouro: {}".format(resultado["logradouro"]))
    print("Complemento(se houver): {}".format(resultado["complemento"]))
    print("Bairro: {}".format(resultado["bairro"]))
    print("Localidade: {}".format(resultado["localidade"]))
    print("UF: {}".format(resultado["uf"]))

    print("______________________________________")
    print("digita 'sim' ou 'nao' ")

    opcao = input("Deseja buscar mais algum CEP? ")
    if opcao != "sim":
        print("programa encerrado!")
