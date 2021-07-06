#1º)imprimir quantos e a soma dos numeros que forem menores que o primeiro
#obs.: o primeiro elemento não deve ser adicionado na soma

#entrada: 11 nuns int 
ref = int(input())

#1.1)recebe 10 numeros
#1.2)analisa se é menor que o ref e soma a quantidade e os lementos
soma = 0
quant = 0

for i in range(0,10):
    n = int(input())
    if n<ref:
        soma +=n
        quant +=1

print(f'menores = {quant}')
print(f'soma = {soma}')


