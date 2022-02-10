#frase = str(input('Digite uma frase: '))
#frase = frase.upper()
frase = str(input('Digite uma frase: ')).upper().strip()
print('A quantidade de letras A na frase é {}'.format(frase.count('A')))
print('O ultimo A esta na posição {}'.format(frase.rfind('A')))
print('O primeir A esta na posição {}'.format(frase.index('A')))

