def aumentar(v, p):
    v += (v * p) / 100
    return v

def diminuir(v, p):
    v -= (v * p) / 100
    return v


def dobro(v):
    v *= 2
    return v


def metade(v):
    v /= 2
    return v


def moeda(v):
    return f'R${v:.2f}'


