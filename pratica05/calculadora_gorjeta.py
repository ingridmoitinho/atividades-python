"""
1- Calculadora de Gorjeta
Crie um programa que calcula o valor da gorjeta a partir do total da conta e da porcentagem escolhida. Use as instruções abaixo:

* Defina o valor da conta (ex: R$ 100,00).  
* Informe a porcentagem da gorjeta (ex: 10%, 15%, 20%).  
* O programa deve calcular o valor correspondente e exibir o resultado com duas casas decimais.
"""
def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    return round(valor_conta * (porcentagem_gorjeta / 100), 2)

valor = float(input("Digite o valor da conta: R$ "))
porcentagem = float(input("Digite a porcentagem da gorjeta: "))
gorjeta = calcular_gorjeta(valor, porcentagem)
total_a_pagar = round(valor + gorjeta, 2)

print(f"Valor da gorjeta: R$ {gorjeta:.2f}")
print(f"Valor total a pagar: R$ {total_a_pagar:.2f}")
