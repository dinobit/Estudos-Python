def menu(msg, *args):

    print(msg.center(42))

    cont = 1
    for i in args:
        print(f'    {cont} - ', end='')
        print(i)
        cont += 1

menu('Ver Filmes', 'Ver Séries', 'Dar Notas', 'Batalha', 'Sair', 'About')
