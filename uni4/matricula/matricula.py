#mudar a matricula de 8 digitos colocando o zero apos o quinto digito e trocar o digito inicial por um.
#ex. 20111035 ==> 101110035
#não pode usar slices nem lista 


#1-entrada: a matricula
m = int(input())

#2-trocar o primeiro elemento por 1
pri = m//10000000
menos = m-(pri*10000000)
div = menos+10000000

#3-colocar um zero depois do 5º elemento 
#3.1- transformar div em string 
matri = str(div)
#3.2- usar for e adicionar 0 no 6º elemento
nova = ""
for i in range(0,len(matri)):
    if i==5:
        nova = nova+"0"
    
    nova = nova+matri[i]

print(nova)
#imprimir o novo cpf 
