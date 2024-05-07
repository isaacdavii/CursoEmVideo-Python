def ficha():
    print('-' * 20)
    print('  Ficha do Jogador')
    print('-' * 20)
    nome = str(input('Nome do Jogador: '))
    gols = str(input('Número de Gols: '))
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    if nome.strip() == '':
        nome = '<Desconhecido>'
    print(f'O jogador {nome} fez {gols} gols no campeonato.')

ficha()