#definir quantas vezes a mesma letra se repete 

def get_frequencia(lista):
    prox = lista[0]
    diferentes = []
    diferentes.append(lista[0])
    for i in range(1,len(lista)):
        if prox==lista[i]:
            prox=lista[i]

        else:
            if lista[i] not in diferentes:
                diferentes.append(lista[i])
                prox = lista[i]
    
    soma = 0
    quants =[]
    for i in range(0,len(diferentes)):
        for l in range(0,len(lista)):
            if diferentes[i]==lista[l]:
                soma+=1

        quants.append(soma)
        soma = 0

    return quants
assert get_frequencia(['b','b','c','b', 'a']) == [3,1,1]
