def area(a, b):
    terreno = a * b
    print(f'O terreno tem área de {terreno:.2f}m².')

print ('---------------------')
print('Controle de Terrenos')
print ('----------------------')

largura = float(input('Qual a largura(m) do terreno: '))
comprimento = float(input('Qual o comprimento(m) do terreno: '))

area(largura, comprimento)