times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Flamengo',
        'São Paulo', 'Atlético-MG', 'Sport Recife','Avaí', 'Goiás', 'Bahia', 'Ceará',
        'Ponte Preta', 'Atlético-PR', 'Cuiabá','Atlético-GO', 'Ceará', 'Fluminense', 'Chapecoense')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros colocados são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos colocados são {times[-4:]}')
print('-=' * 15)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)