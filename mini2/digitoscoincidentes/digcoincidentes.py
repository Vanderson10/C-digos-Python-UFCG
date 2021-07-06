#vê quais digitos pares são iguais na mesma posição entre dois numeros

#entrada
num1 = int(input())
num2 = int(input())

#avaliar quais serão pares de cada um e adicionar numa lista
lista1 = []
lista2 = []

num11 = str(num1)
num22 = str(num2)
#para lista1 analisar se é par
for n in num11:
    if int(n)%2 ==0:
        lista1.append(int(n))

    else:
        lista1.append(-1)

#para lista2 analisar se é par
for n in num22:
    if int(n)%2 ==0:
        lista2.append(int(n))

    else:
        lista2.append(-3)

#analisar quais são iguais
print("Dígitos coincidentes")
somae = 0
soma = 0
for i in range(0,len(lista1)):
    if lista1[i] == lista2[i]:
        somae = somae+lista1[i]
        soma = soma+1
        print(f'{i+1} na posição {lista1[i]}')

if soma==0:
      print(f"Soma de dígitos coincidentes: 0")

else:
    print(f'Soma de dígitos coincidentes: {somae}')



