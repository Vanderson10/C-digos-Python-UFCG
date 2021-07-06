#analisar se todos elementos da lista musica está contido na lista de acordes

#1)criar um for dentro de um for e analisar de cada vez se um elemento da musica, depois outro... está dentro da lista de acordes
#1.1) colocar 1 se estiver
#1.2) quando sair do for colocar esse valor dentro de uma soma
#1.3)quando sair dos for se essa soma for igual ao tamanho da lista, então True...

def sei_tocar_musica(musica, acordes):
    simNao = 0
    soma = 0
    for i in range(0,len(musica)):
        for l in range(0,len(acordes)):
            if musica[i] == acordes[l]:
                simNao = 1

        if simNao==1:
            soma = soma+1

        simNao = 0

    if soma==len(musica):
        return True

    return False

musica = ["a", "d", "dm"]
acordes = ["a", "d"]
assert not sei_tocar_musica(musica, acordes)

musica = ["a", "d"]
acordes = ["a", "bm", "d", "c"]
assert sei_tocar_musica(musica, acordes)





