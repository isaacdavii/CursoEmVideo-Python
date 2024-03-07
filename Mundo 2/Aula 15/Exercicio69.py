homens = pessoas = mulheres = 0 
while True:
    idade = int(input("Insira a idade da pessoa: "))
    sexo = str(input("Digite o sexo da pessoa [H/M]: ")).upper()
    escolha = str(input("Quer continuar?[S/N]: ")).upper()
    if escolha == 'N':
        break
    if idade > 18:
        pessoas += 1 
    if sexo == 'H':
        homens += 1
    if sexo == 'M' and idade < 20:
        mulheres += 1
print(f"{pessoas} pessoas tem mais de 18 anos !")
print(f"{homens} homem(ns) foram cadastrados")
print(f"{mulheres} mulher(es) tem menos de 20 anos!")