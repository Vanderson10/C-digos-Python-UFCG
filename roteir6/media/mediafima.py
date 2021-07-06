#1º)receber os nuns até fim
#2º)calcular a media 
#3º)imprimir os numeros que são menores que a media e seus indices 

#1)usar while e colocar todos os elementos dentro de uma lista até aparecer "fim" 
#2)somar esses elementos no mesmo while com a variavel soma
#2.1) calcular media no final
lista = []
soma = 0
while True:
    n = input()
    if n=="fim":
        break

    else:
        soma+=int(n)
        lista.append(int(n))

media = soma/len(lista)
print(f'{media:.2f}')

#3)com outro while analisar quais elementos da lista são menores que a media e imprimir
i=0
while i<len(lista):
    if lista[i]<media:
        print(f"{i+1} {lista[i]}")
        
    i+=1






