#entrada 
quant = int(input())

#somar os numeros pares de uma sequencia: ok
#for, somando: ok
soma = 0
lista = []
quantpar = 0
for i in range(0,quant):
    n = int(input())
    lista.append(n)
    if n%2==0:
        soma = soma+n
        quantpar = quantpar+1

#fazer a media dos numeros pares: ok
#pega a soma e divide pela quantidade: ok
media = soma/quantpar

#mostrar os numeros menores(de todos os numeros) que a media dos pares
#adicionar todos os elementos do primeiro passo na lista: ok
#analisar com for quais são os elementos menores que a media dos pares 

#saida 
print(f"soma: {soma}")
print(f'média: {media:.1f}')

soma1 = 0
for num in lista:
    if num<media:
        soma1+=1

print(f"{soma1} número(s) abaixo da média")

