"""
4- Conversor de Moedas (para Reais - BRL)  
Crie um programa que mostra a cotação atual de moedas estrangeiras em relação ao Real. O programa deve:

* Solicitar ao usuário o código da moeda estrangeira (ex: USD, EUR, GBP).  
* Acessar a API: "https://economia.awesomeapi.com.br/last/{moeda}-BRL".  
* Exibir a cotação atual, o valor máximo, o valor mínimo e a data/hora da última atualização.  
* Informar ao usuário se o código da moeda for inválido ou houver falha na conexão.  

Dica: A conversão da data/hora pode ser feita com o módulo `datetime`.
"""
import requests

moeda = input("Digite o código da moeda estrangeira (ex: USD, EUR, GBP): ").upper()
url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
try:
    resposta = requests.get(url)
    resposta.raise_for_status()
    dados = resposta.json()
    if "error" in dados:
        print("Código da moeda inválido.")
    else:
        cotacao = dados[f"{moeda}BRL"]
        print(f"Cotação atual de {moeda} para BRL: R$ {cotacao['bid']:.4f}")
        print(f"Valor máximo: R$ {cotacao['high']:.4f}")
        print(f"Valor mínimo: R$ {cotacao['low']:.4f}")
        print(f"Data da última atualização: {cotacao['create_date']}")
except requests.RequestException as e:
    print("Erro ao acessar a API:", e)
