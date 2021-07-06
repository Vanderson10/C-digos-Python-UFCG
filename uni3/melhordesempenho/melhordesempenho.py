#calcular qual aluno teve mais "." no miniteste
#se tiver empate coloca o primeiro 
#se nenhum conseguiu acertar nada é pra imprimir -1

quant = int(input())
#recebo a entrada
#verificar quantos pontos 
maior = 0
lista = []
for val in range(quant):
    pontos = input()
    soma = 0
    for p in range(0,len(pontos)):
        if pontos[p] ==".":
            soma = soma+1
    
    lista.append(soma)
    if soma>=maior:
        maior = soma
    else: 
        maior = maior

if soma==0:
    print(-1)

else: 
    for i in range(0,len(lista)):
        if maior ==lista[i]:
            print(i+1)
            break




