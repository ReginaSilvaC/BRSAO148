# Estrutuda sequencial
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cidade = input("Cidade onde mora: ")
print("Olá", nome)
print("Você tem", idade, "anos")
print("E mora em",cidade)

# Estrutura de repetição
for i in range(5):
    print("Contar", i)
contar = 0
while contar < 5:
    print("Executar", contar)  
    contar += 1    