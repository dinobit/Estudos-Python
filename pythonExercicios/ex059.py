from time import sleep
choice = 4
while choice == 4:
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite o segundo número: '))
    print('Números {} e {}'.format(n1, n2))
    print('\33[33m [1] \33[m somar')
    print('\33[33m [2] \33[m multiplicar')
    print('\33[33m [3] \33[m maior')
    print('\33[33m [4] \33[m novos números')
    print('\33[33m [5] \33[m sair do programa')
    choice = int(input('Escolha uma opção: '))
    print(choice)
    while choice < 1 or choice > 5:
        print('! ! O P Ç Ã O - I N V A L I D A ! !')
        sleep(2)
        print('\n \n \n')
        choice = 4
if choice == 1:
    result = n1 + n2
    name =str('+')
elif choice == 2:
    result = n1 * n2
    name =str('x')
elif choice == 3:
    if n1 > n2:
        print('{} é maior que {}'.format(n1, n2))
    elif n1 < n2:
        print('{} é maior que {}'.format(n2, n1))
    else:
        print('{} e {} são números iguais'.format(n1, n1))
    exit()
elif choice == 5:
    print('\n \n')
    print('Até logo, e obrigado pelos peixes')
    sleep(1)
    print('...')
    sleep(1)
    print('...')
    sleep(1)
    exit()

print('{} {} {} = {}'.format(n1, name, n2, result))