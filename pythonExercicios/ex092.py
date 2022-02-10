import datetime
anoatual = datetime.date.today().year
ficha = {}
ficha['nome'] = str(input('Digite o nome: '))
ano = int(input('Digite o ano de nascimento: '))
ficha['idade'] = anoatual - ano
ficha['CTPS'] = int(input('CTPS (0 para não possui): '))
if ficha['CTPS'] != 0:
    ficha['inicio'] = int(input('Ano de contratação: '))
    ficha['salário'] = float(input('Valor do Salário: '))
    ficha['aposenta'] = ficha['idade'] + ((ficha['inicio'] + 35) - anoatual)
for k, v in ficha.items():
    print(f'{k} tem o valor {v}')
#print(ficha)
