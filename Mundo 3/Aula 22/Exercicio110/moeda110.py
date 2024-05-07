def aumentar(preço = 0, taxa = 0, formato = False):
    res = preço + (preço * taxa/100)
    return res if formato is False else Moeda(res)
    
def diminuir(preço = 0, taxa = 0, formato = False):
    res = preço - (preço * taxa/100)
    return res if formato is False else Moeda(res)
    
def dobro(preço = 0, formato = False):
    res = preço * 2
    return res if formato is False else Moeda(res)
    
def metade(preço = 0, formato = False):
    res = preço / 2
    return res if formato is False else Moeda(res)

def Moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

def resumo(preço = 0, aumento = 10, redução = 5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{Moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'Aumento de {aumento}%: \t{aumentar(preço, aumento, True)}')
    print(f'Redução de {redução}%: \t{diminuir(preço, redução, True)}')
    print('-' * 30)


