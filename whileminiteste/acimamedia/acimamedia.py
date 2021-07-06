#dada uma sequencia de palavras, determinar quais tem tamanho acima da media dos tamanhos das outras palavras
#teremos varias entradas até digitar fim
#saida: media dos tamanhos das palavra com .2f, 
#imprimir palavras com tamanho maior que a media e a posição dessa palavra

#somar a quantidade de letras e calcular a media
#adicionar as palavras numa lista
palavra = "0"
soma = 0
lista = []
while palavra!="fim":
    palavra = input()
    if palavra!="fim":
        lista.append(palavra)
        soma+=len(palavra)

media = soma/len(lista)
print(f'{soma/len(lista):.2f}')
#analisar quais palavras tem tamanho menor que a media e imprimir
for i in range(0,len(lista)):
    if len(lista[i])>media:
        print(f'{i+1} {lista[i]}')




