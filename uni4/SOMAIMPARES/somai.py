#recebe uma sequencia e calcula a soma dos ultimos impares até atingir o valor limite 
#obs. o valor limite não entra na soma
#ex. 3,1,6,4,7 com limite 9, soma = 8 (1+7) obs. de tras pra frente 

#1-entrada: quantos itens, limite, nuns da sequencia 
quant = int(input())
limite = int(input())

#nuns dentro do for
#colocar os elementos dentro de uma lista 
lista = []
for i in range(0,quant):
    n = int(input())
    lista.append(n)

#criar um for e colocar a lista de tras pra frente pra facilitar
listai = []
for i in range(0,quant):
    listai.append(lista[(quant-1)-i])

#somar os elementos impares até chegar no valor limite (<=)
soma = 0
for n in listai:
    if n%2!=0:
        soma=soma+n
        if soma>=limite:
            soma= soma-n
            break

#imprimir a soma
print(soma)
