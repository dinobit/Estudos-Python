n1 = str(input('Escreva o seu nome completo: ')).strip()
print(n1.upper())
print(n1.lower())
lista = n1.split()
junto = ''.join(lista)

print('Seu primeiro nome possui {} letras'.format(len(lista[0])))
print('Seu nome completo possui {} letras'.format(len(junto)))

#metodo do prof
print('Seu nome completo possui {} letras'.format(len(n1) - n1.count(' ')))
print('Seu primeiro nome tem {} letras'.format(n1.find(' ')))
