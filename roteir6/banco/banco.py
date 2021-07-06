#ler nome do cliente e saldo inicial da conta bancaria 
#1 – Sacar, 2 – Depositar, 3 – Encerrar (operações que serão realizadas)
#valor envolvido 
#Quando o código 3 for informado, o seu programa deve encerrar e imprimir o saldo final da conta.

#saida: Considere uma precisão de duas casas decimais

#receber a opção e o valor dentro do while
#receber como string 
#separar os valores
#transformar os valores em dinheiro em float 
#diminuir com opção 1
#somar com opção 2
#imprimir situção com 3

nom = input()
no = nom.split(" ")
nome = no[0]
soma = float(no[1])

while True:
    entrada = input()
    op = entrada.split(" ")
    opr = int(op[0])
    if opr==3:
        money = 0

    else:
        money= float(op[1])

    if opr==3:
        print(f"Saldo de R$ {soma:.2f} na conta de {nome}")
        break
    
    elif opr==1:
        soma = soma-money

    else:
        soma+=money





