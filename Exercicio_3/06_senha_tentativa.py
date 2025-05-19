# Define a senha correta para validação
senha_correta = "123456789"

# Contador de tentativas inicializado em zero
tentativas = 0

# Loop infinito que continuará enquanto não alcançar limite ou senha correta
while True:
    # Solicita que o usuário digite a senha
    senha = input("Digite a senha: ")
    
    # Incrementa o contador de tentativas a cada entrada
    tentativas += 1
    
    # Verifica se a senha digitada está correta
    if senha == senha_correta:
        print("Acesso permitido.")  # Mensagem de sucesso
        break  # Sai do loop, pois senha está correta
    
    else:
        print("Senha incorreta!")  # Mensagem para senha errada
    
    # Verifica se já foram feitas 3 tentativas
    if tentativas == 3:
        print("Número de tentativas excedido, ACESSO NEGADO!")  # Bloqueio após 3 tentativas
        break  # Sai do loop, bloqueando acesso