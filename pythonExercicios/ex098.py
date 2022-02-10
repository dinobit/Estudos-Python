from time import sleep


def contador(i, f, p):
    if i > f and p > 0:
        passo = p - (p*2)
    elif p == 0:
        passo = 1
    else:
        passo = p
    print('-='*30)
    print(f'Contagem de {i} até {f}, de {passo} em {passo}')
    for c in range(i, f+1, passo):
        print(f'{c} ', end='')
        sleep(0.5)
    sleep(1)
    print(f'FIM!')


# Parte personalizada
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
intervalo = int(input('Intervalo: '))
contador(inicio, fim, intervalo)
