from time import sleep


def fatorial(n, show=False):
    """
    Função para calculo de Fatoria
    :param n: Número
    :param show: Mostra os passos se True, opcional
    :return: f (numero fatorado completo)
    Criada por chipset
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(f, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
            sleep(0.3)
    return f


print(f'{fatorial(7)}')
print(f'{fatorial(7, True)}')
help(fatorial)
