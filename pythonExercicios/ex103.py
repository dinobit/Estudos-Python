def ficha(n='', g=''):
    if n == '':
        n = '<desconhecido>'
    if g.isnumeric():
        g = int(g)
    else:
        g = 0
    print(f'O jogador {n} fez {g} gol(s) no campeonato')


Nome = str(input('Digite o nome do jogador: '))
Gols = str(input('Digite o total de Gols: '))
ficha(Nome, Gols)
