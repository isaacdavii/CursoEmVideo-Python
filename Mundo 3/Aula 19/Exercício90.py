aluno = dict()
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['media'] = float(input(f'Digite a média do {aluno["nome"]}: '))
if aluno['media'] >= 6.0:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'

for k, v in aluno.items():
    print('--------------------------------')
    print(f'{k} é igual a {v}.')
print()
resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
if resp == 'N':
    print('Fim!')