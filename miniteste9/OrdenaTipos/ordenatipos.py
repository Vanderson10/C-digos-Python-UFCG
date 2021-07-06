#produzir uma nova lista
#1)primeiras posições aos inteiros
#2)letras
#3)alfanuméricos, incluindo os números com ponto decimal.

def isNumber(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

def ordena_tipos(elementos):
    lista = []
    for i in range(len(elementos)):
        if elementos[i].isdigit() ==True:
            lista.append(elementos[i])
            elementos.pop(i)
            elementos.append('!')

    for i in range(len(elementos)):
        if elementos[i].isalpha()==True:
            lista.append(elementos[i])
            elementos.pop(i)
            elementos.append('!')

    for e in elementos:
        if e.isalnum()==True or isNumber(e)==True:
            lista.append(e)

    return lista

assert ordena_tipos(['1a', '2', 'e', '4', '4.4', 'e6', '8'])  == ['2', '4', '8', 'e', '1a', '4.4', 'e6']

