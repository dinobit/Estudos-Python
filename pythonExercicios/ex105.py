def notas(*r, sit=False):
    """
    Recebe x notas e retorna um dicionario com a quantidade de notas
    a maior nota, a menor nota, a média da turma e se especificado como
    True, a situação geral também é passada
    :param r: notas dos alunos
    :param sit: situação da média (Ruim, Aceitavél e Boa)
    :return: Retorna um dicionário especificando acima.
    """""
    tn = {}
    qnt = (len(r))
    sit = str
    tn['Quantidade de Notas'] = qnt
    maior = menor = r[0]
    for c in range(0, qnt):
        if r[c] > maior:
            maior = r[c]
        if r[c] < menor:
            menor = r[c]
    tn['Maior nota'] = maior
    tn['Menor nota'] = menor
    tn['Média da turma'] = sum(r)/qnt
    if tn['Média da turma'] < 5:
        situac = 'Ruim'
    elif 5 <= tn['Média da turma'] <= 7:
        situac = 'Aceitavel'
    else:
        situac = 'Boa'
    if sit:
        tn['Situação'] = situac
    return tn


resp = notas(5.5, 2.5, 8.5, sit=True)
print(resp)
resp = notas(2, 3, 2, 1, sit=True)
print(resp)
resp = notas(5, 4.4, 6, 8, 10, sit=True)
print(resp)
resp = notas(10, 7, 10, 9, 7, 6, 10, 10, 9, sit=True)
print(resp)
help(notas)