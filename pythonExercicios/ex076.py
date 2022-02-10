

listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90,
            'Estojo', 25, 'Transferidor', 4.20, 'Compasso',
            9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print(listagem)

print('-'* 52)
#print('{:-<25}{:->25}'.format('LISTAGEM DE PREÇOS', 'ok'))
print('{:^52}'.format('LISTAGEM DE PREÇOS'))
print('-'* 52)
#vez = True
#for c in listagem:
#    print(c)
#
for c in range (0, len(listagem), 2):
    #print(c)
    ##print(listagem[c])
    ##print(listagem[c+1])
    print('{:.<22}{:.>22}'.format(listagem[c],'R$'), end='')
    print('{:>8.2f}'.format(listagem[c+1]))
print('-'* 52)
