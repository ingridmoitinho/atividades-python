"""
3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""

def converter_temperatura():   
    temperatura = float(input("Digite a temperatura: "))
    origem = input("Informe a unidade de origem (C para Celsius, F para Fahrenheit, K para Kelvin): ").upper()
    destino = input("Informe a unidade de destino (C para Celsius, F para Fahrenheit, K para Kelvin): ").upper()
    
    if origem == 'C':
        if destino == 'F':
            resultado = (temperatura * 9/5) + 32
            print(f"{temperatura}°C é igual a {round(resultado, 2)}°F")
        elif destino == 'K':
            resultado = temperatura + 273.15
            print(f"{temperatura}°C é igual a {round(resultado, 2)} K")
        else:
            print("Unidade de destino inválida.")
    
    elif origem == 'F':
        if destino == 'C':
            resultado = (temperatura - 32) * 5/9
            print(f"{temperatura}°F é igual a {round(resultado, 2)}°C")
        elif destino == 'K':
            resultado = (temperatura - 32) * 5/9 + 273.15
            print(f"{temperatura}°F é igual a {round(resultado, 2)} K")
        else:
            print("Unidade de destino inválida.")
    
    elif origem == 'K':
        if destino == 'C':
            resultado = temperatura - 273.15
            print(f"{temperatura}K é igual a {round(resultado, 2)}°C")
        elif destino == 'F':
            resultado = (temperatura - 273.15) * 9/5 + 32
            print(f"{temperatura}K é igual a {round(resultado, 2)}°F")
        else:
            print("Unidade de destino inválida.")
    
    else:
        print("Unidade de origem inválida.")

converter_temperatura()
