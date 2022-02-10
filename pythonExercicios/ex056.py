media = 0
idademaxima = 0
mulheresmenores = 0
velho = ''
for c in range(1,5):
    nome = str(input('Digite um nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('o sexo (M/F):')).strip().upper()
    media = media + idade
    print(sexo)
    if idade > idademaxima:
        idademaxima = idade
        velho = nome
    if sexo == 'F' and idade < 20:
        mulheresmenores += 1

print('A média das idades destas pessoas é {}'.format(media/4))

if velho == '':
    print('Não foram listados homens')
else:
    print('O Homem mais velho é {}'.format(velho))

print('Existem {} mulheres menores de 20 anos'.format(mulheresmenores))