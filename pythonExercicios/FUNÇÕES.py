def mostraLinha(x):
    print('-'*x)

mostraLinha(32)
print('   SISTEMA DE ALUNOS   ')
mostraLinha(15)
print('   CADASTRO DE ALUNOS   ')
mostraLinha(15)
print('   ERRO DO SISTEMA   ')
mostraLinha(9)

def lin(msg):
    print('-' * 25)
    print(msg)
    print('-' * 25)

lin('COISOIO')
lin('BRUCUTU')


def soma(x, y):
    print(f'X = {x} e Y ={y}')
    s = x+y
    print(s)

soma(12, 4)
soma(1, 4)
soma(y=1, x=4)
soma(3, 3)


def cor(cor):
    if cor == 'null':
        print('\33m', end='')
    if cor == 'red':
        print('\33[0;31', end='')

cor('red')
print('Esse texto')
cor('null')
print('Esse texto')

mostraLinha(20)
mostraLinha(20)
mostraLinha(20)
mostraLinha(20)


#RECEBE VARIOS PARAMETROS E SOMA (empacotamento)
def contador(*núm):
    print(núm)
    x = sum(núm)
    print(f'{x}')



contador(5,7,3,1,4)
contador(8,4,7)

mostraLinha(20)
mostraLinha(20)
mostraLinha(1)

#LISTAS passada para DEFs

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [7,2,5,0,4]
print(valores)
dobra(valores)
print(valores)
dobra(valores)
print(valores)
