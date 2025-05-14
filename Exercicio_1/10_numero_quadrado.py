def quadrado(numero):
    return numero ** 2

# Solicita ao usuário que digite um número
entrada = input("Digite um número: ")

# Converte a entrada para número (float permite decimais)
numero = float(entrada)

# Chama a função e mostra o resultado
resultado = quadrado(numero)
print(f"O quadrado de {numero} é {resultado}")