#Quando o aluno1 está apto, ele chama o aluno2 para ser a dupla dele.
#Caso esse aluno esteja na lista, o seu nome será colocado antes do aluno2.
#Caso contrário, o nome do aluno1 irá pro final da lista. 

#1)Analisar se o aluno2 etá na lista. 
#1.1)Caso não esteja, add no final da lista
#1.2)Caso esteja, a gente vai adicionar o aluno1 antes do aluno2 (analisar a lista de tras pra frente e remover os alunos até aluno2)
#1.3)Depois iremos colocar os alunos removidos dentro de uma lista e colocar eles de volta dentro da antiga. Zera ela. 

def esta_lista(lista, aluno):
    for i in range(len(lista)):
        if lista[i]==aluno:
            return True
    return False

def insere_nome(aluno1, duplas, aluno2):
        if esta_lista(duplas, aluno2)==False:
            duplas.append(aluno1)

        else: 
            ja = ""
            removidos = []
            for i in range(len(duplas)-1,-1,-1):
                if duplas[i]!=aluno2:
                    if ja!='sim':
                        removidos.append(duplas[i])
                        duplas.pop(i)
                    
                else:
                    removidos.append(aluno2)
                    duplas.pop(i)
                    duplas.append(aluno1)
                    ja='sim'

            for i in range(len(removidos)-1,-1,-1):
                duplas.append(removidos[i])


duplas = ['joel', 'juliano', 'cesar', 'auri', 'zito']
assert insere_nome('gil', duplas, 'juliano') == None
assert duplas == ['joel', 'gil', 'juliano', 'cesar', 'auri', 'zito']
assert insere_nome('marta', duplas, 'vera') == None
assert duplas == ['joel', 'gil', 'juliano', 'cesar', 'auri', 'zito', 'marta']

