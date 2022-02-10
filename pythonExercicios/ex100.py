from time import sleep
from random import randint
#numeros = list()
#somados = int
def somapar(lst):
    print('Oi')
    somados = 0
    print(somados)
    for c in range(0, len(lst)):
        if lst[c] % 2 == 0:
            somados += lst[c]
    print(f'Somando os valores PARES de {lst}, temos {somados}')


def sorteia(x):
    numeros = list()
    print(f'Sorteando {x} valores: ', end='')
    for c in range(0, x):
        numeros.append(randint(0, 10))
        print(f'{numeros[c]}, ', end='')
        sleep(0.5)
    print('PRONTO!')
    somapar(numeros)


sorteia(8)