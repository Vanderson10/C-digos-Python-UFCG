#selecionar as prefeituras que a media dos gastos foram maior que a media estabelecida pela secretaria de financias. 
#imprimir as prefeituras que a media foi a maior que a estabelecida
#se na entrada tiver uma media 2 vezes menor que o valor limite então tem que parar

#entrada
mediasecre = float(input())
valores = "nada"
soma = 0
maiores = []

while True:
    v = input()
    valores = v.split()
    
    if valores==["fim"]:break
    
    i = 0 
    while i<len(valores):
        soma += float(valores[i])
        i+=1

    media = soma/len(valores)
    soma = 0

    if (media*2)<mediasecre:break
        
    if media>mediasecre:
        maiores.append(v)

for maior in maiores:
    print(maior)
