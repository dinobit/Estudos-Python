from random import randint
from time import sleep
ranking ={}
jogo = []
jogada = {}
rank = list()
print('Valores Sorteados')
for c in range(0, 6):
    jogada['jogador'] = c+1
    jogada['dado'] = randint(1, 6)
    print(f'O jogador{jogada["jogador"]} tirou {jogada["dado"]}')
    jogo.append(jogada.copy())
    sleep(1)
#print(jogo)
#print(rank)
#print(jogo[0])
for x in range(0, 7):
    for c in range(0, len(jogo)):
        if jogo[c]['dado'] == x:
            rank.append(jogo[c])
#    rank = {jogo[c]['dado']}
#for k, v in jogada.items():
    #print(f'O {k} é {v}')

#print(jogo)
#print(jogada)
#print(rank)
#print(rank)
print('*=' * 10)
print(f'{"RANKING":^20}')
print('*=' * 10)
for c in range(0, len(rank)):
    print(f'Em {c+1} lugar: Jogador{rank[c]["jogador"]} pontos: {rank[c]["dado"]}')
