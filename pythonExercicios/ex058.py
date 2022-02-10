from random import randint
from time import sleep
print('Estou pensando em um número de 1 a 10')
sleep(.2)
print('...')
sleep(.2)
print('...')
sleep(.2)
print('...')
num = randint(1, 10)
count = 1
chute = int(input('Tente acertar qual número eu pensei: '))
while chute != num:
    print('Você chutou {}'.format(chute))
    count += 1
    if chute > num:
        print('É menor...')
    elif chute < num:
        print('É maior..')
    chute = int(input('Você errou, tente novamente: '))

print('Você chutou {} e acertou'.format(chute))
print('Você ganhou com {} tentativa(s)'.format(count))
