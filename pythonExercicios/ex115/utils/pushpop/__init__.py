from ..funcs import titulo


def pushfile():
    '''
    insere uma nova pessoa no arquivo ex115doc1.txt
    :return: Null
    '''
    from ..validadores import validaano
    titulo("NOVO CADASTRO")
    Nome = str(input('Digite um novo nome: '))
    Idade = validaano('Digite o ano de nascimento: ')
    try:
        salvar = open('ex115doc1.txt', 'a')
    except:
        salvar = open('ex115doc1.txt', 'c')
    salvar.write(f'{Nome};{Idade}\n')
    salvar.close()
    print(f'Novo registro de {Nome} cadastrado')

def readfile():
    '''
    Exibe o conteudo do arquivo ex115doc1.txt
    :return: Null
    '''
    from ..funcs import colorize
    from time import sleep
    titulo('PESSOAS CADASTRADAS')
    try:
        salvar = open('ex115doc1.txt', 'rt')
    except:
        colorize('Nenhum cliente cadastrado!', 3)
    else:
        for linha in salvar:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            #print(dado)
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
            #print(linha, end='')
    finally:
        salvar.close()
        sleep(2)
def push():
    '''
    punhava um item no cadastro - em desuso
    :return: cadastro
    '''
    from ..funcs import titulo
    from ..validadores import validaano
    cadastro = {}
    cadastro.clear()
    titulo("NOVO CADASTRO")
    cadastro['Nome'] = str(input('Digite um novo nome: '))
    idade = validaano('Digite o ano de nascimento: ')
    cadastro['Idade'] = idade
    print(cadastro)
    return cadastro


#def save():
#    try:
#        salvar = open('ex115doc1.txt', 'a')
#    except:
#        salvar = open('ex115doc1.txt', 'c')


#def list():
#    for i in range(0, len(todos)):
#        print(todos[i]['Nome'], end='')
#        print(todos[i]['Idade'])