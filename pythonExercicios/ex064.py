n = float(0)
count = int(0)
soma = float(0)
while n != 999:
    count += 1
    soma += n
    n = float(input('Digite um número: '))
print('você digitou 999 e o processo foi encerrado')
print('vocẽ digitou {} números e a soma deles foi {}'.format(count - 1, soma))
