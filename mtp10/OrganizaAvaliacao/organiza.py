#insatisfeito(-1), neutro(0) e satisfeito(1): niveis de satisfação

#recebi uma lista l
#ordena do menor para o maior, acessando l[i][1]

def organiza_avaliacao(l):
    for i in range(0, len(l)):
        for t in range(0, len(l)):
            if l[i][1]<l[t][1]:
                l[i],l[t] = l[t],l[i]

l = [("Pedro", 1), ("Tito", -1), ("Zeca", 1), ("Lucca", -1), ("Mirna", 0)]

assert organiza_avaliacao(l) == None
assert l == [("Tito", -1), ("Lucca", -1), ("Mirna", 0), ("Pedro",1), ("Zeca", 1)]



l = [("pedro", 1)]
assert l == [("pedro", 1)]

