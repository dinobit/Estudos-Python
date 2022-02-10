def validamenu(x):
    '''
    Valida a entrada do menu
    :param x: valor selecionado
    :return: valor real selecionado
    '''
    from ..funcs import colorize
    while True:
        try:
            x = int(x)
            if 0 < x < 4:
                break
            else:
                colorize('Digite um número válido: ', 3, False)
                x = input()
        except (ValueError, TypeError):
            #print('ops')
            #simples()
            colorize('Digite um número válido: ', 3, False)
            x = input()
        except KeyboardInterrupt:
            colorize('Usuário preferiu não digitar esse número', 3)
            return 0
    return(x)


def validaano(msg):
    '''
    Valida o ano de nascimento
    :param msg: Mensagem solcitando a entrada
    :return: Idade da pessoa
    '''
    from datetime import date
    print(msg, end='')
    while True:
        nasc = input()
        try:
            nasc = int(nasc)
            if 1900 < nasc < date.today().year:
                idade = int(date.today().year) - nasc
                print(idade)
                break
            else:
                print('Digite um ano valido de nascimento (Ex.: 1945): ', end='')
        except:
            print('Digite um ano valido de nascimento (Ex.: 1992): ', end='')
    return idade