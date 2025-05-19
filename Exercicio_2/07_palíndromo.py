'''7- Verificador de Palíndromo
Enunciado:
Crie um programa que solicite uma palavra e verifique se ela é um palíndromo (ou seja, se pode ser lida da mesma forma de trás para frente).

"Socorram-me, subi no onibus em Marrocos" e "A grama e amarga". 
'''

import re  # Importa o módulo 're' (expressões regulares) para manipulação de texto

# Solicita ao usuário que insira uma palavra ou frase
palavra = input("Insira uma palavra ou uma frase: ")

# Remove todos os caracteres que não sejam letras ou números e converte para minúsculas
# Isso serve para ignorar espaços, acentos, pontuação, etc.
palavra_formatada = re.sub(r'[^a-zA-Z0-9]', '', palavra).lower()

# Inverte a string formatada (ex: 'amor' vira 'roma')
palavra_invertida = palavra_formatada[::-1]

# Verifica se a string formatada é igual à sua versão invertida
if palavra_formatada == palavra_invertida:
    # Se for igual, é um palíndromo
    print(f"A palavra/frase {palavra} é um palíndromo.")
else:
    # Se não for igual, não é um palíndromo
    print(f"A palavra/frase {palavra} não é um palíndromo.")


