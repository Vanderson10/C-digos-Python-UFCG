#implemente a função conta_votos(votacoes, id)

#analisar se o id é igual ao que recebemos e somar quantos sim e quantos não

def conta_votos(votacoes, ide):
    sim = 0
    nao = 0
    lista = []
    for i in range(0,len(votacoes)):
        voto = votacoes[i].split(',') 
        SN = voto[-1]
        if int(voto[1]) == ide:
            if SN=="sim":sim+=1
            else:nao+=1
    
    lista.append(sim)
    lista.append(nao)
    return lista


votacao = [
    'lei sobre bancos,543,joao,PPPP,sim',
    'lei sobre bancos,543,marina,PPPP,nao',
    'lei maria da penha,5,joao,PPPP,sim',
    'lei sobre bancos,543,julio,P,nao',
    'lei sobre bancos,543,carlos,PBBBB,sim',
    'lei sobre bancos,543,juliana,PP,sim',
    'lei das brs,99,joao,PPPP,sim',
]

assert conta_votos(votacao, 543) == [3, 2]

