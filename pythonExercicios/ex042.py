a = float(input('Digite o tamanho da primeira reta: '))
b = float(input('Digite o tamanho da segunda reta: '))
c = float(input('Digite o tamanho da terceira reta: '))
if ((a + b) > c) and ((a + c) > b) and ((c + b) > a):
    print('Suas retas PODEM formar um triangulo!')
    #if a == b and b == c:
    if a == b == c:
        tipo = 'equilatero'
    elif a != b != c != a:
        tipo = 'Escaleno'
    else:
        tipo = 'Isóceles'
    print('Seu triangulo é {}'.format(tipo))
else:
    print('Suas retas NÃO podem formar um triangulo!')
