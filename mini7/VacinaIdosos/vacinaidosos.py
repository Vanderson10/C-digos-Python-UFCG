#analisar se o elemento é maior que 60
#caso for a gente vai remover todos os elementos que não tiver o indice desse elemento. 
#depois colocar de volta os elementos que tava na lista de removidos

def vacina_idosos(fila):
    removidos = []
    for i in range(len(fila)-1,-1,-1):
        if fila[i]<60:
            removidos.append(fila[i])
            fila.pop(i)

    for l in range(len(removidos)-1,-1,-1):
        fila.append(removidos[l])

fila = [25, 33, 67, 61, 35, 8, 12, 15, 22, 63, 75, 30, 34]
vacina_idosos(fila)
assert fila == [67, 61, 63, 75, 25, 33, 35, 8, 12, 15, 22, 30, 34]




