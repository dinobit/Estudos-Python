host =str(input('Digite IP: '))
shost = host.split('.')
print(host)
print(shost)
print(shost[0])
print(len(shost))

if len(shost) != 4:
    print('IP invalido')
else:
    try:
        po = int(shost[0])
        so = int(shost[1])
        to = int(shost[2])
        qo = int(shost[3])

    except:
        print('IP INVALIDO')

for i in range(0, 3):
    if 0 < shost[i] < 255:
        print('ok pass2')
    else:
        print(f'erro no {i+1}º octeto')
