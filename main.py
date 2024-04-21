from funcs import algoritmo_elementar, algoritmo_aleatorio, compara
from util import insere_seq

def main():
    print("\n=============================\n||    JOGO DA PACIENCIA    ||\n=============================\n")
    print("1 - Simular o Algoritmo elementar\n2 - Simular o Algoritmo Aleatorio\n3 - Comparar os dois algoritmos\n4 - Finalizar o programa\n")
    n = int(input("Insira uma das opções anteriores (1 - 4): "))
    
    if n == 1:
        seq = insere_seq()
        algoritmo_elementar(seq)

    elif n == 2:
        seq = insere_seq()
        algoritmo_aleatorio(seq)

    elif n == 3:
        compara()
        
    else:
        print("FIM DO PROGRAMA!")

main()
