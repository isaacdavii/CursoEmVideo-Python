import moeda109

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda109.Moeda(p)} é {moeda109.metade(p, True)}')
print(f'O dobro de {moeda109.Moeda(p)} é {moeda109.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda109.aumentar(p, 10, True)}')
print(f'Diminuindo 10%, temos {moeda109.diminuir(p, 10, True)}')
