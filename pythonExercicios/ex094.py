fichas = list()
pessoa = {}
media = 0
while True:
    pessoa['Nome']=str(input('Nome: '))
    while True:
        pessoa['Sexo']=str(input('Sexo: [M/F] ')).upper().strip()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['Idade']=int(input('Idade: '))
    media += pessoa['Idade']
    fichas.append(pessoa.copy())
    pessoa.clear()
    while True:
        continua = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if continua in 'SN':
            break
        print('Erro! Por favor, digite apenas S ou N.')
    if continua in 'Nn':
        break
print('-='*30)
print(f'O grupo tem {len(fichas)} pessoas.')
media = media / len(fichas)
print(f'A média de idade é de {media}')
print(f'As mulheres cadastradas foram: ', end='')
for c in range(0, len(fichas)):
    if fichas[c]['Sexo'] == 'F':
        print(fichas[c]['Nome'], end=', ')
print()
print(f'Lista de pessoa que estão acima da média:')
for c in range(0, len(fichas)):
    if fichas[c]['Idade'] > media:
        print(fichas[c])
        print('\b')