def aumentar(v=0, p=0, form=False):
    v += (v * p) / 100
    if form:
        return moeda(v)
    else:
        return v


def diminuir(v=0, p=0, form=False):
    v -= (v * p) / 100
    if form:
        return moeda(v)
    else:
        return v


def dobro(v=0, form=False):
    v *= 2
    if form:
        return moeda(v)
    else:
        return v


def metade(v=0, form=False):
    v /= 2
    if form:
        return moeda(v)
    else:
        return v


def moeda(v=0, cod='R$'):
    return f'{cod}{v:>8.2f}'.replace('.',',')
    #return f'R${v:.2f}'

def resumo(v=10, ta=10, tr=5):
    print('~' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('~' * 30)
    print(f'Preço analisado: \t{moeda(v)}')
    print(f'Dobro do preço: \t{dobro(v, True)}')
    print(f'Metade do preço: \t{metade(v, True)}')
    print(f'Com {ta}% de aumento: {aumentar(v, ta, True)}')
    print(f'Com {tr}% de redução: \t{diminuir(v, tr, True)}')
    print('~' * 30)
