first = int(input('Digite o Primeiro termo de sua PA: '))
razao = int(input('Digite a razão da PA: '))
show = first
x = 10
#for c in range(0, 10):
#    print(show)
#    show += razao
while x > 0:
    print(show, end=' - ')
    show += razao
    x -= 1