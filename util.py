def insere_seq():
    len_seq = int(input("Insira o tamanho da sequência: "))
    seq = input("Insira a sequência de inteiros: ").split()
    seq = verifica_len_sequencia(len_seq, seq)    # verifica se len da seqeunia é igual ao numero inserido anteriormente
    
    return seq

def verifica_len_sequencia(n, sequencia):
    while len(sequencia) != n:
        sequencia = input(f"[ERRO] Insira uma sequência de {n} inteiros: ")
    return sequencia