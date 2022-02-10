def teste():
    global b
    b = 777
    x = 8
    n = 12
    print(f'Na função teste, n valr {n}')
    print(f'Na função teste o x vale {x}')
    print(f'Na função teste o b vale {b}')


# Principal
n =2
g = 666
print(f'No programa principal, n vale {n}')
print(f'Na função teste o b vale {b}') #B vira global dentro da def acima
# print(f'No programa principal, x vale {x}') < Essa linah da erro pq não existe x global.
teste()

# ^^^ X tem um escopo local, e n é uma variavel global. ^^^

# Interactive Help
print(input.__doc__)
help(input)

# DOCSTING


def contador(i, f, p):
    """
    Faz uma contagem e mostra na tela
    :param i:  ínicio da contagem
    :param f:  fim da contagem
    :param p: intevalo da contagem (passo)
    :return: Não retorna nenhum valor
    Função criada by Chipset 0 absolut bits - Dinobit CEO
    """
    for c in range(i, f, p):
        print(f'{c} -', end='')
    print('FIM!')


contador(2, 100, 2)
help(contador)

# Parametros Opcionais
def somar(a, b, c = 0): # caso não receba C, o c vale 0
# def somar(a=0, b=0, c=0) #<--caso não seja passado nenhum valor
    s = a + b + c
    print(f'A soma vale {s}')

somar(3, 2, 5)
somar(8, 4) # qual será o valor de c? Vai dar pau or...

