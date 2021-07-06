#encontra o primeiro menor valor de uma lista em relação a um inteiro

def encontra_menores(n, lista):
    soma = 0
    for num in lista:
        if num<n:
            break

        else: soma+=1

    if soma==len(lista):
        return -1
        exit()
    
    return num

lista1 = [100,200,300,400]
lista2 = [15, 12, 4, 9, 10]
assert encontra_menores(100, lista1) == -1
assert encontra_menores(10, lista2) == 4
