from Utilis import ptcor
def upf1to():
    from time import sleep
    try:
        fase1 = open('f1ucm.txt', 'rt')
    except:
        ptcor('Erro ao abrir o arquivo!', 3)
    else:
        for linha in fase1:
            dado = linha.split(';')
            #print(dado)
            #dado[1] = dado[1].replace('\n', '')
            #dado[3] = dado[3].replace('\n', '')
            #print(dado)
            print(f'{dado[0]}/t{dado[1]}   {dado[2]}')
            #print(linha, end='')
    finally:
        fase1.close()
        sleep(2)
