"""
4- Leitura e Escrita de Arquivo JSON  
Desenvolva um programa que cria um dicionário com dados de uma pessoa e salva esses dados em um arquivo JSON. Em seguida, o programa deve ler o mesmo arquivo e exibir o conteúdo. Para isso:

* Crie um dicionário com pelo menos três campos (ex: nome, idade, cidade).  
* Solicite ao usuário o nome do arquivo JSON.  
* Salve os dados no arquivo usando o módulo `json`.  
* Após salvar, leia o mesmo arquivo e imprima os dados carregados.  
* Trate possíveis erros como ausência do arquivo ou problemas na escrita.

Dica: Use `json.dump()` para escrever e `json.load()` para ler o arquivo.
"""
import json

pessoa = {
    "nome": "Fernanda",
    "idade": 27,
    "cidade": "Recife"
}

arquivo = input("Digite o nome do arquivo JSON para salvar os dados (ex: pessoa.json): ")

try:
    # Escrita 
    with open(arquivo, mode='w', encoding='utf-8') as f:
        json.dump(pessoa, f, ensure_ascii=False, indent=4)
    print(f"Dados salvos com sucesso em '{arquivo}'.")

    # Leitura 
    with open(arquivo, mode='r', encoding='utf-8') as f:
        dados_lidos = json.load(f)
    print("\nDados carregados do arquivo:")
    print(dados_lidos)

except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")
except json.JSONDecodeError:
    print("Erro: O conteúdo do arquivo JSON é inválido.")
except Exception as erro:
    print(f"Ocorreu um erro: {erro}")
