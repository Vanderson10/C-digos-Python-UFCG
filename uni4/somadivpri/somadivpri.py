#ler 11 numeros inteiros 
#o primeiro valor é o de referencia 
#imprimir a soma dos valores que são divisores do primeiro elemento 
#o primeiro não entra na soma 

#entrada valor de referencia 
pri = int(input())

#criar um for de 0 ate 11
#analisar quais elementos são divisores do primeiro e somar
soma = 0
for n in range(0,10):
    num = int(input())
    if pri%num==0:
        soma += num

print(soma)

