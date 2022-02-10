cont = soma = 0
while True:
    valor = int(input('Digite um valor: (999 para FIM)'))
    if valor == 999:
        break
    else:
        cont +=1
        soma += valor

print(f'Você digitou {cont} valores, e a soma entre eles é {soma}')

