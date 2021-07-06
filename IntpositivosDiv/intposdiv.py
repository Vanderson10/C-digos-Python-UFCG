#imprimir os numeros divisiveis por A e B e menores ou igual a K

#entrada
a = int(input())
b = int(input())
k = int(input())

#analisar quem é maior entre A e B
#comecar a analisar pelo maior quais numeros são divisiveis pelo maior e o menor#e o laço ir até chegar igual ou menor k.

if a>b:
    maior= a
    menor= b

else: 
    maior= b
    menor= a

for i in range(1,k+1):
    if maior%k==0 and menor%k==0:
        print(i)







