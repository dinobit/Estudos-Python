teste = []
filme = {
    'titulo':'Star Wars',
    'ano':1977,
    'diretor':'George Lucas'
}
filme2 = {
    'titulo':'Matrix',
    'ano':1999,
    'diretor':'Whatchovisk'
}
filme3 = {
    'titulo':'Hellboy',
    'ano':2005,
    'diretor':'Del Toro'
}
teste.append(filme)
teste.append(filme2)
teste.append(filme3)
print(teste)

arquivo = 'guarda.txt'

try:
    a = open(arquivo, 'a')
except:
    a = open(arquivo, 'c')
finally:
    for c, v in enumerate(teste):
        a.write(f'{teste[c]["titulo"]};{teste[c]["ano"]};{teste[c]["diretor"]}\n')
    a.close()