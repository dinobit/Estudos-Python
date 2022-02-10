def aumentar(v, p, form=False):
    v += (v * p) / 100
    if form:
        return moeda(v)
    else:
        return v

def diminuir(v, p, form=False):
    v -= (v * p) / 100
    if form:
        return moeda(v)
    else:
        return v

def dobro(v, form=False):
    v *= 2
    if form:
        return moeda(v)
    else:
        return v


def metade(v, form=False):
    v /= 2
    if form:
        return moeda(v)
    else:
        return v


def moeda(v):
    return f'R${v:.2f}'


def linha(car, q):
    print(f'{car}' * q)

def ftitle(msg):
    linha('-', 30)
    print(f'{msg.upper():^30}')
    linha('-', 30)

def resumo(v, a, d):
    ftitle('Resumo do Valor')
    print('Preço analizado:', end='')
    print(f'{v:>15}')
    print('Dobro do preço:', end='')
    print(f'{dobro(v, True):>15}')
    print('Metade do preço:', end='')
    print(f'{metade(v, True):>15}')
    print(f'{a}% de aumento:', end='')
    print(f'{aumentar(v, a, True):>15}')
    print(f'{d}% de redução:', end='')
    print(f'{diminuir(v, d, True):>15}')
    linha('-', 30)