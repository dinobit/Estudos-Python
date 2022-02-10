import random
from time import sleep
s = random.randint(1, 5)
t = int(input('Advinhe o numero que pensei de 1 a 5: '))
sleep(1)
if s == t:
    print('Você acertou. O numero que pensei foi {} e você digitou {}'.format(s, t))
else:
    print('Você errou. Eu havia pensado no numero {} e você digitou {}'.format(s, t))
