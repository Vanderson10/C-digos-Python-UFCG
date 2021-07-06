#imprimir todos os multiplos de 5 menos que um determinado valor 
#os numeros devem sair em ordem crescente 

#receber um limite 
lim = int(input())

#analisar se o resto da divisão por 5 é igual a 0 
#depois analisar se é par e imprimir até o limite 
n = 5
while True:
    n+=5
    if n>=lim:
        break
    else:
        if n%2==0:
            print(n)





    
    

