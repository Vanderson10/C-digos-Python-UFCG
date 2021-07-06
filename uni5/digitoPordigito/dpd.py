#receber um inteiro e imprimir cada algarismo separadamente por calculos sucessivos

#1)recebe um num da entrada
#2)transforma em int só para saber a quantidade 
#3)calcula tudo com o while

n = int(input())
quant = len(str(n))

i=quant
e = 0
while i>0:
    num = (n//(10**e)%10)
    e+=1
    i-=1
    print(num)




    


