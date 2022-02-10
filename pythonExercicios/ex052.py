n1 = int(input('Digite um número inteiro: '))
qt = 0
for c in range(1, n1 + 1):
    if n1 % c == 0:
        print('\33[33m', end='')
        qt += 1
    else:
        print('\33[31m', end='')
    print('{}'.format(c), end='')
print('\n\33[m')
if qt > 2:
    print('O número {} não é primo, pois foi divisivel {} vezes'.format(n1, qt))
else:
    print('O número {} é primo, pois só foi divisivel por 1 e por {}'.format(n1, n1))