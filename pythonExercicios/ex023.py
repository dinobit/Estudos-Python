#Meu metodo não funciona se ddigitar um numero menor de 1000 =D
#n1 = str(input('Digite um numero de 0 a 9999: '))
#print('unidade: {}'.format(n1[3]))
#print('dezena: {}'.format(n1[2]))
#print('centena: {}'.format(n1[1]))
#print('milhar: {}'.format(n1[0]))

#metodo do pro
n2 = int(input('Digite um numero: '))
u = n2 // 1 % 10
d = n2 // 10 % 10
c = n2 // 100 % 10
m = n2 // 1000 % 10
print('Analizando o numero {}'.format(n2))
print('Unidade {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {}'.format(c))
print('Milhar {}'.format(m))