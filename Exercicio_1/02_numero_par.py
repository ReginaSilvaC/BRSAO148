''' 2 - Crie um programa em Python que solicite um número do usuário e informe se ele é par ou ímpar.'''

# Solicita ao usuário que digite um número
numero = int(input("Digite um número: "))

# Verifica se o número é divisível por 2 (o resto é igual a zero)
if numero % 2 == 0:
    # Se o resto da divisão for igual a zero será um número par
    print("O número é par. ")
else:
    # Caso contrário será ímpar
    print("O número é impar. ")

    ''' 
    numero = int(input) - solicita e converte a entrada para um número inteiro
    if número % 2 == 0: - verfica se o número é divisível por 2, caso for o resto será0, sendo 0 será nuúmero par.
    else(senão), número impar.
    print - mostra o resultado
    
    '''