''' Desenvolva uma calculadora em Python que realize as quatro operações básicas (adição, subtração, multiplicação e divisão) entre dois números. A calculadora deve ser capaz de lidar com diversos tipos de erros de entrada e operação. Siga as especificações abaixo:

A calculadora deve solicitar ao usuário que insira dois números e uma operação.
As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).
O programa deve continuar solicitando entradas até que uma operação válida seja concluída.
Trate os seguintes erros:
Entrada inválida (não numérica) para os números
Divisão por zero
Operação inválida
Use try/except para capturar e tratar os erros apropriadamente.
Após cada erro, o programa deve informar o usuário sobre o erro e solicitar nova entrada.
Quando uma operação é concluída com sucesso, exiba o resultado e encerre o programa'''


while True:
    try:
        # Solicita o primeiro número
        num1 = float(input("Digite o primeiro número: "))
        
        # Solicita o segundo número
        num2 = float(input("Digite o segundo número: "))
        
        # Solicita a operação
        operacao = input("Digite a operação (+, -, *, /): ").strip()

        # Verifica se a operação é válida
        if operacao not in ['+', '-', '*', '/']:
            print("Erro: Operação inválida. Use apenas +, -, * ou /.")
            continue

        # Verifica divisão por zero
        if operacao == '/' and num2 == 0:
            print("Erro: Divisão por zero não é permitida.")
            continue

        # Realiza a operação com base na entrada
        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            resultado = num1 / num2

        # Exibe o resultado
        print(f"Resultado: {num1} {operacao} {num2} = {resultado}")
        break  # Encerra o programa após uma operação bem-sucedida

    except ValueError:
        print("Erro: Você deve digitar números válidos.")