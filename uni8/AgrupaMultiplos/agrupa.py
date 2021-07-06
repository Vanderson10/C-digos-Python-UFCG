#todos os valores divisíveis por k sejam relocados para o início da lista

#criar uma função que recebe o indice de um elemento e adiciona ele no inicio
def agrupa_multiplos(seq, k):
    removidos = []
    for i in range(len(seq)-1,-1,-1):
        if seq[i]%k!=0:
            removidos.append(seq[i])
            seq.pop(i)

    for i in range(len(removidos)-1,-1,-1):
        seq.append(removidos[i])

    return seq

seq = [6, 15, 12, 6, 8, 3, 25, 14, 1, 10, 7]

# agrupando seq por múltiplos de 5
agrupa_multiplos(seq, 5)
assert seq == [15, 25, 10, 6, 12, 6, 8, 3, 14, 1, 7]

# reagrupando por pares
agrupa_multiplos(seq, 2)
assert seq == [10, 6, 12, 6, 8, 14, 15, 25, 3, 1, 7]


