#usar for ao contrario
#quando encontrar o indice retorna ele
#caso não encontrar retorna -1

def ultimo_indice(num, lista):
    for i in range(len(lista)-1,-1,-1):
        if lista[i]==num:
            return i

    return -1

assert ultimo_indice(2, [15,2,13,11,14,2]) == 5
assert ultimo_indice(42, [15,2,13,11,14,2]) == -1
