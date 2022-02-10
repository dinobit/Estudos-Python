#LISTAS COMPOSTAS##

pessoas=[['pedro',25],['maria', 19], ['joão', 32]]

#pedro
print(pessoas[0][0]) # pedro
#19
print(pessoas[1][1]) # 19
print(pessoas[2][0]) # joão
print(pessoas[1]) #Maria 19

##Aula 18
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera2 = [['joão', 19],['ana', 33],['joaquim', 13],['Maria', 45]]
print(galera2) #lista toda de lista
print(galera2[0]) #['joao', 19]
print(galera2[0][0]) #joão
print(galera2[2][1]) #13

for p in galera2:
    #print(p[0], end=' - ')
    print(f'{p[0]} tem {p[1]} anos de idade.')

galera3 = list()
dado = list()
for c in range(0, 5):
    dado.append((str(input('Nome: '))))
    dado.append(int(input('Idade :')))
    galera3.append(dado[:])
    dado.clear() #limpa a lista dado.

print(galera3)
totmai = totmen = 0
for p in galera3:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores')