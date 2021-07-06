#somar os valores que são diviseiveis por 5

n = int(input())

soma = 0
for i in range(0,n):
    num = int(input())
    if num%5==0:
         soma = soma+num

print(soma)
