def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f
    
def dobro(n):
    return n * 2

def triplo(n):
    return n * 3

def raiz(n):
    return n ** 0.5

def quadrado(n):
    return n ** 2

def cubo(n):
    return n ** 3

def par(n):
    return n % 2 == 0

def primo(n):
    if n < 2:
        return False
    for c in range(2, n):
        if n % c == 0:
            return False
    return True

