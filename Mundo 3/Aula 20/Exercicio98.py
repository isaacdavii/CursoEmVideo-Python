def contador(opcao):
    if opcao == 1:
        for i in range(1, 11):
            print(i, end=' ')
        print('FIM')
    if opcao == 2:
        for i in range(10, 0, -2):
            print(i, end=' ')
        print('FIM')
    if opcao == 3:
        numero1 = int(input('Digite um número inicial: '))
        numero2 = int(input('Digite um número final: '))
        forma = int(input('Digite a forma de contagem: '))
        print(f'Contagem de {numero1} até {numero2} de {forma} em {forma}:')
        for i in range(numero1, numero2, forma):
            print(i, end=' ')
        print('FIM')

op = int(input('Digite a forma de contagem: '))
contador(op)