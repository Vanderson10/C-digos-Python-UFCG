#analisar quando a media dos valores ultrapassam determinado limite
#entrada: n>0, termina com "-", depois do '-' é fornecido o valor limite
#saida: imprimir o menor numero de elementos cuja media é maior que o limite dado.
#indice da posição q a media excedeu 
#se o limite não for alcançado aparecer "limite não alcançado".

#recebe com while todos os elementos até "-"
#add numa lista os valores
#atribuir o ultimo valor a variavel "lim"
lista = []
while True:
    n = input()
    if n =="-":
        lim = float(input())
        break
    else: 
        lista.append(float(n))

#usar outro while para somar e ir dividindo para tirar a media
#ifs: se a media for >= que o lim
#imprima a media 
#imprima o indice 
soma = 0
i = 0 
while True:
    soma +=lista[i]
    media = soma/(i+1)
    i+=1
    if media>=lim:
        print(f'media = {media:.1f}')
        print(f'num = {i}')
        break




