from random import randint
from time import sleep

print('-' * 30)
print('     JOGO DA MEGA SENA     ')
print('-' * 30)


jogos = []
jogo = []
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'\n-=-=-= SORTEANDO {quantidade} JOGOS =-=-=-\n')
for c in range(0, quantidade):
    for n in range(0, 6):
        numero = randint(1, 60)
        while numero in jogo:
            numero = randint(1, 60)
        jogo.append(numero)
    jogos.append(sorted(jogo[:]))
    jogo.clear()
    sleep(1)
for i, j in enumerate(jogos):
    print(f'Jogo {i + 1}: {j}')
    sleep(1)
print('\n-=-=-=-=-= < BOA SORTE! > =-=-=-=-=-=-')
print('-' * 30)