#retornar a quantidade de palavras que tem o tamanho maior que k.

#1)separar as palavras com split 
#2)usar um for para analisar quais tem o tamanho maior que k e somar.

def conta_palavras(k, palavras): 
    soma = 0
    p = palavras.split(":")
    for i in range(len(p)):
        if len(p[i])>=k:
            soma+=1

    return soma

assert conta_palavras(5, "zero:um:dois:tres:quatro:cinco") == 2
