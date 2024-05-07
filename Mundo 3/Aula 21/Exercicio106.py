comando = ''

while True:
    comando = input('Função ou Biblioteca: ').strip().lower()
    if comando == 'fim':
        break
    help(comando)
print('Até logo!')
