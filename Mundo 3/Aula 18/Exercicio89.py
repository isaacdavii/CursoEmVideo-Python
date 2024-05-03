alunos = []

while True:
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
    if nome.lower() == "sair":
        break
    
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
    
    aluno = [nome, nota1, nota2]
    alunos.append(aluno)

print("\nBoletim dos Alunos\n")
for aluno in alunos:
    nome = aluno[0]
    media = (aluno[1] + aluno[2]) / 2
    print(f"Aluno: {nome} - Média: {media:.2f}")

while True:
    opcao = input("\nDigite o nome do aluno para ver as notas individuais (ou 'sair' para encerrar): ")
    if opcao.lower() == "sair":
        break
    
    encontrado = False
    for aluno in alunos:
        if aluno[0] == opcao:
            encontrado = True
            print(f"Notas do aluno {aluno[0]}: {aluno[1]}, {aluno[2]}")
            break
    
    if not encontrado:
        print("Aluno não encontrado.")