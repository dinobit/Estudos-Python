def areat(a, b):
    resp = a * b
    print(f'A área de um terreno {a} x {b} é {resp}m².')


print('Controle de Terrenos')
print('-'* 30)
l = float(input('LARGURA: (m) '))
c = float(input('COMPRIMENTO: (m) '))
areat(l, c)