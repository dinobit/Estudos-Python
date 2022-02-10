n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
if n1 > n2:
    print('{} é maior que {}'.format(n1, n2))
elif n1 < n2:
    print('{} é maior que {}'.format(n2, n1))
else:
    print('{} é IGUAL a {}!'.format(n1, n2))