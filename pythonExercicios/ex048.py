soma = 0
cont = 0
for c in range (1, 501):
    print(c)
    if c % 3 == 0 and c % 2 != 0:
        print('{} é multiplo de três e impar'.format(c))
        soma += c
        cont += 1
print('A soma dos {} números multiplos de três de 1 a 500 é {}'.format(cont, soma))
