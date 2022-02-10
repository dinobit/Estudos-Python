continuar = 'S'
count = soma = 0
while continuar == 'S':
    valor = float(input('Digite um valor: '))
    if count == 0:
        menor = maior = valor
    if valor < menor:
        menor = valor
    if valor > maior:
        maior = valor
    if valor != 0:
        count += 1
    soma += valor
    continuar = str(input('Deseja digitar novo valor? (S) (N)').strip().upper())[0]
print('O menor valor digitado foi {}. O Maior valor digitado foi {}'.format(menor, maior))
print('A soma entre os valores digitados foi {} \n e a média foi {}'.format(soma, soma / count))