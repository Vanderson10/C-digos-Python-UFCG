#criar um for de 0 a 10
#analisar quantas vezes cada numero desse ta na lista e somar
#caso a soma for igual a 3, então entrará em outro for e esses elementos serão removidos.

def ocorrencia_tripla(lista):
    soma = 0
    for i in range(0,10):
        for l in range(0,len(lista)):
            if i==lista[l]:
                soma+=1

        if soma==3:
            for t in range(len(lista)-1,-1,-1):
                if i==lista[t]:
                    lista.pop(t)

        soma=0

    return lista

l = [1, 1, 2, 1]
ocorrencia_tripla(l)
assert l == [2]

l = [1, 2, 1, 2, 1, 1]
ocorrencia_tripla(l)
assert l == [1, 2, 1, 2, 1, 1]


