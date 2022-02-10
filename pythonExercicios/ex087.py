#linha1 = list()
#linha2 = list()
#linha3 = list()
linha1 = [0, 0, 0]
linha2 = [0, 0, 0]
linha3 = [0, 0, 0]
matrix = [linha1, linha2, linha3]
somapares = 0
somal3 = 0

for l in range (0,3):
    for c in range (0,3):
        # matrix.insert[l][c] = (int(input('Digite um valor: ')))
        num = int(input(f'Digite um valor para [{l},{c}]: '))
        #print(l, c)
        matrix[l][c] = num
        if num % 2 == 0:
            somapares += num
        if c == 2:
            somal3 += num
print('=-'*10)
for c, v in enumerate(linha1):
    print(f'[ {v} ]',end=' ')
print('\b')
for c, v in enumerate(linha2):
    print(f'[ {v} ]',end=' ')
print('\b')
for c, v in enumerate(linha3):
    print(f'[ {v} ]',end=' ')
print('\b')
print('=-' * 10)
print(f'A soma dos valores pares é {somapares}')
print(f'A Soma dos valores da terceira colina é {somal3}')
print(f'O maior valor da segunda linha é {max(linha2)}')