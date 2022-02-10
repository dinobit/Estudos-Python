ficha = dict()

ficha['Nome']=str(input('Digite o nome do Aluno: '))
ficha['Média']=float(input(f'Média de {ficha["Nome"]}: '))
if ficha['Média'] < 5:
    ficha['Situação'] = 'Reprovado'
elif 5 <= ficha['Média'] <7:
    ficha['Situação'] = 'Recuperação'
else:
    ficha['Situação'] = 'Aprovado'

for k, v in ficha.items():
    print(f'{k} é igual a {v}')
