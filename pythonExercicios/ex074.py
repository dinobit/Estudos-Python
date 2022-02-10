from random import randint
num = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print(num)
ft = True
##print(len(num))
print('='*15)
##x = 3
##print(num[x])
for c in num:
    if ft == True:
        menor = maior = c
        #print(c)
        ft = False
    else:
        if c > maior:
            maior = c
        if c < menor:
            menor = c

    #print(num)
    #print(num[c])
#print(num)
print(f'O menor número da tuplas {menor} e o maior é {maior}')

###METODO DO PROF MARDITO
print(f'O menor numero foi {min(num)}')
print(f'O maior numero foi {max(num)}')