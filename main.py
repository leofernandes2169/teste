import re
import requests

def main():
    cep = input("Informe um CEP: ")

    if not re.search(r"^([\d]{5}-[\d]{3})|([\d]{8})$", cep):
        print("Informe um CEP com o formato válido.\nExemplo: 62375-000.")
        exit()

    try:
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json")
    except:
        print("Ocorreu algum erro ao fazer a requisição.")
        exit()

    if response.status_code != 200:
        print("Informe um CEP válido.")
        exit()

    response = response.json()

    print(f"CEP: {response['cep'] or 'Indisponível'}")
    print(f"Logradouro: {response['logradouro'] or 'Indisponível'}")
    print(f"Complemento: {response['complemento'] or 'Indisponível'}")
    print(f"Bairro: {response['bairro'] or 'Indisponível'}")
    print(f"Cidade: {response['localidade'] or 'Indisponível'}")
    print(f"Estado: {response['uf'] or 'Indisponível'}")
    print(f"SIAFI: {response['siafi'] or 'Indisponível'}")
    print(f"IBGE: {response['ibge'] or 'Indisponível'}")
    print(f"GIA: {response['gia'] or 'Indisponível'}")
    print(f"DDD: {response['ddd'] or 'Indisponível'}")

if __name__ == "__main__":
    main()
