import matplotlib.pyplot as plt
import pandas as pd

def insere_seq():
    len_seq = int(input("Insira o tamanho da sequência: "))
    seq = input("Insira a sequência de inteiros: ").split()
    seq = verifica_len_sequencia(len_seq, seq)    # verifica se len da seqeunia é igual ao numero inserido anteriormente
    
    return seq

def verifica_len_sequencia(n, sequencia):
    while len(sequencia) != n:
        sequencia = input(f"[ERRO] Insira uma sequência de {n} inteiros: ")
    return sequencia

def cria_grafico(X, Y1, Y2):
    
    df = pd.DataFrame({
        'Tamanho da Permutação': X,
        'Elementar': Y1,
        'Aleatorio': Y2
    })

    plt.plot(
        'Tamanho da Permutação', 'Elementar', data=df,
        marker='o', markerfacecolor='blue', markersize=12,
        color='skyblue', linewidth=4, label='Elementar'
    )

    plt.plot(
        'Tamanho da Permutação', 'Aleatorio', data=df,
        marker='p', markerfacecolor='red', markersize=12,
        color='firebrick', linewidth=4, label='Aleatorio'
    )

    plt.legend()
    plt.show()
