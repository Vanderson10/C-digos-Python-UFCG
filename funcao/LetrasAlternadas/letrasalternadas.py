def letras_alternadas(string):
    nova = ""
    for i in range(0, len(string)):
        if i%2==0:
            nova +=string[i]

    return nova

assert letras_alternadas("casa") == 'cs'
assert letras_alternadas("exemplo") == "eepo"

