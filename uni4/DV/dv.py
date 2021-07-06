#calcular o dv
#digito = soma dos digitos principais%11
#se resto = 10, deve ser subs. por X

#entrada como string 
conta = input()

#fazer um for, transformar em inteiro e somar cada elemento 
soma = 0
for i in range(0,len(conta)):
    soma +=int(conta[i])

#analisar se o resto é 10 e colocar x, caso não seja so imprime 
#imprimir o dv 
dv = soma%11
if dv==10:
    print(f'{conta}-X')

else:
    print(f'{conta}-{dv}')
