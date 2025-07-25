"""
3- Calculadora de Desconto em Produto
Desenvolva um programa que aplica um desconto sobre o preço de um produto. O programa deve:

* Solicitar o preço original do produto.  
* Solicitar o percentual de desconto desejado.  
* Calcular e exibir o preço final com desconto, arredondado para duas casas decimais.
"""
def aplicar_desconto(preco, desconto_percentual):
    return round(preco * (1 - desconto_percentual / 100), 2)

preco_original = float(input("Digite o preço do produto: R$ "))
desconto = float(input("Digite o percentual de desconto: "))
preco_final = aplicar_desconto(preco_original, desconto)
print(f"Preço com desconto: R$ {preco_final:.2f}")
