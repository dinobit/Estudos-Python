nome = str(input('Escreva seu nome completo: '))
nome2 = nome.split()
print('O primeiro nome é {}'.format(nome2[0]))
print('O ultimo nome é {}'.format(nome2[int(len(nome2) - 1)]))
