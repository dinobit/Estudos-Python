def aprint(msg):
    print('\033[1;30;44m' , end='')
    print('~' * (len(msg) + 4))
    print(f'  {msg}')
    print('~' * (len(msg) + 4))
    print('\33[m', end='')

def helpa(cmd):
    print('\033[0;31;46m' , end='')
    help(cmd)
    print('\33[m', end='')

# Programa principal
while True:
    aprint("SISTEMA DE AJUDA PyHELP")
    print('\033[0;31;40m', end='')
    com=str(input('Finção da Biblioteca > '))
    print('\33[m', end='')
    if com.upper() == "FIM":
        aprint('ATÉ LOGO')
        break
    else:
        helpa(com)