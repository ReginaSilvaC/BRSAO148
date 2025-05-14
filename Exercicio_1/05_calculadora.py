'''5 - Crie um programa em Python que peça dois números e uma operação matemática (+, -, * ou /), e mostre o resultado de 
acordo com a operação escolhida.'''

# Solicita a usuário que digite o primeiro número
numero1 = float(input("Digite o primeiro número: "))
# Solicita a usuário que digite o segundo número
numero2 = float(input("Digite o segundo número: "))
# Solicita que o usuário escolha a operação
operação = input("Digite a operação (+, -, * ou /): ")
if operação == "+":
    resultado = numero1 + numero2
    print("O resultado da soma é: ", resultado)


elif operação == "-":
    resultado = numero1 - numero2
    print("O resultado da subtração é: ", resultado)

elif operação == "*":
    resultado = numero1 * numero2
    print("O resultado da multiplicação é: ", resultado)

elif operação == "/":
    # Verifica se o segundo número é diferente de zero
    if numero2 != 0:
       resultado = numero1 / numero2
       print("O resultado da divisão é: ", resultado)
    else:
        print("Erro: Divisão por ZERO não é permitida")
else:
     print("Opreação inválida")