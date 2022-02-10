valores = list()
cont = 0
keep = 'S'
while keep == 'S':
    valores.append(int(input('Digite um valor: ')))
    cont += 1
    keep = str(input('Deseja continuar? (S/N): ')).strip().upper()[0]

print(f'Você digitou {cont} valores')
#print(valores)
#print(valores.sort())
#print(valores.sort(reverse=True))
valores.sort(reverse=True)
print(f'Em ordem decrescente: {valores}')
if 5 in valores:
    print('O numero 5 consta na sua lista')
else:
    print('O numero 5 não consta na lista')