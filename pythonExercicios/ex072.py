contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oitor', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
print(contagem)
n = int(input('Digite um número de 0 a 20: '))
while n < 0 or n > 20:
    print('Número incorreto!')
    n = int(input('Digite um número de 0 a 20: '))

print(f'O número digitado foi {contagem[n]}')