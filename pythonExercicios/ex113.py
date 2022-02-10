def leiaInt():
    while True:

        try:
            n = int(input('Digite um número inteiro: '))
        except KeyboardInterrupt:
            print()
            print('\033[0;33mUsuario preferiu não digitar um valor.\033[m')
            break
        except:
            print('\033[0;31mERRO! Digite um número inteiro válido\033[m')
            n = input('Digite um número inteiro: ')
        else:
            print(f'Você digitou o número {n}')
            break
        finally:
            print('------')


def leiaReal():
    while True:
        try:
            n = float(input('Digite um número real: '))
        except KeyboardInterrupt:
            print()
            print('\033[0;33mUsuario preferiu não digitar valor\033[m')
            break
        except:
            print('\033[0;31mERRO! Digite um número real válido\033[m')
            n = input('Digite um número real: ')
        else:
            print(f'Você digitou o número {n:.2f}')
            break
        finally:
            print('------')


# Programa Principal:
leiaInt()
leiaReal()