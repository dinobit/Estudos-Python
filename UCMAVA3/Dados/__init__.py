from Utilis import ptcor


def mostrafilme(fs):
    '''
    Mostra pausadamente os filmes da fase selecionada
    :param fase: fase passada para execuçaõ
    :return: Null 0 ziero niente ''
    '''
    from time import sleep
    if fs < 0:
        texto = '~~~~ Série'
    else:
        texto = '~~~~ Filme'
    print(f'\033[0;34m{texto:<40}', end='')
    print(f'{"Ano       Nota"}\033[m')
    try:
        if fs < 0:
            fase = open('seriesucm.txt', 'rt')
        else:
            fase = open('f'+f'{fs}'+'ucm.txt', 'rt')
    except (FileExistsError, FileNotFoundError, PermissionError):
        ptcor('Erro ao abrir o arquivo!', 3)
    else:
        for linha in fase:
            dado = linha.split(';')
            dado[2] = dado[2].replace('\n', '')
            print(f'{dado[0]:<40}{dado[1]}      {dado[2]}')
            sleep(.5)
    finally:
        try:
            fase.close()
        except (FileExistsError, FileNotFoundError, PermissionError):
            ptcor('Erro ao tentar fechar o arquivo', 3)
        ptcor('Enter para voltar ao menu...', 4, False)
        input('')


def atribnotas(fs):
    if fs == 5:
        texto = 'Série'
    else:
        texto = 'Filme'
    #print(f'\033[0;34m{texto:<40}', end='')
    #print(f'{"Ano       Nota"}\033[m')
    try:
        if fs == 5:
            fase = open('seriesucm.txt', 'rt')
        else:
            fase = open('f'+f'{fs}'+'ucm.txt', 'rt')
        filedata = fase.read()
        fase.close()
    except (FileExistsError, FileNotFoundError, PermissionError):
        ptcor('Erro ao abrir o arquivo!', 3)
    else:
        for linha in fase:
            dado = linha.split(';')
            dado[0] = dado[0].replace('\n', '')
            print('Entre com a nota para o filme:')
            print(f'{dado[0]}: ', end='')
            nota = str(input())
            ##AQUI TA OSSO
    finally:
        try:
            fase.close()
        except (FileExistsError, FileNotFoundError, PermissionError):
            ptcor('Erro ao tentar fechar o arquivo', 3)
        ptcor('Enter para voltar ao menu...', 4, False)
        ##input('')