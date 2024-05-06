from random import randint

def sorteia(lista):
    for cont in range(0, 5):
        lista.append(randint(1, 10))
    print(f'Os valores sorteados foram: {lista}')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos valores pares é: {soma}')

numeros = []
sorteia(numeros)
somaPar(numeros)
print()
print('FIM!')
print()
