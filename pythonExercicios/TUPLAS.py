lanche = ('amburguer', 'suco', 'pizza', 'pudim')
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-3:])

for c in lanche:
    print(f'vou comer {c}')
#TUPLAS SÃO IMUTAVEIS

print(len(lanche))

for c in range (0, len(lanche)):
    print(c)
    print(lanche[c])

for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida} na posição {pos}')

print(lanche)

#para imprimir a tupla em ordem
print(sorted(lanche))

#concatenação de tuplas:
a = (2, 5, 4)
b = (5, 8, 1, 2)
print(a)
print(b)
c = a + b
print(c)
#tamanho da tupla
print(len(c))

#quantas x aparece o numero na tupla - ex '5'
print(c.count(5))

#qual posição esta o conteuro
print(c.index(8))

#qual ocorrencia do 2 apos posição 3
print(c.index(2, 3))

pessoa = ('Gustavo', 39, 'M', 100)
print(pessoa)
del pessoa
