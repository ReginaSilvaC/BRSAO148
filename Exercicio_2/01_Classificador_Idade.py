'''1- Classificador de Idade
Crie um programa que solicite a idade do usuário e classifique-o 
em uma das seguintes categorias: 

*Criança (0-12 anos), 
*Adolescente (13-17 anos), 
*Adulto (18-59 anos) ou 
*Idoso (60 anos ou mais).'''

# Solicita ao usuário que digite sua idade e converte o valor para inteiro
idade = int(input("Digite sua idade: "))

# Verifica se a idade está entre 0 e 12 anos (inclusive)
if idade >= 0 and idade <= 12:
    print("Classificação: Criança")  # Imprime se for criança

# Verifica se a idade está entre 13 e 17 anos (inclusive)
elif idade >= 13 and idade <= 17:
    print("Classificação: Adolescente")  # Imprime se for adolescente

# Verifica se a idade está entre 18 e 59 anos (inclusive)
elif idade >= 18 and idade <= 59:
    print("Classificação: Adulto")  # Imprime se for adulto

# Verifica se a idade é 60 anos ou mais
elif idade >= 60:
    print("Classificação: Idoso")  # Imprime se for idoso

# Caso nenhuma das condições anteriores seja atendida (idade negativa, por exemplo)
else:
    print("Idade inválida!")  # Imprime mensagem de erro