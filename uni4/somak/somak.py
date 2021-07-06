#vamos ter uma sequencia e um elemento k
#temos que somar os elementos a cada k, da sequencia 

#receber um num int k >=1 (pulos)
k = int(input())
#n quantidade de numeros a serem lidos a seguir
n = int(input())

#calcular a soma dos elementos a cada k posições, incluindo o primeiro elemento
#imprimir sequencia
for i in range(1,n+1):
    entrada = int(input())

soma = 0
for i in range(1,n+1,k):
    soma+=i

print(f"Soma: {soma}.")

