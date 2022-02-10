#Fila entre [ ]
num = [2, 5, 9, 1]
print(num, end='\n')

#substitui key 2 (9 por 3 no ex)
num[2] = 3
print(num, end='\n')

#acrescenta um novo elemento no fim da fila
num.append(7)
print(num)

#organiza em ordem
num.sort()
print(num)

#organiza em ordem decrescente
num.sort(reverse=True)
print(num)

#quantidade de elementos:
print(f'Essa lista tem {len(num)} elementos')
print(num)

#adciona valores: (zero na key 2)
num.insert(2, 0)
print(num)

#remover o ultimo valor
num.pop()
print(num)

#remove um elemento pela key
num.pop(2)
print(num)
#
num.insert(2, 2)
#removendo por elemento (remove o primeiro elemento 2

print(num)
num.remove(2)
print(num)

#Remover valor que não existe da pau no programa - usar o if para testar
if 5 in num:
    num.remove(5)
else:
    print('Não achei o numero 5')

##################
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)

#para cada valor da lista valores / cada elemento da lista
for v in valores:
    print(f'{v}...', end='')
print('\n')

#essa é nova
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('End List')

#criando uma lista vazia e adicionando valores:
compras = list()
for cont in range(0, 5):
    compras.append(int(input('Digite um valor: ')))

print(compras)

print('\n \n')
### UMa lista B = A faz uma ligação ente as listas
a = [2, 3, 4, 7]
b = a
c = a[:] # pego os valores de A e jogo em c
b[2] = 8 #esse comando modifia o [2] nas duas listas a e b
c[3] = 8 # c não tem ligação nenhuma com A
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista B: {c}')

##################
## lembra do While = True?  \ não ta usando !!!
## break                    /
##
##if 'x' in (valores) <---- não ta usando tmb.