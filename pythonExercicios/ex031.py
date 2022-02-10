d = float(input('Qual a distancia da sua viagem em Km: '))
if d >= 200:
    print('O valor da KM é de R$0,50 e o custo total da viagem é R${:.2f}'.format(d * 0.5))
else:
    print('O valor da KM é de R$0,45 e o custo total da viagem é R${:.2f}'.format(d * 0.45))

