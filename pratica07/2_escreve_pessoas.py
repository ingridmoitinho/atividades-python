"""
2- Escrita de Arquivo CSV  
Crie um programa que escreve dados de pessoas (nome, idade e cidade) em um arquivo CSV. Para isso:

* Crie uma lista de listas com dados fictícios de pelo menos três pessoas.  
* Solicite ao usuário o nome do arquivo CSV onde os dados serão salvos.  
* Escreva os dados usando o módulo `csv`, com cabeçalhos apropriados.  
* Confirme a gravação exibindo uma mensagem com o nome do arquivo.  
* Trate possíveis erros de escrita de arquivo.

Dica: Use `csv.writer()` para escrever os dados linha por linha.
"""
import csv

pessoas = [
    ["Ingrid", 30, "Bahia"],
    ["Daniela", 35, "Sergipe"],
    ["Fernanda", 22, "Recife"]
]

arquivo = input("Digite o nome do arquivo CSV para salvar os dados (ex: pessoas.csv): ")

try:
    with open(arquivo, mode='w', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f)
        escritor.writerow(["Nome", "Idade", "Cidade"])  
        escritor.writerows(pessoas) 
    print(f"Dados salvos com sucesso no arquivo '{arquivo}'.")
except Exception as erro:
    print(f"Ocorreu um erro ao salvar o arquivo: {erro}")
