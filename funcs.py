import random
from main import main

def algoritmo_elementar(seq):
    pilhas = []

    for valor in seq:
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


def algoritmo_aleatorio(seq):
    pilhas = []

    for valor in seq:
        valor = int(valor)
        indices_validos = []
        
        for i in range(len(pilhas)):
            if valor <= pilhas[i][-1]:
                indices_validos.append(i)
        
        idx_aleatorio = random.choice(indices_validos+[-1])
        
        if idx_aleatorio == (-1):
            pilhas.append([valor])  # cria uma nova pilha
        else:
            pilhas[idx_aleatorio].append(valor)  # insere na pilha escolhida
    
    num_pilhas = len(pilhas)
    tamanho_maximo_pilha = max(len(pilha) for pilha in pilhas)
    tamanho_minimo_pilha = min(len(pilha) for pilha in pilhas)

    print("\nResultado da simulação: ")
    print("- Total de pilhas:", num_pilhas)
    print("- Tamanho máximo:", tamanho_maximo_pilha)
    print("- Tamanho mínimo:", tamanho_minimo_pilha)

    main()

def compara():
    pass