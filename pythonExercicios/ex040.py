n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print ('Você ficou com media {:.2f} e esta \033[1:31:40m REPROVADO \033[m !'.format(media))
elif media >=5 and media <= 6.9:
    print('Você ficou com media {:.2f} e esta de \033[1:33m recuperação!\033[m'.format(media))
else:
    print('Você foi \033[1:32m APROVADO \033[m com média {:.2f}'.format(media))
