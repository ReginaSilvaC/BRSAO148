import random  # Importa o módulo random para gerar números aleatórios

# Gera um número aleatório entre 1 e 10 que o usuário deverá adivinhar
numero_secreto = random.randint(1, 10)

# Inicializa a variável que conta o número de tentativas feitas pelo usuário
tentativas = 0

# Mensagem de boas-vindas ao jogador
print("Bem-vindo ao Jogo da Adivinhação!")
print("Tente adivinhar o número entre 1 e 10.")

# Loop infinito que só termina quando o usuário acertar o número secreto
while True:
    # Solicita ao usuário que digite seu palpite e converte para número inteiro
    palpite = int(input("Digite seu palpite: "))
    
    # Incrementa o contador de tentativas a cada palpite
    tentativas += 1

    # Verifica se o palpite está correto
    if palpite == numero_secreto:
        # Mensagem de sucesso com o número de tentativas feitas
        print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativa(s)!")
        break  # Sai do loop porque o jogo acabou
    elif palpite < numero_secreto:
        # Dica para o usuário, indicando que o palpite foi baixo demais
        print("Muito baixo! Tente novamente.")
    else:
        # Dica para o usuário, indicando que o palpite foi alto demais
        print("Muito alto! Tente novamente.")