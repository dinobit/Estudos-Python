first = int(input('Digite o Primeiro termo de sua PA: '))
razao = int(input('Digite a razão da PA: '))
show = first
x = 10

while x > 0:
    print(show, end=' - ')
    show += razao
    x -= 1
    if x == 0:
        x = int(input('Quer mostrar mais quantos termos? '))
