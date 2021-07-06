#encontrar letras iguais na mesma posição entre duas palavras 

#entrada
p1 = input()
p2 = input()
print("Letras coincidentes")

if p1<p2:
    p = p1

else: p=p2
#usar for 
#comparar as letras e imprimir qual é a letra e a posição
#realizar soma se for igual
soma = 0
for i in range(0,len(p)):
    if p1[i]==p2[i]:
        soma+=1
        print(f"'{p[i]}' na posição {i+1}")
    
por = (soma*100)//(len(p1)+len(p2))
print(f'Total de letras coincidentes: {soma} ({por}%)')

#imprimir total de letras conincidentes 
