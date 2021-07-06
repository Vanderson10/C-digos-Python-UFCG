#deixar tudo em maisculo upper()
#usar um for para acessar cada elemento da lista
#usar outro for para analisar as letras dentro da lista
#se a letra consecutiva de uma plavra for igual, então vamos remover essa palavra

def remove_consecutivas(lista):
    soma = 0
    for i in range(len(lista)-1,-1,-1):
        prox = (lista[i]+"1").upper()
        palavra = lista[i].upper()
        for l in range(len(lista[i])):
            if palavra[l]==prox[l+1]:
                soma=1

        if soma==1:
            lista.pop(i)

        soma = 0

lista1 = ['arara', 'tv',   'bacia']
assert remove_consecutivas(lista1) == None
assert lista1 == ['arara', 'tv',  'bacia']

lista1 = ['aRra', 'arRoba',   'bacia']
assert remove_consecutivas(lista1) == None
assert lista1 == ['bacia']


