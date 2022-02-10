nome = str(input('Qual é o seu nome: '))
if nome == 'Thiago':
    print('Que nome bonito')
elif nome == 'Tiago':
    print('Bonito nome, mas falta alguma coisa.')
elif nome == 'Enzo':
    print('Eita nome feio.')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia, {}!'.format(nome))
