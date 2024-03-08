lista = [[], []]
numero = 0
principal = []

for c in range(0,7):
    numero = int(input(f'Digite o {c+1}º valor: '))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)
        
lista[0].sort()
lista[1].sort()

print(f'Todos os valores: {lista}')
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores ímpares digitados foram: {lista[1]}')