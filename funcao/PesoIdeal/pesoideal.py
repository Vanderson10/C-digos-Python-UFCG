#Calcular o peso ideal de várias pessoas

#criar uma função analisando o sexo e altura e usar calculo especifico
def calculaPeso(sexo, altura):
    if sexo=="M" or sexo=="m": 
        peso = 72.7*altura-58 

    else: 
        peso = 62.1*altura-44.7
        
    return peso 

#while que analisa se foi digitado ****
#colocar os valores numa lista 
entrada = 0
lista = []
sexos = []
while True:
    ent = input()
    if ent=="****":break
    entrada = ent.split()
    lista.append(calculaPeso(entrada[0], float(entrada[1])))
    if entrada[0]=='M' or entrada[0]=='m':
        sexos.append('Homem')

    else: sexos.append('Mulher')

#percorrer esses valores com for i imprimir um por vez
for i in range(0,len(lista)):
    print(f'{sexos[i]}: peso ideal é {lista[i]:.1f}')



