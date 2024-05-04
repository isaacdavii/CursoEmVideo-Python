pessoas = dict()
soma = media = 0
galera = list() 

while True:
    pessoas.clear()
    pessoas['Nome'] = str(input('Nome: '))
    
    while True:
        pessoas['Sexo'] = str(input('Sexo [M/F]: ')).upper()
        if pessoas['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
        
    pessoas['Idade'] = int(input('Idade: '))
    soma += pessoas['Idade']
    galera.append(pessoas.copy())    
    
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()
        if resp in 'SN':
            break
        print('ERRO! Digite uma resposta válida!')
    if resp in 'N':
        break
    
print('-=' * 30)
print(f'Foram cadastradas {len(galera)} pessoas.')
media = soma / len(galera)
print(f'A média de idade é de {media:.2f} anos.')
print('As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]} ', end='')
print()
print('Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['Idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<< ENCERRADO >>>')