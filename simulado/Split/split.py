#programar o split

#analisar se o delimitador foi encontrado e colocar dentro de uma lista 

def split(frase, delimitador):
    lista = []
    novo = ""
    for i in range(0, len(frase)):

        if frase[i][i+1]==delimitador+delimitador or frase[i]==delimitador:
            lista.append(novo)
            novo = ""

        else:
            novo+=frase[i]

    if i==(len(frase)-1):
        lista.append(novo)
        return lista


print(split('duas,,palavras',','))


