#distribuir os produtos nas listas que temos disponiveis

def distribui_materia_prima(esteira_de_materia_prima, n):
    k = 0
    lista = []
    for i in range(0,len(esteira_de_materia_prima)):
        if i<n:
            lista.append([esteira_de_materia_prima[i]])
        else:
            lista[k].append(esteira_de_materia_prima[i])
            k+=1

        if k>=n:
            k = 0

    if len(esteira_de_materia_prima)<n:
        p = n-len(esteira_de_materia_prima)
        for i in range(p):
            lista.append([])

    return lista

esteira_de_materia_prima = ['camera', 'fone', 'microfone', 'processador', 'tela']
assert distribui_materia_prima(esteira_de_materia_prima, 3) == [['camera', 'processador'],['fone', 'tela'], ['microfone']]

esteira_de_materia_prima = ['fone', 'cabo', 'sensor', 'processador', 'tela']
assert distribui_materia_prima(esteira_de_materia_prima, 2) == [['fone','sensor','tela'], ['cabo', 'processador']]

esteira_de_materia_prima = ['fone']
assert distribui_materia_prima(esteira_de_materia_prima, 1) == [['fone']]

esteira_de_materia_prima = ['fone']
assert distribui_materia_prima(esteira_de_materia_prima, 3) == [['fone'],[],[]]


