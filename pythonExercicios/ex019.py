import random
a1 = input('Coloque o nome do primeiro aluno: ')
a2 = input('Coloque o nome do segundo aluno: ')
a3 = input('Coloque o nome do terceiro aluno: ')
a4 = input('Coloque o nome do quarto aluno: ')
sortudo = random.choice([a1, a2, a3, a4])
print('O Sorteado para apagar o quadro foi {}. Parabén!'.format(sortudo))
