#multiplicar todos os numeros que estão dentro do vetor


def altera_vetor_por_escalar(vetor, escalar):
    for i in range(0,len(vetor)):
        mul = vetor[i]*escalar
        vetor[i] = mul

vetor_1 = [1, 2, 3]
assert altera_vetor_por_escalar(vetor_1, -1) == None
assert vetor_1 == [-1, -2, -3]
assert altera_vetor_por_escalar(vetor_1, 2) == None
assert vetor_1 == [-2, -4, -6]


