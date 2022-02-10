tester = []
print(f'tester{tester}')
arquivo = 'guarda.txt'
filme = {}
try:
    a = open(arquivo, 'rt')
    for linha in a:
            dado = linha.split(';')
            #print(dado)
            dado[2] = dado[2].replace('\n', '')
            filme.clear()
            filme['titulo'] = dado[0]
            filme['ano'] = dado[1]
            filme['diretor'] = dado[2]
            tester.append(filme.copy())
            filme.clear()

except:
    print('Arquivo não existe')
finally:
    a.close()

print(f'tester{tester}')