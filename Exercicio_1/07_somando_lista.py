''' 7 - Crie um programa que contenha uma lista com números e calcule a soma total desses números usando um laço for.'''

# Cria uma lista com alguns números
numeros = [5, 8, 3, 10, 2]

# Inicializa a variável que vai guardar a soma
soma = 0

# Percorre cada número da lista
for numero in numeros:
    # Adiciona o número atual à soma
    soma += numero

# Mostra o resultado final da soma
print("A soma total é:", soma)
