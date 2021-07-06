#Recebe um numero inteiro maior que 0
#imprime os divisores desse numero 


#entrada num int
num = int(input())

#for de 1 ate o num 
#analisar quais num%==0
for n in range(1,num):
    if num%n==0:
        print(n)




