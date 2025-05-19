# Solicita o nome do aluno
aluno = input("Digite o nome do aluno: ")

# Solicita e converte a primeira nota para float (número com ponto decimal)
nota1 = float(input("Digite a primeira nota: "))

# Solicita e converte a segunda nota para float
nota2 = float(input("Digite a segunda nota: "))

# Solicita e converte a terceira nota para float
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média das três notas
media = (nota1 + nota2 + nota3) / 3

# Exibe a média com duas casas decimais
print(f"A média do(a) {aluno} é: {media:.2f}")

# Verifica se a média é maior ou igual a 7
if media >= 7:
    print("Situação: APROVADO!")  # Aprovado se a média for 7 ou mais

# Verifica se a média está entre 5 (inclusive) e menor que 7
elif media >= 5:
    print("Situação: Recuperação!")  # Em recuperação se média for entre 5 e 6.99

# Caso a média seja menor que 5
else:
    print("Situação: REPROVADO!")  # Reprovado se a média for menor que 5