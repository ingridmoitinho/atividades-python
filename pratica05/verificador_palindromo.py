"""
2- Verificador de Palíndromos
Crie um programa que verifica se uma palavra ou frase é um palíndromo, ou seja, se pode ser lida da mesma forma de trás para frente, desconsiderando espaços, acentos e pontuação. Para isso:

*Solicite ao usuário uma palavra ou frase.
*Desconsidere letras maiúsculas, espaços e sinais de pontuação.
*Verifique se a frase é um palíndromo.
*Exiba "Sim" se for palíndromo ou "Não" se não for.

Exemplo: A frase "A cara rajada da jararaca" deve ser reconhecida como um palíndromo.
"""
import re

def eh_palindromo(frase):   
    frase = re.sub(r'[\W_]+', '', frase.lower())    
    return frase == frase[::-1]

entrada = input("Digite uma palavra ou frase: ")
if eh_palindromo(entrada):
    print("Sim, é um palíndromo.")
else:
    print("Não, não é um palíndromo.")
