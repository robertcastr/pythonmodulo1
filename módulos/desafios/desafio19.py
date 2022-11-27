##sortando um valor da lista

import random

al1=str(input('Informe o nome do aluno 1'))
al2=str(input('Informe o nome do aluno 2'))
al3=str(input('Informe o nome do aluno 3'))
al4=str(input('Informe o nome do aluno 4'))
lista = [al1,al2,al3,al4] #criação de array
res = random.choice(lista)
print('O aluno escolhido foi o {} '.format(res))

