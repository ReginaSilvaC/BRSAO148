''' 6 - Crie um programa que receba um número do usuário e diga se ele é positivo, negativo ou igual a zero'''

# Pede um número ao usuário e converte para float
numero = float(input("Digite um número: "))
# Verifica se o número é maior que zero
if numero > 0:
     # Se for maior que zero, imprime que o número é positivo
    print("O número é positivo")
# Verifica se o número é menor que zero
elif numero < 0:
# Se for menor que zero, imprime que o número é negativo
    print("O número é negativo")
# Se o número não for maior nem menor que zero, então é igual a zero
else: 
     # Imprime que o número é zero
    print("O número é zero")
