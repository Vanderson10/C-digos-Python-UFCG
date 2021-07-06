#criar uma função que deixa os caracteres consecultivos como unicos
#não pode usar lista

#criar a função
#concatenar a letra a uma variavel, caso a proxima letra não seja igual. 

def unico(entrada):
    unico = ""
    string = entrada+"ç"
    for i in range(0,len(entrada)):
        if string[i]!=string[i+1]:
            unico+=string[i]

    return unico

assert unico("aa***xxxzzb+++") == "a*xzb+"
assert unico("") == ""

