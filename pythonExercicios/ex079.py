keep = 'S'
valores = list()
while keep == 'S':
    valorin = (int(input('Digite um valor: ')))
    while valorin in valores:
        valorin = int(input('Valor repetido, digite outro valor: '))

    valores.append(valorin)

    keep = str(input('Deseja Continuar (S/N): ')).strip().upper()[0]
print(valores)
valores.sort()
print(f'Você digitou os valores {valores}')
