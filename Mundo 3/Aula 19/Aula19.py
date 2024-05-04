# Title: Dicionários

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
pessoas['peso'] = 98.5
'''pessoas['nome'] = 'Pedro' >> altera nome pra Pedro'''

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')

print(pessoas.keys())       >> Mostra a categoria (nome, ano, ...)
print(pessoas.values())     >> Mostra os nomes dos objetos
print(pessoas.items())      >> Ele mostra os dois

for k in pessoas.values():
    print(k)
    
for k,v in pessoas.items():
    print(f'{k} = {v}')

'''---------------------------------'''

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

'''---------------------------------'''

estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
    
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
        
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
