def leiaDinheiro(msg):
    ok = False
    v = 0
    while True:
        v = input(msg)
        if v.isnumeric():
            v = float(v)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido\033[m')
        if ok:
            break
    return v