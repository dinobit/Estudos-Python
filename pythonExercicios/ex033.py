n1 = float(input('Digite um número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

if n1 > n2:
    if n1 > n3:
        maior = n1
    else:
        maior = n3
    if n2 < n3:
        menor = n2
    else:
        menor = n3
else:
    if n2 > n3:
        maior = n2
    else:
        maior = n3
    if n1 < n3:
        menor = n1
    else:
        menor = n3

print('Analizando os numeros {}, {} e {}'.format(n1, n2, n3))
print('O numero de maior valor é {} e o menor é {}'.format(maior, menor))

##MEtodo do prof
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3

##maior
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3

print('Analizando os numeros {}, {} e {}'.format(n1, n2, n3))
print('O numero de maior valor é {} e o menor é {}'.format(maior, menor))
