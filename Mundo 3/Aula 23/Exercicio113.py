def leiaInt():
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido.')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não informar os dados.')
            return 0
        else:
            return print(f'Você digitou o número {n}!')

def leiaFloat():
    while True:
        try:
            n = float(input('Digite um número real: '))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número real válido.')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não informar os dados.')
            return 0
        else:
            return print(f'Você digitou o número {n}!')

leiaInt()
leiaFloat()