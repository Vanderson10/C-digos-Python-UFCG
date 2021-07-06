#remove os elementos que tiver como fator o que foi recebido 
#contar quantos fatores foram removidos 

#1)usar o for de trás pra frente
#2)analisar se é o resto com o fator é igual a zero e retirar esse elemento
#3) realizar somar da quantt. desses elementos que estão sendo removidos

def remove_multiplos(fator, numeros):
    soma = 0
    for i in range(len(numeros)-1,-1,-1):
        if numeros[i]%fator==0:
            soma+=1
            numeros.pop(i)

    return soma

numeros = [2, 4, 6, 5, 7, 3, 10, 1]
assert remove_multiplos(2, numeros) == 4
assert numeros == [5, 7, 3, 1]

numeros = [2, 4, 6, 5, 7, 3, 10, 1]
assert remove_multiplos(3, numeros) == 2
assert numeros == [2, 4, 5, 7, 10, 1]

