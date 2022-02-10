from utilidadescev import moeda
from utilidadescev import dados

p = dados.leiaDinheiro('Digite o preço: R$')
#p = float(input('Digite o preço: R$'))
moeda.resumo(p, 35, 22)