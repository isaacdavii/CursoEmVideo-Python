from datetime import datetime

ficha = dict()

ficha['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
ficha['Idade'] = datetime.now().year - nascimento
ficha['Carteira'] = int(input('Carteira de Trabalho (0 não tem): '))
if ficha['Carteira'] == 0:
    print('-=' * 30)
    for k, v in ficha.items():
        print(f'{k} tem o valor {v}')
    print()
else:
    ficha['Contratação'] = int(input('Ano de Contratação: '))
    ficha['Salário'] = float(input('Salário: R$ '))
    ficha['Aposentadoria'] = ficha['Idade'] + (ficha['Contratação'] + 35) - datetime.now().year
    print('-=' * 30)
    for k, v in ficha.items():
        print(f' - {k} tem o valor {v}')
    print()