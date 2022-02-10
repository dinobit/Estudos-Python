try:
    salve = open('listinha2.txt', 'r')
    for linha in salve:
        print(linha)
        salve.close()
    print('leu')

except:
    salve = open('listinha2.txt', 'w')
    salve.close()
    print('criou')

salve = open('listinha.txt', 'r') # Abra o arquivo (leitura)
conteudo = salve.readlines()
conteudo.append('Biriburb biribá')   # insira seu conteúdo

salve = open('listinha.txt', 'w') # Abre novamente o arquivo (escrita)
salve.writelines(conteudo)    # escreva o conteúdo criado anteriormente nele.

salve.close()