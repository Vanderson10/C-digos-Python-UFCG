#Analisar a pessoa mais velha pelo dia, mes e ano 

#pessoa1
nome1 = input()
dia1 = int(input())
mes1 = int(input())
ano1 = int(input())

#pessoa2
nome2 = input()
dia2 = int(input())
mes2 = int(input())
ano2 = int(input())

#analisar pessoa mais velha pelo ano
if ano1<ano2:
    print(nome1)

elif ano2<ano1:
    print(nome2)

#analisar pelo mes 
else:
    if mes1<mes2:
        print(nome1)

    elif mes2<mes1:
        print(nome2)

#analisar pelo dia 
    else: 
        if dia1<dia2:
            print(nome1)

        elif dia2<dia1:
            print(nome2)

        else: 
            print("nenhuma")


