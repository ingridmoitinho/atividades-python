"""

1- Gerador de Senhas Seguras  
Crie um programa que gera senhas aleatórias com letras, números e caracteres especiais. Siga as instruções abaixo:

* Solicite ao usuário o tamanho da senha desejada (por exemplo: 8, 12, 16 caracteres).  
* A senha gerada deve conter letras maiúsculas, minúsculas, números e símbolos (ex: !@#$%&*).  
* Exiba a senha gerada ao final do programa.  

Dica: Use os módulos `random` e `string` para gerar os caracteres aleatórios.
"""
import random
import string

t = int(input("Tamanho da senha (mínimo 6): "))
if t < 6:
    print("Tamanho mínimo é 6.")
else:
    tipos = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice("!@#$%&*")
    ]
    outros = random.choices(string.ascii_letters + string.digits + "!@#$%&*", k=t-4)
    senha = ''.join(random.sample(tipos + outros, t))
    print("Senha gerada:", senha)
