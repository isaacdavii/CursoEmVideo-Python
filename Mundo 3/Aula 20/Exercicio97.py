def titulo(txt):
    tamanho = len(txt) + 4
    print('-' * tamanho)
    print(f'  {txt}')
    print('-' * tamanho)
    
mensagem = str(input('Digite a mensagem:'))
titulo(mensagem)