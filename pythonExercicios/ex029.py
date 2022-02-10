v = float(input('Digite a velocidade do carro ao passar pelo radar em Km/h: '))
print('A velocidade registrada é de {}Km/h'.format(v))
if v > 80:
    print('Você foi multado em {:.2f}'.format((v - 80) * 7 ))