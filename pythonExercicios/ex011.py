alt = float(input('Qual a Altura de sua parede?'))
lar = float(input('Qual a Largura da sua parede?'))
area = alt * lar
print('A área da sua parede é de {}m2'.format(alt*lar))
#cada 2 m2 é necesario 1 litro de tinta.
print('A quantidade de tinda necessaria para pintar é {:.1f} litros'.format(area/2))
