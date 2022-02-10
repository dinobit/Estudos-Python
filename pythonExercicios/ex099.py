from time import sleep
def maior(* tds):
    if tds == ():
        print('Nenhum valor foi informado!')
    else:
        print('-='*30)
        print('Analisando os valores passados...')
        tm = len(tds)
        for c in range (0, len(tds)):
            print(f'{tds[c]} ', end='')
            sleep(0.5)
        print(f'Foram informados {len(tds)} valores ao todo.')
        print(f'O maior número informado foi {max(tds)}')


maior()
maior(4,4,5,2)
maior(41,14,15,22,34,80)
maior(0)
maior(1,1,10,0,0)