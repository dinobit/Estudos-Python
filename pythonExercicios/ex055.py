maior = float(0)
menor = float(0)
for c in range(1, 6):
    peso = float(input('Digite um peso em Kg:'))
    print('{}Kg'.format(peso))
    if c == 1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print('O maior peso registrado foi {:.1f}'.format(maior))
print('O menor peso registrado foi {:.1f}'.format(menor))