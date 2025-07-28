"""
3- Consulta de CEP  
Desenvolva um programa que consulta dados de endereço a partir de um CEP brasileiro. Siga os passos abaixo:

* Solicite ao usuário que digite um CEP (apenas números, sem traço).  
* Acesse a API pública do ViaCEP: "https://viacep.com.br/ws/{cep}/json/".  
* Exiba as seguintes informações: logradouro, bairro, cidade, estado e o próprio CEP.  
* Caso o CEP não exista ou haja erro, informe isso de forma clara ao usuário.  

Dica: Use o módulo `requests` e trate exceções com `try/except`.
"""
import requests

cep = input("Digite o CEP (somente números): ")

try:
    resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    dados = resposta.json()

    if "erro" in dados:
        print("CEP não encontrado.")
    else:
        print("Logradouro:", dados['logradouro'])
        print("Bairro:", dados['bairro'])
        print("Cidade:", dados['localidade'])
        print("Estado:", dados['uf'])
        print("CEP:", dados['cep'])

except requests.exceptions.RequestException:
    print("Erro na conexão com a API.")
