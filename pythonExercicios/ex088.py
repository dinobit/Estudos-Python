from random import randint
from time import sleep
gera = list()
print('-'*45)
print(f"{'JOGA NA MEGA SENA':^45}")
print('-'*45)
num = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'Sorteando {num} jogos:')
for c in range(0, num):
    #print(c)
    for j in range (0, 6):
        choose = randint(1,60)
        while choose in (gera):
            choose = randint(1, 60)
        gera.append(choose)
    sleep(1)
    gera.sort()
    print(f'Jogo {c + 1} - {gera}')
    gera.clear()