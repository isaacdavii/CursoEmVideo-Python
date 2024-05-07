def notas():
    """
    Função que lê várias notas de um aluno e retorna um dicionário com a quantidade de notas, a maior nota, a menor nota, a média e a situação do aluno.
    """
    notas = []
    while True:
        nota = float(input('Digite a nota: '))
        notas.append(nota)
        continuar = input('Deseja continuar? [S/N] ').strip().upper()
        if continuar == 'N':
            break
    dicionario = {
        'Quantidade de notas': len(notas),
        'Maior nota': max(notas),
        'Menor nota': min(notas),
        'Média': sum(notas) / len(notas),
        'Situação': 'Boa :)' if sum(notas) / len(notas) >= 7 else 'Ruim :()'
    }
    return dicionario

print(notas())