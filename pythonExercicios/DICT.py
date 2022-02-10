"""
Declarando dicionarios:

dados = ditc()
ou
dados = { }

"""
filme = {
    'titulo':'Star Wars',
    'ano':1977,
    'diretor':'George Lucas'
}

#não tem append para dic. Para adicionar um novo:
filme['nota']=5
filme['porno']=False

#removere elementos
del filme['porno']

#print todos os valores
print(filme.values())
#print as chaves
print(filme.keys())
#valores e chaves
print(filme.items())

#para cada key e valor no dicionario filme:
for k, v in filme.items():
    print(f'O {k} é {v}')

# pode dicionario dentr de fila

#PRATICA:
pessoas = {'nome':'Gustavo','sexo':'M','idade':22}
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
#para cada chave
for k in pessoas.keys():
    print(k)
#para cada valor
for k in pessoas.values():
    print(k)
#para cada chave e valor
for k, v in pessoas.items():
    print(f'{k} = {v}')
#apagando
del pessoas['sexo']

#mudando o valor de um item
pessoas['nome'] = 'Leandro'

print(pessoas.values())

###### DICIONARIO DENTRO DE LISTA pra puts da vida com o Bruno#######

estado1 = {'uf':'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf':'São Paulo', 'sigla':'SP'}
brasil = list()
brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
estado = dict()
brasil = list ()

#FORMA ERRADA... ultima entrada sempre irá sobrepor
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    print(e)

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')


print('*'*10)
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()