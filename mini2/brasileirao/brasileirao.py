#Escreva um programa que recebe a pontuação final, número de vitórias, números de gols marcados e o número de gols sofridos de dois times e define quem dos dois times está melhor na classificação do Campeonato.

#entrada dados do time a: 
pontosa = int(input())
vitoa = int(input())
golsa = int(input())
sofria = int(input())

#entrada dados do time b:
pontosb = int(input())
vitob = int(input())
golsb = int(input())
sofrib = int(input())

#Calculo saldo de gols
saldoa = golsa-sofria
saldob = golsb-sofrib

#condições
if pontosa>pontosb:
    print("O Time A ganhou do Time B.")

elif pontosb>pontosa:
    print("O Time B ganhou do Time A.")

#se for empate: analisar as vitorias
else: 
    if vitoa>vitob: 
        print("O Time A ganhou do Time B.")

    elif vitob>vitoa:
        print("O Time B ganhou do Time A.")

    #se continuar empatado analisar o saldo 
    else: 
        if saldoa>saldob:
            print("O Time A ganhou do Time B.")

        elif saldoa<saldob:
            print("O Time B ganhou do Time A.")

        else:
            print("Os dois times terminaram empatados.")
