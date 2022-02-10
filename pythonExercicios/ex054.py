from datetime import date
ano = date.today().year

#import datetime
#from datetime import date
#anoatual = datetime.date.strftime('%Y')
print(ano)
#anohj = int(anoatual)
soma = 0
for c in range(1, 8):
    nas = int(input('Digite um ano de nascimento: '))
    if nas + 18 < ano:
        soma += 1

if soma != 0:
    print('Das datas de nascimento digitadas \n apenas {} atingiram a maioridade'.format(soma))
else:
    print('Das datas digitadas, nenhuma atingiu a maioridade')
