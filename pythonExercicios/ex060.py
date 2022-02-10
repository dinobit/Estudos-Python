n = int(input('Digite o número a fatorar: '))
fator = n
x = n - 1
while x > 0:
    fator = fator * x
    x -= 1
print('Fator de {} é {}'.format(n, fator))

fator = n
for r in range (n - 1, 0, -1 ):
    fator = fator * r

print('Fator em for de {} é {}'.format(n, fator))

n = int(input('Digite o número a fatorar: '))
x= n
f = 1
while x > 0:
    print('{}'.format(x),end='')
    print(' x ' if x > 1 else ' = ', end='')
    f *= x
    x-= 1
print('{}'.format(f))
