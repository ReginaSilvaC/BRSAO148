# Define a senha correta que o usuário deve digitar
senha_correta = "123456"

# Loop infinito que vai continuar pedindo a senha até a correta ser digitada
while True:
    # Pede ao usuário para digitar a senha
    senha = input("Digite a senha: ")
    
    # Verifica se a senha digitada é igual à senha correta
    if senha == senha_correta:
        print("Acesso permitido!")  # Mensagem de sucesso
        break  # Sai do loop quando a senha estiver correta
    else:
        print("Senha incorreta. Tente novamente.")  # Mensagem de erro se a senha estiver errada