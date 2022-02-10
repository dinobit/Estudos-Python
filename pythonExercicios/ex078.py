valores = list()
menorpos = list()
maiorpos = list()

for c in range(0, 5):
    #print(c)
    valores.append(int(input('digite um valor para posição {}: '.format(c))))

maior = menor = int(valores[0])

for v in valores:
    if v > maior:
        maior = v
    if v < menor:
        menor = v

for c, v in enumerate(valores):
#    print(f'Na posição {c} encontrei o valor {v}')
    if v == menor:
        menorpos.append(c)
    if v == maior:
        maiorpos.append(c)

print(valores)
print(f'Menor é {menor} na posição {menorpos}')
print(f'Maior é {maior} na posição {maiorpos}')
#print(frase.find('deo'))
