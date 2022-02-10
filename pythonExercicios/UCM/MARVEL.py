from time import sleep
fase1 = ({'Filme': 'Homem de Ferro', 'Ano': 2008},
        {'Filme': 'O Incrível Hulk', 'Ano': 2008},
        {'Filme': 'Homem de Ferro 2', 'Ano': 2010},
        {'Filme': 'Thor', 'Ano': 2011},
        {'Filme': 'Capitão América: O Primeiro vingador', 'Ano': 2011},
        {'Filme': 'Vingadores', 'Ano': 2012})

fase2 = ({'Filme': 'Homem de Ferro 3', 'Ano': 2013},
        {'Filme': 'Thor: O Mundo Sombrio', 'Ano': 2013},
        {'Filme': 'Capitão América: O Soldado Inverna', 'Ano': 2014},
        {'Filme': 'Guardiões da Galáxia', 'Ano': 2014},
        {'Filme': 'Vingadores: Era de Ulton', 'Ano': 2015},
        {'Filme': 'Homem-Formiga', 'Ano': 2015})

fase3 = ({'Filme': 'Capitão América: Guerra Civil', 'Ano': 2016},
         {'Filme': 'Doutro Estranho', 'Ano': 2016},
         {'Filme': 'Guardiões da Galáxia 2', 'Ano': 2017},
         {'Filme': 'Homem-Aranha: De Volta ao Lar', 'Ano': 2017},
         {'Filme': 'Thor: Ragnarok', 'Ano': 2017},
         {'Filme': 'Pantera Negra', 'Ano': 2018},
         {'Filme': 'Vingadores: Guerra Infinita', 'Ano': 2018},
         {'Filme': 'Homem-Formiga e a Vespa', 'Ano': 2018},
         {'Filme': 'Capitã Marvel', 'Ano': 2019},
         {'Filme': 'Vingadores: Ultimato', 'Ano': 2019},
         {'Filme': 'Homem-Aranha: Longe de Casa', 'Ano': 2019})

fase4 = ({'Filme':'Viúva Negra', 'Ano': 2021},
         {'Filme':'Shang-Chi e a Lenda dos Dez Anéis', 'Ano': 2021},
         {'Filme':'Os Eternos', 'Ano': 2021},
         {'Filme':'Homem-Aranha: Sem volta para casa', 'Ano': 2021})

series = ({'Serie':'WandaVision', 'Ano': 2021},
          {'Serie':'Falcão e Soldado Inverna', 'Ano': 2021},
          {'Serie':'Loki', 'Ano': 2021},
          {'Serie':'What if...?', 'Ano': 2021},
          {'Serie':'Gavião Arqueiro', 'Ano': 2021})

ucm = (fase1, fase2, fase3, fase4, series)


# Funções
def title(msg):
    print('*=*' * 12)
    print(msg)
    print('*=*' * 12)


def menu():
    while True:
        print('O que você gostaria de fazer.')
        print('(1) - Listar Filmes da fase 1.')
        print('(2) - Listar Filmes da fase 2.')
        print('(3) - Listar Filmes da fase 3.')
        print('(4) - Listar Filmes da fase 4.')
        print('(5) - Listar Series.')
        print('(6) - Escolher o melhor.')
        print('(7) - Sair!')
        c = int(input('>>>>>>>>>>>: '))
        if 0 < c < 8:
            return c

def mostraFilme(x):
    print('=+'*15)
    v =0
    if x == 5:
        frase = 'Series da Marvel'
        saida = 'Serie'
    else:
        frase = 'Filmes da fase'
        saida = 'Filme'
    print(f'{frase:^15}')
    print(f'  {saida:<40}', end='')
    print(f'{"Ano       Nota":<45}')
    for e in ucm[x - 1]:
        if x == 5:
            print(f'{ucm[x - 1][v]["Serie"]:<40}', end='')
        else:
            print(f'{ucm[x - 1][v]["Filme"]:<40}', end='')
        try:
            print(f'{ucm[x - 1][v]["Ano"]}        {ucm[x - 1][v]["Nota"]}')
        except:
            print(f'{ucm[x - 1][v]["Ano"]}      N/A')
        v += 1
        sleep(0.5)

    while True:
        print('~~~~~~~~~~~~~~ Fim da fase ~~~~~~~~~~~~~~')
        input('Aperte ENTER para continuar')
        break

def menuMelhor():
    while True:
        print('O que você gostaria de fazer?')
        print('(1) - Dar nota para cada Filme.')
        print('(2) - Batalha dos Filmes.')
        print('(3) - Listar obras por Nota.')
        print('(4) - Voltar ao Menu principal.')
        print('(5) - Sair!')
        c = int(input('>>>>>>>>>>>: '))
        if 0 < c < 6:
            break
    return c


def byebye():
    print('Obrigado por utilizar o UCM Filmes e Series Avaliator')
    print('Até breve...')


def notas():
    title('  VOTAÇÃO POR NOTA ')
    print('+='*15)
    print('Digite uma nota de 0 a 10 para cada Filme. Para interromper votação (999)')
    print('+=' * 15)
    print(' Filme', end='')
    print('\t \t \t \t NOTA')
    for l in range(0, len(ucm)):
        for c in range(0, len(ucm[l])):
            if l == 4:
                print(ucm[l][c]['Serie'], end='')
            else:
                print(ucm[l][c]['Filme'], end='')
            nt = input('\t \t Nota:').strip()
            while True:
                if nt.isnumeric():
                    nt = int(nt)
                    if nt >= 0 and nt <= 10:
                        ucm[l][c]['Nota']= nt
                        break
                    if nt == 999:
                        break
                else:
                    print('Digite uma nota valida de 0 a 10')
                    nt = input('\t \t Digite a nota de 0 a 10:').strip()
            if nt == 999:
                break
        if nt == 999:
            break





# Programa principal
choice = 1
while choice != 7:
    title('  FILMES e SERIES da MARVEL ')
    choice = menu()
    #print(choise)
    if choice != 6 and choice != 7:
        mostraFilme(choice)
    elif choice == 6:
        choice = menuMelhor()
        if choice == 5:
            byebye()
            break
        elif choice == 1:
            notas()
#        elif choice == 3:
#            note_list()
#        elif choice == 2:
#            batalha()
    else:
        byebye()
        break