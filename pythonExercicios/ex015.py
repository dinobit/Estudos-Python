dias = int(input('Digite a quantidade de dias: '))
km = float(input('Digite a Quilometragem rodada: '))
total = (dias * 60) + (km * 0.15)
print('O valor total é de {:.2f}'.format(total))
