n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua media foi {:.1f}'.format(m))
#if m >= 6:
#    print('Sua media foi boa! Parabéns!')
#else:
#    print('Sua media foi ruim! Estude mais!')
print('PARABENS' if m >=6 else 'Estude mais!')
