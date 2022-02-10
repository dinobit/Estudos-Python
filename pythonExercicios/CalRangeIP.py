#crio a lista de IPs de 0 a 256

ipr = list()
for c in range(0,256):
    ipr.append(c)

#imprime a lista em 4 colunas
##for x in range(0,64):
##    for c in range(x,256,64):
##        if c < 10:
##            print(ipr[c],end='       ')
##        elif c > 9 and c <100:
##            print(ipr[c], end='      ')
##        else:
##            print(ipr[c], end='     ')
##    print()

#Dizeres leagais
print('*=' *20)
print(f'{"Calculo de IP/MASK/REDE":^40}')
print('*=' *20)



#pega o IP desejado para var IP
while True:
    print('Digite o final de IP desejado:')
    print('(Apenas o ultimo octeto.)')
    print('EX: \033[0;34m192.168.0.\033[0;31m68\33[m')
    ip = int(input('IP: '))
    if ip < 0 or ip > 256:
        print('Entrada inválida')
    else:
        break
#Pega a máscara desejada para var REDE
while True:
    print('Digite a máscara:')
    print('EX: \033[0;34m255.255.255.\033[0;31m248\33[m ou \033[0;31m /29\33[m')
    maskc = str(input('Mascara: ')).strip()
    print(maskc)
    print(maskc[1])
    if maskc[0] == '/':
        if maskc[1] != '2' and maskc[1] != '3':
            print('Rede inválida. Esse programa foi feito para trabalhar um range /24 _')
        elif maskc[1] == '2' or maskc[1] == '3':
            if maskc[2] == '4':
                rede = 0
                break
            elif maskc[2] == '5':
                rede = 128
                break
            elif maskc[2] == '6':
                rede = 192
                break
            elif maskc[2] == '7':
                rede = 224
                break
            elif maskc[2] == '8':
                rede = 240
                break
            elif maskc[2] == '9':
                rede = 248
                break
            elif maskc[2] == '0':
                rede = 252
                break
            else:
                print('Rede inválida. Esse programa foi feito para trabalhar um range /24')
    if maskc[0] != '/':
        if maskc in ('0','128','192','224','240','248','252'):
            rede = int(maskc)
            break
        else:
            print('Rede inválida. Esse programa foi feito para trabalhar um range /24')

#Printa o escolhido:
print(f'O IP escolhido foi {ip} e a mascara 255.255.255.{rede}')

if rede == 0:
    print(f'\033[0;32mIP da Rede\33[m * \031[0;31mBroadcast\33[m * \034[0;31m /29IP selecionado {ip} [m')
    for x in range(0,64):
        for c in range(x,256,64):
            if rede ==0:
                if ipr[c] == 0:
                    print('\33[0;32m', end='')
                elif ipr[c] == 255:
                    print('\33[0;31m', end='')
                elif ipr[c] == ip:
                    print('\33[0;34m', end='')
            print(f'{ipr[c]:^10}', end='')
            print('\33[m', end='')
            #if c < 10:
            #    print(ipr[c],end='       ')
            #elif c > 9 and c <100:
            #    print(ipr[c], end='      ')
            #else:
            #    print(ipr[c], end='     ')
        print('\b')