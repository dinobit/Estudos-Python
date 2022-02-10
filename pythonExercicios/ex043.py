peso = float(input('Digite o seu peso em Kg: '))
altura = float(input('Digite a sua altura em metros: '))
imc = peso / (altura ** 2)
print('Seu IMC é {:.2f}'.format(imc))
if imc <= 18.5:
    print('Seu status é: Abaixo do Peso!')
elif imc > 18.5 and imc <= 25:
    print('Seu status é: Peso ideal!')
elif imc > 25 and imc <= 30:
    print('Seu status é: Sobrepeso!')
elif imc > 30 and imc <= 40:
    print('Seu status é: Obesidade!')
else:
    print('Seu status é: Obersidade Morbida, vai morré fedaputa, para de come!')