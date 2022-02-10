maiores = homens = mulheres = 0
sexo = continua = 'X'

while True:
    continua = 'X'
    idade = int(input('Digita a idade: '))
    sexo = str(input('Digite o sexo (M/F): ')).strip().upper()[0]
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Digite o sexo (M/F): ')).strip().upper()[0]
    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    else:
        if idade < 20:
            mulheres += 1
    #while continua != 'S' and continua != 'N':
    while continua not in 'SN':
        continua = str(input('Deseja cadastrar mais um? (S/N)')).strip().upper()
    if continua == 'N':
        break
print(f'Seu cadastro possui {maiores} pessoas com mais de 18 anos')
print(f'{homens} é o total de homens, e {mulheres} mulheres tem menos de 20 anos.')
