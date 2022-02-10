import math
angle = float(input('Entre com o seu angulo: '))
sen = math.sin(math.radians(angle))
cos = math.cos(math.radians(angle))
tan = math.tan(math.radians(angle))

print('O seno do angulo {:.2f} é {:.1f} \n O coseno é {:.2f} e a tangente é {:.2f}'.format(angle, sen, cos, tan))
