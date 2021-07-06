#somar e calcular a media dos maiores numeros da dupla
#obs. se for igual, esse número não entra no calculo

#caso não possa calcular a media "Não é possível calcular a média.".

#entrada: quantidade de entradas 
quant = int(input())

#separar com split 
#for para analisar quais são os maiores
#pegar os maiores e somar 
#contar quantos são para calcular a media 
#analisar se não tem nenhum valor para calcular a media 

soma = 0
q = 0
for i in range(0, quant):
    m = input().split(" ")
    m1 = int(m[0])
    m2 = int(m[1])

    if m1>m2:
        soma = soma+m1
        q+=1

    elif m1<m2:
        soma = soma+m2
        q+=1

if soma==0:
    print("Não é possível calcular a média.")

else: 
    media = soma/q
    print(f'{media:.2f}')

    


