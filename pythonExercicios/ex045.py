from random import choice
from time import sleep
print('>> Pedra \n>> Papel \n>> Tesoura')
userch = str(input('Escolha uma oção:'))
userch = str.upper(userch)
print(userch)
if userch != 'PEDRA' and userch != 'PAPEL' and userch != 'TESOURA':
    print('Sua opção não é valida. Tente novamente!')
else:
    print('Escolhendo minha MÃO')
    sleep(0.5)
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO')
    pcch = choice(['PEDRA', 'PAPEL', 'TESOURA'])
    print('Eu escolhi: {} , você escolheu {}!'.format(pcch, userch))
    if pcch == userch:
          print('Nos empatamos')
    elif (pcch == 'PEDRA' and userch == 'TESOURA') or (pcch == 'PAPEL' and userch == 'PEDRA') or (pcch == 'TESOURA' and userch == "PAPEL"):
            print('Eu venci')
    else:
            print('Você venceu')
