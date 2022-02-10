def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Por favor, digite um número inteiro valido.')
            continue
        except KeyboardInterrupt:
            print('\nEntrada de dados interrompida pelo usuário!')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('Por favor, digite um número real válido')
            continue
        except KeyboardInterrupt:
            print('Usuário preferiu não digitar esse número.')
            return 0
        else:
            return n

# Programa Principal
num = leiaInt('Digite um valor: ')
num2 = leiaFloat('Digite um valor Real: ')
print(f'O valor inteiro digitado foi {num} e o real {num2}')
