#primeira linha da entrada indica o angulo inicial 
#segunda linha diferença em graus entre os ângulos de duas linhas consecutivas 
#terceira indica quantas linhas tem a tabela

import math

anguloi = float(input())
diferenca = float(input())
quant = int(input())

print(f"|{'Angulo':6}|{'Seno':7}|{'Cosseno':7}|")
print(f'|{anguloi:6.2f}|{math.sin(anguloi):<07.2f}|{math.cos(anguloi):<07.2f}|')

#for i in range(1,quant):



#    print(f'|{angulo:6}|{grauss:<07}|{grausc:<07}|')







