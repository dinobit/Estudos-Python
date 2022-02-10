frase = 'Curso em Vídeo Python'
#21 espaços na memoria com indice de 0 a 20

#Fatiamento
print(frase[9])
print(frase[9:14])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

#Analise
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('xurupita'))
print('Curso' in frase)

#Transformação
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

frase2 = ('   Aprenda Python  ')
print(frase2)
print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())

#Divisao
print(frase.split())

#Junção
print('-'.join(frase))
