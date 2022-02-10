pessoa = list()
dados = list()
pesados = leves = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(int(input('Peso em Kg: ')))
    dados.append(pessoa[:])
    #print(pessoa[1])
    if pessoa[1] > pesados:
        pesados = pessoa[1]
    if leves == 0 or pessoa[1] < leves:
        leves = pessoa[1]
    pessoa.clear()
    k = str(input('Deseja cadastrar mais um? (S/N): ')).strip().upper()[0]
    if k != 'S':
        break
#analise
print(dados)
print(len(dados))
print(pesados)
print(leves)

###RESPOSTAS
print(f'Você cadastrou {len(dados)} pessoas.')
print(f'As pessoas mais pesadas com {pesados}Kg são', end=': ')
for c in range (0, len(dados)):
    if dados[c][1] == pesados:
        print(dados[c][0], end = ' - ')

print(f'\n \n As pessoas mais leves com {leves}Kg são', end=': ')
for c in range (0, len(dados)):
    if dados[c][1] == leves:
        print(dados[c][0], end = ' - ')