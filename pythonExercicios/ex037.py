n1 = int(input('Escreve um número inteiro para conversão: '))
base = int(input('Escolha a base númerica \n 1 - Para binário \n 2 - Para octal \n 3 - Para hexadecimal: '))
if base == 1:
    print('{} em binário é: {}'.format(n1, bin(n1)[2:]))
elif base == 2:
    print('{} em octal é: {}'.format(n1, oct(n1)[2:]))
elif base == 3:
    print('{} em hexadecimal é : {}'.format(n1, hex(n1)[2:]))
else:
    print('Opção invalida, tente novamente.')