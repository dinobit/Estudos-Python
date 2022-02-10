soma = 0
for c in range (0, 6):
    n1 = float(input('Digite o número {}: '.format(c+1)))
    if n1 %2 == 0:
        soma += n1
print('A soma dos números pares digitados é {:.1f}'.format(soma))
