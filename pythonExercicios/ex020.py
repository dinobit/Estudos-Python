import random
a1 = input('Coloque o nome do primeiro aluno: ')
a2 = input('Coloque o nome do segundo aluno: ')
a3 = input('Coloque o nome do terceiro aluno: ')
a4 = input('Coloque o nome do quarto aluno: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem dos alunos será: {}'.format(lista))
