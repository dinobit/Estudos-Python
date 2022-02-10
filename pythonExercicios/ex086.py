#linha1 = list()
#linha2 = list()
#linha3 = list()
linha1 = [0, 0, 0]
linha2 = [0, 0, 0]
linha3 = [0, 0, 0]
matrix = [linha1, linha2, linha3]
for l in range(0, 3):
    for c in range(0, 3):
        # matrix.insert[l][c] = (int(input('Digite um valor: ')))
        num = int(input(f'Digite um valor para [{l},{c}]: '))
        #print(l, c)
        matrix[l][c] = num
print('=-'*10)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^5}]', end='')
    print()
#for c, v in enumerate(linha1):
#    print(f'[{v:^5}]',end=' ')
#print('\b')
#for c, v in enumerate(linha2):
#    print(f'[{v:^5}]',end=' ')
#print('\b')
#for c, v in enumerate(linha3):
#    print(f'[{v:^5}]',end=' ')
#print('\b')
print('=-' * 10)