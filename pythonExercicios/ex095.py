comp = []
ficha = {}
gols = []
#golx = []
while True:
    ficha.clear()
    gols.clear()
    ficha['Nome']=str(input('Digite o nome do Jogador: '))
    qtjogos = int(input(f'Digite a quantidade de Jogos de {ficha["Nome"]}: '))
    for c in range(0, qtjogos):
        gols.append(int(input(f'Quantos gols {ficha["Nome"]} fez na partida {c+1}? ')))
##c = a[:] # pego os valores de A e jogo em c
#gols = golx[:]
    ficha['Gols'] = gols[:]
    ficha['Total'] = sum(gols)
    k = str(input('Deseja continuar? [S/N]')).strip()
    comp.append(ficha.copy())
    if k in 'Nn':
        break
print('=*'*30)
print(comp)
print('=*'*30)
print('cod ', end='')
for i in ficha.keys():
    print(f'{i:<15}', end='')
print()
print('-'*60)
for k, v in enumerate(comp):
    print(f'{k:>3} ', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
    #print(f'{comp[k]["Nome"]}', end='')
    #print(f'{comp[k]["Gols"]}', end='')
    #print(f'{comp[k]["Total"]:>20}')
print('-'*60)
print()
#print(len(comp))
while True:
    qual = int(input('Ver dados de qual jogador? (999 para encerrar)'))
    if qual == 999:
        break
    elif (qual < 0) or (qual > len(comp)-1):
        print('ERRO, digite um número válido')
    else:
        print(f' -- Levantamento do jogador {comp[qual]["Nome"]}')
        for c, v in enumerate(comp[qual]['Gols']):
        #for c in range(0, len(comp[qual]['Gols'])):
            print(f'   No jogo {c+1} fez {v} gols')
print('=^'*30)
print('!!VOLTE SEMPRE!!!')