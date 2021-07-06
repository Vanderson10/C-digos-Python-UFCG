#analisar se a palavra tem um determinado caracter


#recebi uma lista de palavras
#analisa cada palavra se tem o caractere
#realiza a soma e caso a soma seja >0 então essa palavra tem esse caractere
#e no somapalavras adiciona mais 1.

def palavras_com_caractere(palavras, caractere):
    soma = 0
    somapalavras = 0
    for i in range(0,len(palavras)):
        for letra in palavras[i]:
            if letra==caractere:
                soma+=1

        if soma>0:
            somapalavras+=1

        soma = 0

    return somapalavras


assert palavras_com_caractere(["casa", "carro", "teste"], "x") == 0
assert palavras_com_caractere(["casa", "carro", "teste"], "r") == 1
assert palavras_com_caractere(["casa", "carro", "teste"], "a") == 2

