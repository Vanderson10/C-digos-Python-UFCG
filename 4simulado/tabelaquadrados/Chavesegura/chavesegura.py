#analisar se a chave é segura 
#se não tiver mais que cinco vogais na chave
#não tem tre caracteres consecultivos iguais

#quando detectar que a chave não é segura é para o programa parar e avisar ao usuario

#criar um while e analisar se tem tres letras igual em sequencia
#analisar se tem mais que cinco vogais, analisar com uma lista cada letra.

#entrada
chave = input()
pri = chave[0]
seg = chave[1]
i = 2
soma = 0
vogais = ['A','E','I','O','U','a','e','i','o','u']
e = 0
while True: 
    if pri == seg and pri == chave[i]:
        print("Chave insegura. 3 caracteres consecutivos iguais.")
        break

    else:
        pri = seg
        seg = chave[i]

    i=i+1

    for v in vogais:
        if v==chave[e]:
            soma = soma+1
            break

    e=e+1
    if soma>5:
        print("Chave insegura. 6 vogais.")
        break
            
    if i==len(chave):
        print("Chave segura!")
        break

    if e>len(chave):
        print("Chave segura!")
    
        





    
