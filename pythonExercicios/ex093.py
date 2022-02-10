ficha = {}
gols = []
ficha['Nome']=str(input('Digite o nome do Jogador: '))
qtjogos = int(input(f'Digite a quantidade de Jogos de {ficha["Nome"]}: '))
for c in range(0, qtjogos):
    gols.append(int(input(f'Quantos gols {ficha["Nome"]} fez na partida {c+1}? ')))
ficha['Gols'] = gols
ficha['Total'] = sum(gols)
print('=*'*20)
print(ficha)
print('=*'*20)
for k, v in ficha.items():
    print(f'O campo {k} tem o valor {v}.')
print('=*' * 20)
print(f'O jogador {ficha["Nome"]} jogou o total de {qtjogos} partidas:')
for c, v in enumerate(gols):
    print(f'=> Na partida {c+1}, fez {v} gols.')
print(f'Foi um Total de {ficha["Total"]} gols')