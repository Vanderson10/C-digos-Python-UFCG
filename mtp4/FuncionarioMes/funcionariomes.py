#Receber a quantidade de chinelos produzidos por cada funcionario nos vários turnos dele.
#Saida: descobrir quem vendeu mais chinelos.
#obs:. não haberá empates

#1)receber cada usuario e realizar a soma do quanto eles venderam
#2)colocar cada soma numa lista 
#3)colocar o nome numas lista
#4) analisar quem vendeu mais na lista

nomes = []
soma = 0
somas = []
while True:
    nome = input()
    if nome=="fim":break
    else:nomes.append(nome)
    while True:
        n = input()
        if n=="-": break
        else: soma+=int(n)

    somas.append(soma)
    soma = 0

#analisar qual soma é maior 
i = 1
maior = somas[0]
nom = nomes[0]
while i<len(somas):
    if maior>=somas[i]:
        maior = maior
        nom = nom

    else:
        maior = somas[i]
        nom = nomes[i]

    i+=1

print(f'Funcionário do mês: {nom}')
    


