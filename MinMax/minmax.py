def minmax_sort(lista):
    metade = len(lista)//2
    maior = 0
    menor = 0
    soma = 0
    i = 0
    j = len(lista)
    t = -1
    li = []
    while True:
        maior = i
        menor = i
        for l in range(i,j):
            if lista[l]<lista[menor]:
                menor = l

        lista[menor],lista[i] = lista[i], lista[menor]

        for l in range(i,j):
            if lista[l]>lista[maior]:
                maior = l
                
        lista[maior], lista[t] = lista[t], lista[maior]
        
        li.append(lista)

        i+=1
        j-=1
        t-=1

        if i==metade: break

    return li

lista = [7,4,8,1,2,3]
print(minmax_sort(lista))
