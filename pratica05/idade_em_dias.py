"""
4- Calculadora de Idade em Dias
Crie um programa que calcula a idade aproximada de uma pessoa em dias. Para isso:

* Solicite o ano de nascimento da pessoa.  
* Considere o ano atual automaticamente.  
* Calcule a idade em anos e transforme em dias (desconsidere anos bissextos).  
* Exiba o resultado final.
"""
from datetime import datetime

def calcular_idade_em_dias(ano_nascimento):
    ano_atual = datetime.now().year
    idade_em_anos = ano_atual - ano_nascimento
    return idade_em_anos * 365

ano_nascimento = int(input("Digite o ano de nascimento: "))
idade_em_dias = calcular_idade_em_dias(ano_nascimento)
print(f"Idade em dias: {idade_em_dias} dias")
