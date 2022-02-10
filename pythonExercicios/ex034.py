salario = float(input('Digite o valor do seu salário: R$'))
if salario >= 1250:
    aumento = 10
else:
    aumento = 15
print('O valor de seu sariro recebera {}% de reajuste e será agora de R${:.2f}'.format(aumento, (salario * (aumento / 100 + 1))))
