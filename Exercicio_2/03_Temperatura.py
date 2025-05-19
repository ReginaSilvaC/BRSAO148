# Solicita ao usuário que digite o valor da temperatura e converte para float
valor = float(input("Digite a temperatura: "))

# Solicita a unidade de origem (C, F ou K) e converte para maiúscula
origem = input("Digite a unidade de origem (C, F, K): ").upper()

# Solicita a unidade de destino (C, F ou K) e converte para maiúscula
destino = input("Digite a unidade de destino (C, F, K): ").upper()

# Inicializa a variável resultado como None
resultado = None

# Verifica se a unidade de origem é Celsius
if origem == "C":
    if destino == "F":
        resultado = (valor * 9/5) + 32  # Celsius para Fahrenheit
    elif destino == "K":
        resultado = valor + 273.15      # Celsius para Kelvin
    elif destino == "C":
        resultado = valor               # Celsius para Celsius (mesma unidade)

# Verifica se a unidade de origem é Fahrenheit
elif origem == "F":
    if destino == "C":
        resultado = (valor - 32) * 5/9              # Fahrenheit para Celsius
    elif destino == "K":
        resultado = (valor - 32) * 5/9 + 273.15     # Fahrenheit para Kelvin
    elif destino == "F":
        resultado = valor                           # Fahrenheit para Fahrenheit

# Verifica se a unidade de origem é Kelvin
elif origem == "K":
    if destino == "C":
        resultado = valor - 273.15                  # Kelvin para Celsius
    elif destino == "F":
        resultado = (valor - 273.15) * 9/5 + 32     # Kelvin para Fahrenheit
    elif destino == "K":
        resultado = valor                           # Kelvin para Kelvin

# Se nenhuma condição for atendida (unidade inválida)
else:
    resultado = None

# Exibe o resultado se a conversão foi possível
if resultado is not None:
    print(f"Temperatura convertida: {resultado:.2f} {destino}")
else:
    print("Unidade inválida informada.")