#capturo a frase, retiro os espaços e crio o X = numero de letras na frase
frase = str(input('Digite sua frase/palavra: ')).strip()
# frase = frase.replace(' ', '') # prof usou abaixo
aux = frase.split()
frase = ''.join(aux)

x = len(frase)-1
print(x)
#torno a frase lista
l = list(frase)

#crio a frase que receberá ela ao contrario e transformo em lista
frase2 = str(frase)
l2 = list(frase2)

#print da l2
print(l2)

#print da l2 e da l
print('l2 = {}'.format(l2))
print('l = {}'.format(l))
print('\n \n \n')
#alteração
#l2[4] = l[0]

#laço querido
for c in range(0, x+1):
    l2[c] = l[x]
    x = x - 1

#print da l2 pós alteração
print('l2 = {}'.format(l2))
print('l = {}'.format(l))

#ve se é ingual
frase = ''.join(l)
frase2 = ''.join(l2)

if frase == frase2:
    print('você escreveu um palindromo')
else:
    print('nada a declarar')