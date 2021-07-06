#Fazer a campanha do campinense
#quantas vitorias, empates e derrotas 
#pontos
#saldos de gols 
#pontos em casa
#pontos fora

#acesar pelo indice a quantidade de gols
#comparar dentro do for e realizar a soma de v,e,d
#pontos: v*3+e
#saldo: somar gols que tomou e que levou e diminuir
#calcular os pontos fora e dentro de casa separado e depois comar pra dar o geral

v = 0
d = 0
e = 0
gf = 0  
gl = 0 
pontosc = 0
for i in range(0,10):
    placar = input()
    p = placar.split(" ")
    g1 = int(p[0][0])
    g2 = int(p[0][2])

    if p[1]=="(c)":
        if g1>g2:
            v = v+1
            gf +=g1
            gl +=g2
            pontosc +=3

        elif g1==g2:
            e +=1
            gf +=g1
            gl +=g2
            pontosc +=1

        else:
            d +=1
            gf +=g1
            gl +=g2

    else:
        if g1>g2:
            d+=1
            gf +=g2
            gl +=g1

        elif g1==g2:
            e+=1
            gf +=g2
            gl +=g1

        else: 
            v=v+1
            gf +=g2
            gl +=g1

print(f'{v}v, {e}e, {d}d')
pontos = v*3+e
print(f"pontos: {pontos}")
s = gf-gl
print(f"saldo: {s} ({gf} pro, {gl} contra)")
print(f"pontos em casa: {pontosc}")
print(f'pontos fora: {pontos-pontosc}')





