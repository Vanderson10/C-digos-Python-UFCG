#calcular qual aluno teve mais "." no miniteste
#se tiver empate coloca o primeiro 
#se n acertar nenhuma questão é pra imprimir -1

quant = int(input())

#encontrar qual teve mais "."
maior = 0
lista = []
for i in range(quant):
    exercicio = input()
    soma = 0
    for t in range(0,len(exercicio)):
        if exercicio[t] == ".":
            soma +=1

    lista.append(soma)
    if maior<soma: 
        maior = soma

if maior == 0: 
    print(-1)
    exit()

for v in range(0,len(lista)):
    if lista[v]==maior:
        print(v+1)
        break


    







