def voto(i):
    from datetime import date
    idade = date.today().year - i
    fato = ''
    if idade < 16:
        fato = "Impedido de votar"
    elif 18 >= idade < 65:
        fato = "Obrigatório"
    else:
        fato = "Obrigatório"
    return f'Com {idade} anos o voto é: {fato}'


nascimento = int(input('Digite o ano de nascimento: '))
print(voto(nascimento))