inivalor = valor = int(input('Qual valor deseja sacar? '))
um = dez = vinte = cinq = 0
while True:
    if valor >= 50:
        valor -= 50
        cinq += 1
    elif valor < 50 and valor >= 20:
        valor -= 20
        vinte += 1
    elif valor < 20 and valor >= 10:
        valor -= 10
        dez += 1
    elif valor < 10 and valor > 0:
        valor -= 1
        um += 1
    else:
        break
    print(valor)
print('='*35)
print('{:^30}'.format('DINOBANK'))
print('='*35)
print(f'Você solicitou saque de R${inivalor}')
print(f'Total de {cinq} cédulas de R$50')
print(f'Total de {vinte} cédulas de R$20')
print(f'Total de {dez} cédulas de R$10')
print(f'Total de {um} cédulas de R$1')
print('='*35)
print('Volte sempre ao DINOBANK! Tenha um bom dia!')