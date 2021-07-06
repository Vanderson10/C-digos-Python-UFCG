#gratificação de natal
#dados: 235 dias, G = (235 - número de dias que faltou) * valor-da-gratificação-por-dia-trabalhado
#caso ele não tenha faltado nenhum dia tem a gratificação também

#entrada: codigo do cargo, dias que faltou
cod = int(input())

#caso1
if cod == 1:
    print('Deverá receber em dezembro R$ 25000.00.')

elif cod ==2:
    print('Deverá receber em dezembro R$ 15000.00.')

elif cod ==3:
    diasfaltou = int(input())
    gratificacao = (235-diasfaltou)*2
    if diasfaltou ==0:
        gt = 500
        sala = 8000+gt
        print(f"Valor da gratificação R$ {gt:.2f}.")
        print(f"Deverá receber em dezembro R$ {sala:.2f}.")
    else:
        sala = 8000+gratificacao
        print(f"Valor da gratificação R$ {gratificacao:.2f}.")
        print(f"Deverá receber em dezembro R$ {sala:.2f}.")

elif cod ==4:
    diasfaltou = int(input())
    gratificacao = (235-diasfaltou)*1
    if diasfaltou ==0:
        gt = 300
        sala = 5000+gt
        print(f"Valor da gratificação R$ {gt:.2f}.")
        print(f"Deverá receber em dezembro R$ {sala:.2f}.")
    else:
        sala = 5000+gratificacao
        print(f"Valor da gratificação R$ {gratificacao:.2f}.")
        print(f"Deverá receber em dezembro R$ {sala:.2f}.")

elif cod ==5:
    diasfaltou = int(input())
    gratificacao = (235-diasfaltou)*0.7
    if diasfaltou ==0:
        gt = 200
        sala = 2800+gt
        print(f"Valor da gratificação R$ {gt:.2f}.")
        print(f"Deverá receber em dezembro R$ {sala:.2f}.")
    else:
        sala = 2800+gratificacao
        print(f"Valor da gratificação R$ {gratificacao:.2f}.")
        print(f"Deverá receber em dezembro R$ {sala:.2f}.")

