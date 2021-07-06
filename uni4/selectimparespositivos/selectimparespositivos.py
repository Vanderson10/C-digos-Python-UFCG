#imprimir os numero impares menores que o que foi digitado 

#entrada 
n = int(input())

#for com os numeros de 1, pulando de 2 em 2, até o ultimo numero menor que o digitado

for i in range(1,n,2):
    if i<n:
        print(i)
    else:
        break
