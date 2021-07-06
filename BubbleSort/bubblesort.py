
def inteiro(string):
    lista = string.split()
    l = []
    for i in range(len(lista)):
        l.append(int(lista[i]))

    return l

def bubblestep(lista):
    i = 0
    while lista!='fim':
        l = inteiro(lista)
        if i ==len(lista)-1:break
        if l[i]<l[i+1]:
            l[i],l[i+1] = l[i+1], l[i]
        i+=1

    return lista

lista = input()
print(bubblestep(lista))


    


