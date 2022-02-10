sexo = str(input('Digite seu sexo "M" ou "F": ')).strip().upper()[0]

#while sexo != 'F' or sexo != 'M':
while sexo not in 'MmFf':
    print('Informação {} incorreta!'.format(sexo))
    sexo = str(input('Digite seu sexo "M" ou "F": ')).strip().upper()[0]
    print(sexo)
print(sexo)
print('Você escolheu {}'.format(sexo))
