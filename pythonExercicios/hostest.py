import os
iplist = []

def myping(host):
    response = os.system("ping -c 1 " + host)
    if response != 0:
        iplist.append(host)

while True:
    print(f'\033[0;33m', end='')
    print('Digite os 3 primeiros octetos da rede.')
    rede = str(input('Ex: (10.16.238)...    '))
    print(f'mostrar os IPs que não responderem da rede \033[0;34m{rede}.0/24\033[m')
    go = str(input('Enter para confirmar, 0 para descontinuar: ')).strip()
    if go == '':
        break

print(f'Testando a {rede}.0/24 - de 1 a 254')
for i in range(1, 254):
    #print(f'{rede}.{str(i)}')
    print(myping(f'{rede}.{str(i)}'))


print('=*'*40)
print('=*'*40)
print(f'\033[1;32m', end='')
print('lista dos IPs que não responderam:')
print(f'\033[0;31m', end='')
for c, v in enumerate(iplist):
    print(f'{v}\t', end='')
    if c % 5 == 0:
        print('')

