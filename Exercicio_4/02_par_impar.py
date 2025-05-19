''' 2 - Crie um programa que solicite ao usuário que insira números inteiros. O programa deve continuar solicitando números até que o usuário digite 'fim'. Para cada número inserido, o programa deve informar se é par ou ímpar. Se o usuário inserir algo que não seja um número inteiro, 
o programa deve informar o erro e continuar. No final, o programa deve exibir a quantidade de números pares e ímpares inseridos.'''

quantidade_pares = 0  # Inicializa o contador de números pares
quantidade_impares = 0  # Inicializa o contador de números ímpares

while True:
    entrada = input("Digite um número inteiro (ou 'Fim' para encerrar): ")  # Solicita um número ou 'Fim' para encerrar
    
    if entrada.lower() == 'fim':  # Verifica se o usuário digitou 'fim' (ignorando maiúsculas/minúsculas)
        break  # Encerra o loop se for 'fim'

    try:
        numero = int(entrada)  # Tenta converter a entrada para número inteiro
        if numero % 2 == 0:  # Verifica se o número é par
            print("O número é PAR.")  # Informa que o número é par
            quantidade_pares += 1  # Incrementa o contador de pares
        else:
            print("O número é ÍMPAR.")  # Informa que o número é ímpar
            quantidade_impares += 1  # Incrementa o contador de ímpares
    except ValueError:
        print("Erro: Você deve digitar um número inteiro ou 'FIM'.")  # Mensagem de erro para entradas inválidas

# Exibe a quantidade total de pares e ímpares digitados
print(f"Quantidade de números PARES: {quantidade_pares}")
print(f"Quantidade de números ÍMPARES: {quantidade_impares}")



