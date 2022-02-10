#Tente alguma coisa se não acontece uma exeção

# operação
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou')

except ZeroDivisionError:
    print('Não é possivel dividir um número por zero')

except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados')

except Exception as erro:
# falhou
    print('Infelizemente tivemos um problema ...:(')
    print(f'{erro.__cause__}')

# deu certo.
else:
    print(f'O resultado é {r}')

# acontece se der certo ou erro
finally:
    print('Volte sempre! Muito Obrigado')