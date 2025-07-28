"""
2- Gerador de Usuário Aleatório  
Crie um programa que acessa uma API pública e exibe informações de um usuário fictício. Para isso:

* Use a API pública "https://randomuser.me/api/" para obter dados aleatórios.  
* Mostre na tela: nome completo, e-mail e país do usuário.  
* O programa deve tratar possíveis erros de conexão ou falha na API.  

Dica: Utilize o módulo `requests` para fazer a requisição e o método `.json()` para acessar os dados.
"""
import requests

response = requests.get("https://randomuser.me/api/")

if response.status_code == 200:
    dados = response.json()['results'][0]
    nome = f"{dados['name']['first']} {dados['name']['last']}"
    email = dados['email']
    pais = dados['location']['country']
    print(f"Nome: {nome}\nEmail: {email}\nPaís: {pais}")
else:
    print("Erro ao obter dados do usuário.")
