import moeda108

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda108.Moeda(p)} é {moeda108.Moeda(moeda108.metade(p))}')
print(f'O dobro de {moeda108.Moeda(p)} é {moeda108.Moeda(moeda108.dobro(p))}')
print(f'Aumentando 10%, temos {moeda108.Moeda(moeda108.aumentar(p, 10))}')
print(f'Diminuindo 10%, temos {moeda108.Moeda(moeda108.diminuir(p, 10))}')
