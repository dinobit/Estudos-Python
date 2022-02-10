import math
co = float(input('Digite a medida do cateto Oposto: '))
ca = float(input('Digite a medida do cateto Adjacente: '))
ht = math.hypot(co, ca)
htm = math.sqrt((co ** 2) + (ca ** 2))
print('A Hipotenusa do seu triangulo, usando modulo math mede {:.2f}'.format(ht))
print('A Hipotenusa do seu trinagulo, usando formula matematica mede {:.2f}'.format(htm))
