#entrada
#recebe quantidade de palavras 
quantpala = int(input())

vogais = ['a','e','i','o','u','A','E','I','O','U']
#recebe palavras e vê se a primeira letra é consoante 
#conta quantas começam
cont = 0
consoante = 0
for i in range(0,quantpala):
    #recebe as palavras
    palavra = input()  
    #testa cada vogal a primeira letra
    for i in range(0,len(vogais)):  
        #analisa se a primeira letra é consoante 
        if palavra[0] != vogais[i]:
            #conta +1 se for diferente de vogal
            cont = cont+1           
    #caso a soma seja 10 é uma consoante caso seja 9 é uma vogal 
    if cont==10:
        #soma quantidade de consoantes 
        consoante = consoante+1
    #zera o contador para inciar a proxima palavra 
    cont = 0

#saida
#total de palavras
print(f"total de palavras: {quantpala}")
#inciadas com consoantes e porcentagem
porc = (consoante*100)/quantpala
print(f"iniciadas por consoantes: {consoante} ({porc:.2f}%)")

