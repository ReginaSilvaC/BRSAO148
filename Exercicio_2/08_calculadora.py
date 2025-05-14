# Solicita ao usuário o primeiro número e converte para float
num1 = float(input("Digite o primeiro número: "))

# Solicita ao usuário o segundo número e converte para float
num2 = float(input("Digite o segundo número: "))

# Solicita a operação desejada (+, -, *, /)
operacao = input("Digite a operação a ser realizada (+, -, *, /): ")

# Verifica se a operação é adição
if operacao == "+":
    resultado = num1 + num2  # Realiza a soma
    print(f"O resultado de {num1} + {num2} é: {resultado}")  # Exibe o resultado

# Verifica se a operação é subtração
elif operacao == "-":
    resultado = num1 - num2  # Realiza a subtração
    print(f"O resultado de {num1} - {num2} é: {resultado}")  # Exibe o resultado

# Verifica se a operação é multiplicação
elif operacao == "*":
    resultado = num1 * num2  # Realiza a multiplicação
    print(f"O resultado de {num1} * {num2} é: {resultado}")  # Exibe o resultado

# Verifica se a operação é divisão
elif operacao == "/":
    if num2 != 0:  # Verifica se o divisor não é zero
        resultado = num1 / num2  # Realiza a divisão
       
        print(f"O resultado de {num1} / {num2} é: {resultado}")  # Exibe o resultado
    else:
        # Caso o divisor seja zero, exibe mensagem de erro
        print("Erro!!! divisão por zero não permitida.")

# Caso a operação não seja reconhecida
else:
    print("Operação inválida.")