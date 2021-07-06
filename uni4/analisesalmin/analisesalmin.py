#determinar de uma serie de salarios minimos quais ficaram acima e abaixo de 100

#entrada: ano inicial, ano final, valores do salario na faixa de anos indicada 
anoi = int(input())
anof = int(input())

dif = anof-anoi

#indicar quais salarios então acima e quais estão abaixo de 100
#somar quantos anos ficaram abaixo e acima
somab = 0
somac = 0
salac = 0
salab = 0
for i in range(0,dif+1):
    sala = float(input())
    if sala<=100:
        somab +=1
        salab +=sala

    else:
        somac +=1
        salac +=sala

#percentagem
percb = (100*somab)/(dif+1)
percc = (100*somac)/(dif+1)

#media: somar no for os salarios e dividir por dif+1
#só precima imprimir a media caso tenha mais que um valor 
if somac!=0:
    mediaacima = salac/somac
if somab!=0:
    mediaabaixo = salab/somab

#saida 
print(f"{somab} ano(s) abaixo ({percb:.0f}% dos anos)")
if somab !=0:
    print(f"média dos anos abaixo: U$ {mediaabaixo:.2f}")
print(f"{somac} ano(s) acima ({percc:.0f}% dos anos)")
if somac !=0:
    print(f"média dos anos acima: U$ {mediaacima:.2f}")






