# Criando a matriz 3x3
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = somaColuna = 0
maior = 0

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite o valor para a posição [{i}][{j}]: '))
        if matriz[i][j] % 2 == 0:
            somaPar += matriz[i][j]

    if j == 2:
        somaColuna += matriz[i][j]
                    
for c in range(0 ,3):
    if c == 0:
        maior = matriz[1][c]
    else:
        if matriz[1][c] > maior:
            maior = matriz[1][c]
            
# Mostrando a matriz na tela
print()
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()
print()
print(f'A soma dos valores pares é {somaPar}')
print(f'A soma dos valores da terceira coluna é {somaColuna}')
print(f'O maior valor da segunda linha é {maior}')