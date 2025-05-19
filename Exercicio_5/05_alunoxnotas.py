def solicitar_nome():
    return input("Digite o nome do aluno (ou 'fim' para encerrar): ").strip()

def solicitar_notas():
    notas = []
    for i in range(1, 4):
        while True:
            try:
                nota = float(input(f"Digite a nota {i} (0 a 10): "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Nota inválida. Digite um valor entre 0 e 10.")
            except ValueError:
                print("Entrada inválida. Digite um número.")
    return notas

def calcular_media(notas):
    return sum(notas) / len(notas)

def exibir_resultados(alunos):
    print("\n--- Médias dos Alunos ---")
    melhor_aluno = None
    maior_media = -1

    for nome, notas in alunos.items():
        media = calcular_media(notas)
        print(f"{nome}: Média = {media:.2f}")
        if media > maior_media:
            maior_media = media
            melhor_aluno = nome

    if melhor_aluno:
        print(f"\nAluno com a maior média: {melhor_aluno} ({maior_media:.2f})")

def main():
    alunos = {}

    while True:
        nome = solicitar_nome()
        if nome.lower() == "fim":
            break
        if nome == "":
            print("Nome não pode ser vazio.")
            continue
        if nome in alunos:
            print("Aluno já cadastrado. Escolha outro nome.")
            continue
        notas = solicitar_notas()
        alunos[nome] = notas

    if alunos:
        exibir_resultados(alunos)
    else:
        print("Nenhum aluno foi cadastrado.")

# Executa o programa
main()

