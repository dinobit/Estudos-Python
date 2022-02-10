def menuzim():
    '''
    Mostra o menu inicial
    :return: Nada
    '''
    titulo('MENU PRINCIPAL')
    colorize('1 - ', 1, False)
    colorize('Ver pessoas cadastradas', 2)
    colorize('2 - ', 1, False)
    colorize('Cadastrar nova Pessoa', 2)
    colorize('3 - ', 1, False)
    colorize('Sair', 2)
    print('-' * 40)
    colorize('Sua opção: ', 4, False)


def titulo(msg):
    '''
    Imprime uma mensagem de titulo
    :param msg: mensagem do titulo
    :return: Nada
    '''
    print('~' * 40)
    #print(f'{msg:^40}')
    print(msg.center(40))
    print('~' * 40)


def colorize(txt, cor=0, quebra=True):
    '''
    Recebe um texto e o imprime colorido
    :param txt: mensagem a imprimir
    :param cor: 0, sem cor - 1, amarelo - 2, azul - 3, vermelho - 4, verde
    :param quebra: False = Quebra a linha no final, True = Não quebra
    :return: Nada
    '''
    if cor == 0: #Sem cor
        print(f'\033[m', end='')
    elif cor == 1: # Amarelo
        print(f'\033[0;33m', end='')
    elif cor == 2: # Azul
        print(f'\033[0;34m', end='')
    elif cor == 3: # Vermelho
        print(f'\033[0;31m', end='')
    elif cor == 4: # Verde
        print(f'\033[0;32m', end='')
    print(f'{txt}', end ='')
    if quebra:
        print(f'\033[m')
    else:
        print(f'\033[m', end='')