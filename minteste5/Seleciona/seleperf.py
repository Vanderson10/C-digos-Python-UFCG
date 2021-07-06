#encontrar numeros perfeitos dentro de uma lista
#um numero perfeito é aquele em que seus divisores tem como soma esse numero perfeito 


#pegar cada elemento da lista
#gerar seus divisores e somar 
#caso essa soma seja igual ao numero da lista que estamos analizando esse numero é perfeito.

def seleciona_perfeitos(lista):
    soma = 0
    lista1 = []
    for i in range(0,len(lista)):
        for l in range(1,lista[i]):
            if lista[i]%l==0:
                soma+=l

        if lista[i]==soma:
            lista1.append(soma)
        soma = 0

    return lista1

lista = [3, 6, 9, 12, 15, 18, 19, 21, 28]
assert seleciona_perfeitos(lista) == [6, 28]
assert lista == [3, 6, 9, 12, 15, 18, 19, 21, 28]


