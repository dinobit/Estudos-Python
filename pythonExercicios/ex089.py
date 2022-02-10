boletim = list()
tmpaluno = list()
tmpnotas = list()

print('*:'*15)
print('{:^30}'.format('BOLETIM ESCOLAR'))
print('*:'*15)

while True:
    tmpaluno.append(str(input('Nome: ')))
    tmpnotas.append(float(input('Nota 1: ')))
    tmpnotas.append(float(input('Nota 2: ')))
    tmpnotas.append((tmpnotas[0] + tmpnotas[1]) / 2) #média
    tmpaluno.append(tmpnotas[:])
    print(tmpaluno)
    boletim.append(tmpaluno[:])
    tmpaluno.clear()
    tmpnotas.clear()

    keep=(str(input('Quer Continuar? (S/N) '))).strip().upper()[0]
    if keep == 'N':
        break

print('*:'*15)
print('{:<15}'.format('No.  Nome'), end='')
print('{:>15}'.format('Média'))
ss = 0
for c in range(0, len(boletim)):
    #print('{:<30} {:<30}'.format(c, boletim[c][0]), end='')
    print(c, end='    ')
    print(boletim[c][0], end='')
    print('{:>18}'.format(boletim[c][1][2]))
    ss += 1
while True:
    q = (int(input('Deseja ver as notas de qual aluno: (999 para encerrar) ')))
    #print(ss)
    if q == 999:
        break
    elif q < 0 or q > ss -1:
        print('entrada invalida!')
    else:
        print(f'Notas do aluno {boletim[q][0]} : {boletim[q][1][0]}, {boletim[q][1][1]}')

print('*:'*15)
print('{:^30}'.format('Até logo, volte sempre'))
print('*:'*15)