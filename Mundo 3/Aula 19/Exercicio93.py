ficha = dict()
gols = list()

ficha['Nome'] = str(input('Nome do jogador: '))
ficha['Partidas'] = int(input('Quantas partidas ele jogou: '))

for i in range(ficha['Partidas']):
    gols.append(int(input(f'Quantos gols ele fez na partida {i + 1}: ')))
    
ficha['Gols'] = gols
ficha['Total'] = sum(gols)

print()
for k, v in ficha.items():
    print(f'O campo {k} tem o valor {v}')

print()
print('-=' * 30)
print(f'O jogador {ficha["Nome"]} jogou {ficha["Partidas"]} partidas.')
for i in range(ficha['Partidas']):
    print(f'  => Na partida {i + 1}, fez {ficha["Gols"][i]} gols.')
print(f'Foi um total de {ficha["Total"]} gols.')
print('-=' * 30)
print()
