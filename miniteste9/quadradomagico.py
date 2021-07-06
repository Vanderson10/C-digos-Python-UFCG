#analisar se os resultados estão sendo iguais


def eh_quadrado_magico(quadrado):
    if len(quadrado)!=len(quadrado[0]): return False 
    soma = 0
    soma1 = 0

    for i in range(len(quadrado)):
        for j in range(len(quadrado[0])):
            soma += quadrado[i][j]

        if i==0:
            soma1 = soma

        if soma1!=soma:return False
        soma = 0

    soma=0
    for l in range(len(quadrado)):
        for t in range(len(quadrado[0])):
            soma+=quadrado[t][l]
    
        if soma!=soma1:return False
        soma=0
    
    soma =0
    for i in range(len(quadrado)):
        soma+=quadrado[i][i]
    if soma!=soma1: return False
    soma=0

    soma =0
    for i in range(len(quadrado)):
        for t in range(len(quadrado[0])-1,-1,-1):
            soma+=quadrado[i][t]
        if soma!=soma1: return False
        soma = 0

    return True

quadrado1 = [[2,7,6],[9,5,1],[4,3,8]]
quadrado2 = [[1,2,3],[4,5,6]]
assert eh_quadrado_magico(quadrado1)
assert not eh_quadrado_magico(quadrado2)
