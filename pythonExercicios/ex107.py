import moeda

#print(moeda.aumentar(100, 50))
#print(moeda.diminuir(100,30))
#print(moeda.dobro(100))
#print(moeda.metade(500))

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13)}')
