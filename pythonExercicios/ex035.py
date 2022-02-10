a = float(input('Digite o tamanho da primeira reta: '))
b = float(input('Digite o tamanho da segunda reta: '))
c = float(input('Digite o tamanho da terceira reta: '))

if ((a + b) > c) and ((a + c) > b) and ((c + b) > a):
    print('Suas retas PODEM formar um triangulo!')
else:
    print('Suas retas NÃO podem formar um triangulo!')
