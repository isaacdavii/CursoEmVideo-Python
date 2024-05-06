def maior(*numero):
    cont = maior = 0
    print('Analisando os valores passados!')
    print()
    for valor in numero:
        print(f'{valor} ', end=' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram digitados {len(numero)} números!')
    print(f'O maior valor informado foi {maior}!')
    
    
'''while True:
    num = int(input('Digite um número [999 p/ parar]: '))
    if num == 999:
        break'''
    
maior(5, 6, 8, 9, 7)