valores = list()
pares = list()
ímpares = list()
keep = 'S'
while keep == 'S':
    valores.append(int(input('Digite um valor: ')))
    keep = str(input('Deseja continuar? (S/N): ')).strip().upper()[0]
print(f'Os valores digitados foram {valores}')
for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        ímpares.append(v)
print(f'Os pares foram {pares}')
print(f'Os ímpares foram {ímpares}')
