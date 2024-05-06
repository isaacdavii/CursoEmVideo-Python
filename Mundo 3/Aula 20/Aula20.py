# Funções

def soma(a, b):
    print(f'A soma de {a} + {b} é: {a + b}')
    return a + b

soma(2, 3)

## Conceito de empacotar parâmetros
# [*num] significa que a pessoa jogará vários parâmetros joga na var num
def contador(*num):
    print(num)
    print(f'São {len(num)} números!')
    for valor in num:
        print(f'{valor} ', end='')
    print()
    print('FIM!')
    print()

contador(5, 7, 3, 1, 4)
contador( 5, 6, 8, 1, 1, 7)

## Adicionando os valores numa lista
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

def soma(*valores):
    sum = 0
    for num in valores:
        sum += num
    print(f'Somando os valores {valores}, temos {sum}')

soma(5, 2)
soma(2, 9, 4)
