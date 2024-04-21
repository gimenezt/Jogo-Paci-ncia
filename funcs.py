import random
from util import cria_grafico

from main import main

def algoritmo_elementar(seq, comparing = 0):
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

    if comparing == 0:  # ondião para não ficar printando os resultados se estivermos apenas comparando
        print("\nResultado da simulação: ")
        print("- Total de pilhas:", num_pilhas)
        print("- Tamanho máximo:", tamanho_maximo_pilha)
        print("- Tamanho mínimo:", tamanho_minimo_pilha)
        main()
        
    return pilhas


def algoritmo_aleatorio(seq, comparing = 0):
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

    if comparing == 0:  # ondião para não ficar printando os resultados se estivermos apenas comparando
        print("\nResultado da simulação: ")
        print("- Total de pilhas:", num_pilhas)
        print("- Tamanho máximo:", tamanho_maximo_pilha)
        print("- Tamanho mínimo:", tamanho_minimo_pilha)
        main()
    
    return pilhas


def comparar_algoritmos(tamanho_minimo, tamanho_maximo, delta, num_amostras):
    print("Gerando gráfico...")
    tamanhos = list(range(tamanho_minimo, tamanho_maximo + 1, delta))
    medias_pilhas_elementar = []
    medias_pilhas_aleatorio = []

    for tamanho in tamanhos:
        num_pilhas_elementar = 0
        num_pilhas_aleatorio = 0

        for _ in range(num_amostras):
            permutacao = list(range(1, tamanho + 1))
            random.shuffle(permutacao)
            
            pilhas_elementar = algoritmo_elementar(permutacao, comparing=1)
            num_pilhas_elementar += len(pilhas_elementar)
            
            pilhas_aleatorio = algoritmo_aleatorio(permutacao, comparing=1)
            num_pilhas_aleatorio += len(pilhas_aleatorio)

        medias_pilhas_elementar.append(num_pilhas_elementar / num_amostras)
        medias_pilhas_aleatorio.append(num_pilhas_aleatorio / num_amostras)

    cria_grafico(X=tamanhos, Y1=medias_pilhas_elementar, Y2=medias_pilhas_aleatorio)
    main()
