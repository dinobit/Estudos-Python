#valorest = [5, 8, 7, 13, 1]
#print(valorest)
#print(max(valorest))
#print(min(valorest))

#valores = [0, 0, 0, 0, 0]
valores = list()
for c in range(0, 5):
    nunin = int(input('Digite um valor: '))
    if c == 0 or nunin > valores[-1]:
        valores.append(nunin)
        print('Valor adicionado no fim da lista')
    else:
        pos = 0
        while pos < len(valores):
            if nunin <= valores[pos]:
                valores.insert(pos, nunin)
                print(f'adicionado na posição {pos} da lista')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {valores}')
