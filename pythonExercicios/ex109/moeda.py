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