#digitos = [1, 2, 1, 2, 1, 1] deve ficar [1,2]
#digitos = [1, 1, 2, 2, 5, 1] deve ficar [1,2,5]
#remover os digitos repetidos de uma lista

#1)Criar um for para saber dentre os numeros de 0 a 9 quais e quantos existem na lista 
#2)cria um for e vai add numa lista os indices dos numeros que são iguais
#3)tirar o primeiro indice dessa lista
#4)criar um for para retirar os elementos da lista que tem os indices igual os elementos 
#5)apagar todos dessa lista para continuar os proximos numeros. 

def remove_repetidos(digitos):
    soma = 0
    indices = []
    for i in range(0,len(digitos)):
        for l in range(0,len(digitos)):
            if digitos[i]==digitos[l]:
                indices.append(l)
                soma+=1

    return soma,indices

print(remove_repetidos([1,2,1,1,4,5]))

    

#digitos = [1, 1, 2, 2, 5, 1]
#remove_repetidos(digitos)
#print(digitos)

#digitos = [1, 2, 1, 2, 1, 1]
#remove_repetidos(digitos)
#print(digitos)






