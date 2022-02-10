pares = list()
ímpares = list()
valores =[pares, ímpares]
for c in range (0,7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        ímpares.append(num)
pares.sort()
ímpares.sort()
print('-='*30)
print(f'Os valores pares digitados foram: {valores[0]}')
print(f'Os valores ímpares digitados foram: {valores[1]}')

#DiAG
#print(valores)
#print(pares)
#print(ímpares)
#pares.sort()
#ímpares.sort()
#print(valores)
#print(pares)
#print(ímpares)
