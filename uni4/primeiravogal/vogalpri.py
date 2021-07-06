#encontrar primeira vogal
vogais = ['a','e','i','o','u','A','E','I','O','U']

palavra = input()

soma = 0
for letra in palavra:
    if letra in vogais: 
        print(letra)
        exit()

    else: 
        soma = soma+1

#caso não encontre nenhuma
if soma==len(palavra):
    print('-')




