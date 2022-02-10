from time import sleep
###name = 'thiago'
###print(name)
###print(name[0])
###name.split()
##
##for c in range(0, len(name)):
##    #print(c)
##    if name[c] in 'aeiou':
##        print(name[c])
##
palavras = ('carro', 'casa', 'coronavirus', 'canoa', 'colher',
            'canhambeque', 'coração', 'credo', 'criquety',
            'cuzao', 'comala', 'criptomoeda', 'criatividade')
print('VOGAIS: \n \n')

for c in range(0, len(palavras)):
#    print(palavras[c])
    varredor = palavras[c]
#    print(varredor[0])
    print(f'Na palavra {palavras[c].upper()}, temos', end=' ')
    for r in range(0, len(varredor)):
        if varredor[r] in 'aeiou':
            print(varredor[r], end='')
    print('')


############SOLUÇÂO DO PROFESSOR##########
for p in palavras:
    print(f'\n Na palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

