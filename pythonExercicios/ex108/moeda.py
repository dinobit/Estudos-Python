def aumentar(v=0, p=0):
    v += (v * p) / 100
    return v


def diminuir(v=0, p=0):
    v -= (v * p) / 100
    return v


def dobro(v=0):
    v *= 2
    return v


def metade(v=0):
    v /= 2
    return v


def moeda(v=0, cod='R$'):
    return f'{cod}{v:>8.2f}'.replace('.',',')
    #return f'R${v:.2f}'