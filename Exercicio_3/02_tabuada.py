# Solicita ao usuário que digite um número inteiro para ver a tabuada
numero = int(input("Digite um número para ver a tabuada: "))

# Exibe um cabeçalho informando qual tabuada será mostrada
print(f"\nTabuada do {numero}:")

# Estrutura de repetição 'for' que vai de 1 até 10 (inclusive)
for i in range(1, 11):
    # Calcula o resultado da multiplicação
    resultado = numero * i
    
    # Exibe a operação e o resultado formatados de forma clara
    print(f"{numero} x {i:2} = {resultado}")

# Mensagem final para indicar que o programa terminou
print("\nFim da tabuada.")