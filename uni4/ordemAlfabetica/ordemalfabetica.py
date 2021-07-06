#palavra dada 
#colocar quantas palavras vem antes e quantas vem depois da palavra dada
#se o programa vier em ordem alfabetica não deve ordenar as palavras 

#entrada
quant = int(input())

#usar for e adicionar as palavras dentro de uma lista
lista = []
for i in range(0,quant):
    palavra = input()
    lista.append(palavra)

print("---")
referencia = input()
#analisar se as palavras são maiores ou menores
#se for maior elas vem antes
#se for menor vem depois
antes = depois = 0 
for pa in lista:
    if referencia>pa:
        antes +=1

    elif referencia<pa:
        depois +=1


print(f"{antes} antes")
print(f'{depois} depois')




