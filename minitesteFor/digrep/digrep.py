#1º) quantas senhas numéricas de uma dada sequencia tem digitos iguais ao lado

#entrada
quant = int(input())

#1)usar o for e analisar para cada sequencia quais tem um numero ao lado do outro igual
com = 0
for i in range(quant):
    senha = input()
    senhap = senha+"-1"
    soma = 0
    for i in range(0,len(senha)):
        if senha[i]==senhap[i+1]:
            soma +=1

    if soma>0:
        com +=1

print(f'com: {com}')
print(f'sem: {quant-com}')


