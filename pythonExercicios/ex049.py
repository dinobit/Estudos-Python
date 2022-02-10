x = int(input('Digite o número de sua escolha: '))
print('A Tabuada do número {} :'.format(x))
for c in range (0, 10, 1):
    print('{} x {} = {}'.format(x, c, c * x))
