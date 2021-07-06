#descobrir a menor sequencia 
#se for igual colocar a primeira

d1 = input()
dna1 = len(d1)
d2 = input()
dna2 = len(d2)
d3 = input()
dna3 = len(d3)

#verificar qual é menor
if dna1<=dna2 and dna1<=dna3:
    print(f'{d1} {dna1}')

elif dna2<dna1 and dna2<=dna3:
    print(f'{d2} {dna2}')

else:
    print(f'{d3} {dna3}')
