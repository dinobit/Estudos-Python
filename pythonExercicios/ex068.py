from random import choice, randint
from time import sleep
vitorias = 0
while True:
    #pc = str(choice(['par', 'ímpar']))
    #print(pc)
    print('\33[35m*-\33[m'*20)
    player = str(input('PAR ou ímpar? ')).strip().upper()
    print(player)
    while player != 'PAR' and player != 'ÍMPAR':
        print('Invalido, digite PAR ou ÍMPAR')
        player = str(input('PAR ou ímpar? ')).strip().upper()
        print(player)
    if player == 'PAR':
        pc = 'ÍMPAR'
    else:
        pc = 'PAR'

    bites = randint(0, 5)
    dedos = int(input('Digite seu número: '))
    soma = dedos + bites
    print(f'você é \33[33m {player} \33[m e eu \33[33m {pc} \33[m')
    print(f'você escolheu \33[33m {dedos} \33[m e eu \33[33m {bites}\33[m')
    if (soma % 2 == 0 and player == "PAR") or (soma % 2 == 1 and player == 'ÍMPAR'):
        final = str('\33[36m você venceu!\33[m')
        vitorias += 1
    else:
        final = str('\33[32m você perdeu!\33[m')
        print(f'a soma é \33[33m {soma}\33[m, \33[33m{final}\33[m')
        sleep(1)
        print(f'você venceu \33[33m {vitorias} x \33[mesta partida.')
        break
    print(f'a soma é \33[33m {soma}\33[m, \33[33m {final}\33[m')
    sleep(1)
    print(f'você já venceu \33[33m {vitorias}x\33[m !!')

