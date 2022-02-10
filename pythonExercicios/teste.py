comp = [{'Nome': 'Tatu', 'Gols': [0, 2, 0], 'Total': 2}, {'Nome': 'manga', 'Gols': [1, 0], 'Total': 1}, {'Nome': 'jau', 'Gols': [4, 0, 2], 'Total': 6}]
print('=*'*20)
print(comp)
print('=*'*20)
print('cod nome          gols          total')
print('-'*35)

for k, v in enumerate(comp):
    print(f'{k}', end=' ')
    print(f'{comp[k]["Nome"]}', end='')
    print(f'{comp[k]["Gols"]}', end='')
    print(f'{comp[k]["Total"]:>20}')
print('-'*35)
print()
print(len(comp))
while True:
    qual = int(input('Ver dados de qual jogador? (999 para encerrar)'))
    if qual == 999:
        break
    elif (qual < 0) or (qual > len(comp))-1:
        print('ERRO, digite um número válido')
    else:
        print(f' -- Levantamento do jogador {comp[qual]["Nome"]}')
        for c in range(0, len(comp[qual]['Gols'])):
            print(f'No jogo {c+1} fez {comp[qual]["Gols"][qual]} gols')
print('=^'*30)
print('!!VOLTE SEMPRE!!!')