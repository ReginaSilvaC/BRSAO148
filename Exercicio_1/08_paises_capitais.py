# Dicionário com países e suas respectivas capitais
capitais = {
    "Brasil": "Brasília",
    "Japão": "Tóquio",
    "Canadá": "Ottawa",
    "Argentina": "Buenos Aires",
    "Alemanha": "Berlim"
}

# Solicita ao usuário que informe o nome de um país
pais = input("Por favor, digite o nome de um país: ")

# Verifica se o país está presente no dicionário
if pais in capitais:
    # Exibe a capital correspondente de forma formal
    print(f"A capital do país {pais} é {capitais[pais]}.")
else:
    # Mensagem para caso o país não esteja no dicionário
    print("Desculpe, o país informado não consta em nossa base de dados.")
