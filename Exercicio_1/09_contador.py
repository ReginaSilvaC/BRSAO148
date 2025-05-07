'''9 - Crie um programa que faça uma contagem regressiva de 5 até 1 usando while, e exiba “Lançar!” no final.'''

import time

# Mensagem de início
print("Preparando para lançar...")
time.sleep(1)

# Inicia a contagem a partir de 5
contador = 5

# Enquanto o contador for maior que 0, continua
while contador > 0:
    print(f"{contador}...", end=" ")  # Exibe o número e a animação de ponto
    time.sleep(1)  # Espera 1 segundo
    contador -= 1  # Diminui 1 a cada repetição

# Mensagem final
print("\nAção!")