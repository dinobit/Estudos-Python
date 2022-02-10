n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, o produto é {}, a divisão é {:.2f}'.format(s, m, d))
print('A divisão inteira é {} e a potencia é {}'.format(di, e))
