import Utilis, Conteudo
from time import sleep
while True:
    Utilis.title('UCM AVALIATOR')
    Utilis.menu('Menu principal', 'Ver Filmes', 'Ver Séries', 'Dar Notas', 'Batalha', 'Sair', 'About')
    x = (Utilis.validachoice(7))
    if x == 6:
        Conteudo.menu6()
    if x == 5:
        Conteudo.menu5()
        break
    if x == 1:
        Conteudo.menu1()
