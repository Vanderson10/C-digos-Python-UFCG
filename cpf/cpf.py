#imprimir as 4 partes de um cpf

#recebi as 3 partes 
p1 = int(input())
p2 = int(input())
p3 = int(input())

#transformar p3 em inteiro e soma para formar p4 
pc = (p3//100)
pdd = p3-(100*pc)
pd = pdd//10
pu = pdd-(pd*10)

p4 = pc+pd+pu

print(f"{p1:03}.{p2:03}.{p3:03}.{p4:02}")

