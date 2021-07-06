binario = input()
cont = len(binario)-1
soma = 0
for i in range(0,len(binario)):
    cal = int(binario[i])*(2**(cont-i))
    print(f"{binario[i]} * {2**(cont-i)} = {cal}")
    soma +=cal

print(f'{binario}(2) = {soma}(10)')

