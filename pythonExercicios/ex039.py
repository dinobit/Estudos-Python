#import datetime
from datetime import date
print('Hojé é: {}'.format(date.today()))
data = str(date.today())
ano = int(data[:4])
uano = int(input('Digite o ano do seu nascimento: '))

if uano < ano - 18:
    print('Você deveria ter se apresentado ao Serviço militar no ano de {}'.format(uano + 18))
elif uano > ano - 18:
    print('Faltam {} anos para você se apresentar ao Serviço Militar.'.format(uano + 18 - ano))
else:
    print('Você deve se apresentar ao Serviço militar este ano')