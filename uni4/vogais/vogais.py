#analisar se as letras de uma palavra é vogal ou não 

#entrada
p = input() 

#criar um for e adicionar cada letra numa lista
letras = []
for i in range(0,len(p)):
    letras.append(p[i])

#pegar cada letra e analisar dentro de um for com uma lista de vogais 
#criar uma nova lista com sims e nãos caso seja vogal ou caso não seja 
vogais = ['A','E','I','O','U','a','e','i','o','u']
soma = 0
nova = []
for l in letras:
    for vogal in vogais:
        if l==vogal:
            soma = soma+1

    if soma==1:
        nova.append("sim")

    else:
        nova.append("nao")

    soma = 0

for i in range(0,len(letras)):
    print(f"<{letras[i]}> {nova[i]}")
    



