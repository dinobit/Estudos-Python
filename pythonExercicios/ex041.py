from datetime import date
#import datetime
ano = int(input('Qual o ano de nascimento do atleta? '))
anoatual = str(date.today())
idade = int(anoatual[:4]) - ano

if idade <= 9:
    atleta = str('Mirim')
elif idade > 9 and idade <= 14:
    atleta = str('Infantil')
elif idade > 14 and idade <= 19:
    atleta = str('Júnior')
elif idade > 19 and idade <= 25:
    atleta = str('Sênior')
else:
    atleta = str('Master')

print('Você tem {} anos e é um atleta {}'.format(idade, atleta))