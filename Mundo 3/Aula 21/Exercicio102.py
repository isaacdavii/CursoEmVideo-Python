def fatorial():
    """
    => É uma função fatorial que retorna o valor fatorial de um número desejado
    param n: int -> número a ser calculado o fatorial
    return: int -> retorna o valor fatorial do número desejado
    
    """
    n = int(input('Digite um número: '))
    f = 1
    for c in range(n, 0, -1):
        f *= c
    print(f'O fatorial de {n} é {f}')
    
fatorial()