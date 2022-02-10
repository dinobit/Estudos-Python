while True:
    print('-'*30)
    valor = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if valor < 0:
        break
    else:
        for r in range (1, 11):
            print(f'{r} x {valor} = {r * valor}')
