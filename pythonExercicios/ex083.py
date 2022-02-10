#crio a lista e a var que vai receber a expressão já é atribuida
exl = list()
ex = (str(input('Digite um expressão: '))).strip()
wrong = bool(False)
#quebro a string ex e coloco na lista exl
for c in range(0, len(ex)):
    exl.append(ex[c])
#Copio a lista exl para sexl, depois inverto a lista sexl
sexl = exl[:]
sexl.sort(reverse=True)

#verifico a quantidade de ( e ):
abre = exl.count('(')
fecha = exl.count(')')

#se a quantidade difere expressão esta errada:
if abre != fecha:
    wrong = True
#se não ele continua verificando
#Se ) ven antes de ( então expressão esta errada:
elif exl.index('(') > exl.index(')'):
    wrong = True
#Se ( vem em primeiro na lista invertida, então tmb ta errado:
elif sexl.index('(') < sexl.index(')'):
    wrong = True

if wrong == False:
    print('Expessão valida!')
else:
    print('Expressão invalida!')
