st1=str('\33[1:30:0m')
st2=str('\33[1:0:40m')
st0=str('\33[m')
print('{}*-*{}'.format(st1, st0)*10)
print('{}*-*{}'.format(st2, st0)*10)
