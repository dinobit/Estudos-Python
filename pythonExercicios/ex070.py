total = caros = barato = 0
ft = bool(True)
while True:
    nome = str(input('Qual o nome do Produto? ')).strip()
    preco = float(input(f'diga o preço do produto {nome}: R$'))
    if ft == True:
        barato = barato = preco
        ft = False
    if preco > 1000:
        caros += 1
    if preco < barato:
        barato = preco
        marba = nome
    total += preco
    continua = str(input('Quer colocar mais um produto no carrinho? (S/N)')).strip().upper()[0]
    if continua == 'N':
        break
print(f'O total gasto na compra foi de R${total :.2f}')
print(f'{caros} produtos custaram mais de R$1000,00')
print(f'O produto {marba} foi o mais barato, custando apenas R${barato}')