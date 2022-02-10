#\033[ stylo ; text ; back m
# stylo           text    black
# 0 - none      30 with     40
# 1 - bold      31 red      41
# 4 - underline 32 green    42
# 7 - negative  33 yellow   43
#               34 blue     44
#               35 roxo     45
#               36 ciano    46
#               37 cinza    47
# sintaxe:
#       \033[0;33;44m
print('\033[0;30;41m Olá mundo\033[m')
print('\033[1;33;44m Olá mundo\033[m')
print('\033[1;35;43m Olá mundo\033[m')
print('\033[30;42m Olá mundo\033[m')
print('\033[m Olá mundo\033[m')
print('\033[7;30m Olá mundo\033[m')

