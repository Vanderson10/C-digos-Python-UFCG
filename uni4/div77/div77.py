#sequência de números ímpares entre 1 e 101
#encontrar dentro da sequencia os numeros divisiveis por 7 e terminados em 7
#Quando encontrar substituir por um "*"
#saida: 1, 3, 5, *, 9, 11, 13, 15, *, 19, *, 23, ..., 101

#for para a sequencia de 1 até 101, com pulos, pois é só impares 
for n in range(1,102,2):
    #analisar n%7==0
    if n%7==0:
        print("*")
    
    #17,27,37 ... 97
    elif n%10==7:
        print("*")

    else:
        print(n)




