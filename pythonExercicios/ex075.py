num = (
    int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite mais um número: ')),
    int(input('Digite o quarto número: ')),
    int(input('Digite o ultimo número: '))
)
print(num)
nove = 0
tres = False
for c in num:
    print(c)
    if c == 9:
        nove += 1
    if c == 3:
        tres = True

print(f'O numero 9 foi digitado {nove} vezes')
if tres == True:
    print(f'O numero 3 aparece primeiro na posição {num.index(3)+1}')
else:
    print('O Valor 3 não foi digitado em nenhuma posição')
print('O valores pares digitados são: - ', end='')
for c in num:
    if c % 2 == 0:
        print(c, end=' - ')

###METODO DO PROFS
print(f'O valor 9 apareceu {num.count(9)} vezes')
print(f'O valor 3 apareceu na {num.index(3)+1} posicao')

##O ultimo foi preciso um for mesmo =D igual o meu!