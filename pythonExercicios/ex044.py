preco = float(input('Qual o preço do produto: R$'))
#print('INFORME TIPO DE PAGAMETO')
print('{:=^40}'.format(' DINOBIT STORE '))
print('1 - à vista')
print('2 - à vista no cartão')
print('3 - 2x no cartão')
print('4 - 3x no cartão')
pagamento = int(input('Digite a forma de pagamento: '))
desconto = 0
juros = 1
if pagamento == 1:
    desconto = 10
elif pagamento == 2:
    desconto = 5
elif pagamento == 3:
    desconto = 0
elif pagamento == 4:
    juros = 1.2
    print(juros)
else:
    print('Forma de pagamento incorreta')

print('Com o pagamento selecionado o valor final do produto é {}'.format((preco - (preco * desconto / 100)) * juros))
