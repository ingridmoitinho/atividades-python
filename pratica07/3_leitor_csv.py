"""
3- Leitura de Arquivo CSV  
Desenvolva um programa que lê os dados de um arquivo CSV e imprime cada linha na tela. Para isso:

* Solicite ao usuário o nome do arquivo CSV a ser lido.  
* Utilize o módulo `csv` para abrir o arquivo e ler os dados.  
* Exiba cada linha completa como uma lista.  
* Trate erros como arquivo inexistente ou problemas na leitura.

Dica: Use `csv.reader()` para ler e percorrer as linhas do arquivo.
"""
import csv

arquivo = input("Digite o nome do arquivo CSV a ser lido (ex: produtos.csv, pessoas.csv): ")

try:
    with open(arquivo, mode='r', encoding='utf-8') as f:
        leitor = csv.reader(f)
        for linha in leitor:
            print(linha)
except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")
except Exception as erro:
    print(f"Erro ao ler o arquivo: {erro}")
