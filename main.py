def main():
    print("\n=============================\n||    JOGO DA PACIENCIA    ||\n=============================\n")
    print("1 - Simular o Algoritmo elementar\n2 - Simular o Algoritmo Aleatorio\n3 - Comparar os dois algoritmos\n4 - Finalizar o programa\n")
    n = int(input("Insira uma das opções anteriores (1 - 4): "))
    
    if n == 1:
        tamanho_permutacao = int(input("Insira o tamanho da permutação (N): "))
        permutacao = input("Insira a permutação dos inteiros de 1 até N: ").split()
        algoritmo_elementar(permutacao)

    elif n == 2:
        algoritmo_aleatorio()

    elif n == 3:
        compara()
        
    else:
        print("FIM DO PROGRAMA!")

def algoritmo_elementar(sequencia):
    pilhas = []

    for valor in sequencia:
        valor = int(valor)
        pilha_inserida = False
        
        for pilha in pilhas:    # itera pilhas existentes para encontrar onde inserir valor
            if valor <= pilha[-1]:
                pilha.append(valor)
                pilha_inserida = True
                break

        if not pilha_inserida:
            pilhas.append([valor])    # se não foi possível inserir em nenhuma pilha existente, cria uma nova

    num_pilhas = len(pilhas)
    tamanho_maximo_pilha = max(len(pilha) for pilha in pilhas)
    tamanho_minimo_pilha = min(len(pilha) for pilha in pilhas)

    print("\nResultado da simulação: ")
    print("- Total de pilhas:", num_pilhas)
    print("- Tamanho máximo:", tamanho_maximo_pilha)
    print("- Tamanho mínimo:", tamanho_minimo_pilha)

    main()


def algoritmo_aleatorio():
    pass

def compara():
    pass

main()
