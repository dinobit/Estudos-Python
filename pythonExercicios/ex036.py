valor = float(input('Digite o valor do Imóvel: R$'))
renda = float(input('Digite sua renda mensal: R$'))
tempo = int(input('Digite a quantidade de anos para pagar: '))
# s 30% da renda > parcela mensal
prestacao = valor / (tempo * 12)
minimo = renda * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(valor, tempo, prestacao))
if prestacao <= minimo:
    print('Seu emprestimo de R${} será aprovado'.format(valor))
else:
    print('Seu emprestimo de R${} não será aprovado.'.format(valor))
